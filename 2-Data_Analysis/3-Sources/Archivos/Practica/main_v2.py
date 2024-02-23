from clase import Fichero
from variables import * 

documentos = Fichero("Documentos", doc_types, ruta)
imagenes = Fichero("Imagenes", img_types, ruta)
softwares = Fichero("Softwares", software_types, ruta)
new_categorie = Fichero("Markdowns", (".md"), ruta)
# new_categories...
otros = Fichero("Otros", (), ruta)