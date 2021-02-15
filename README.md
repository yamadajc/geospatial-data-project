# GeoSpatial Data Project

![portada](https://github.com/yamadajc/geospatial-data-project/blob/main/images/1.jpeg)


Los planes de expansion de una empresa de videojuegos indican que España podria ser el destino mas oportuno para afianzar el posicionamiento europeo de su actividad. Deseamos saber cual es la ciudad española con mayor concentracion de empresas que cuenten con  mas de un millon de euros recaudados en rondas de financiacion y que ademas hayan sido creadas en el siglo XXI con el fin de instalarnos a su alrededor.

Partimos de una base de datos inicial, companies.csv,  con un listado de empresas con  un mas de 18.000 empresas repartidas por todo el mundo. 

Tras un analisis previo recurimos a la API de foursquare para cumplir con los requerimientos de distintos departamentos.
 - los diseñadores desean inspiracion, asi que se tendra que asegurar la cercania de museos.
 - se priorizara la localizacion mas cercana al aereopuerto.
 - se a demostrado que los trajadores son mas felices y productivos cuando tienen un starbucks cerca de la oficina ... o eso dicen los ejecutivos.

## Objetivos:
- Realizar consultas en mongo db para obtener un listado de empresas inicial.
- Realizar llamadas a API y extraer datos geoposicionales para su posteriror tratamiento. 
- Tratamiento de datos geojson en mongo destinados a la geolocalizacion y calculo de distancias. 
