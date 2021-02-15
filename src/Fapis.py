import pandas as pd
import geopandas as gpd
import sys
from dotenv import load_dotenv
import os
import requests
import json
from functools import reduce
import operator
from cartoframes.viz import Map, Layer, popup_element
from haversine import haversine
from pymongo import MongoClient, GEOSPHERE
import shapely.geometry

def create_querry(gdf, nombre, lon, lat):
    '''
    
    gdf : nombre del data frame con la columna geometry creada 
    nombre : de las empresas 
    lon: longitud de la empresa
    lat: latiutud  de la empresa

    '''
    client = MongoClient() # conectamos con mongo 
    db = client.geoloco # genera bbdd con un nombre en este caso geoloco
    collection = db.create_collection(f"{nombre}") # genera collecion con formato de la empresa 
    collection = db[f"{nombre}"] # genera collecion con formato de texto de la empresaa( ¿este podria sobrar ?)
    collection.create_index([("geometry", "2dsphere")]) # creamos index con dos columnas '2dsphere' sera el geojson

    data = gdf.to_dict(orient='records') # conversion del DF para que mongo pueda 'leerlo'
    collection.insert_many(data) # insertamos en mongo el dicionario como una coleccion 
    fillter =  [{ "$geoNear": {'near': [lon,lat],
                 'distanceField': 'distance',
                 'maxDistance': 7000,
                 'distanceMultiplier': 6371, 
                 'spherical'  : True}}]
    distance = collection.aggregate(fillter)
    result = json.loads(dumps(distance))
    return result

def geoenterprise(df_ofi):
    '''
    recibe un data frame y devuelve un dicionario de dicionarios con:
    - nombre de la empresas 
    - formato para hacer llamadas 
    - latitud y longitud de la empresa 
    ''' 
    dict_coordenadas = {} #Iniciamos dicionario
    for i in df_ofi.index: #Captura las coordenadas del registro i-esimo
        company = df_ofi.loc[i]['name'] # Alamcena nombre de 
        lat = df_ofi.loc[i]['latitude'] #Almacena latitud
        long = df_ofi.loc[i]['longitude'] #Almacena longitud
        empresa_coor= [lat, long]    
        empresa = {'type': 'Point', 'coordinates': empresa_coor}
        dict_coordenadas[company]=empresa #Agregamos al dicionario 

    return dict_coordenadas

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)


def list_enterprise_name(df_ofi):
    '''
    Recibe un data frame y devuelve una lista de con el nombre de las empresas
    '''
    company_list = []
    for i in df_ofi.index:
        company_list.append(df_ofi.loc[i]['name'])
    return company_list