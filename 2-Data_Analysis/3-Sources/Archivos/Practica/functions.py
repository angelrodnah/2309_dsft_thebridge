import os
import shutil

def select_dir(ruta):
    os.chdir(ruta)

def create_categories():
    os.makedirs('Imagenes', exist_ok=True)
    os.makedirs('Documentos', exist_ok=True)
    os.makedirs('Softwares', exist_ok=True)
    os.makedirs('Otros', exist_ok=True)

def move_files(doc_types, img_types, software_types):
    for archivo in os.listdir():
        archivo = archivo.lower()
        if os.path.isdir(archivo):
            print(archivo, "Es una carpeta")
        elif archivo.endswith(doc_types):
            try:
                shutil.move(archivo, "Documentos")
            except Exception as e:
                print(e)
        elif archivo.endswith(img_types):
            try:
                shutil.move(archivo, "Imagenes")
            except Exception as e:
                print(e)
        elif archivo.endswith(software_types):
            try:
                shutil.move(archivo, "Softwares")
            except Exception as e:
                print(e)
        else:
            try:
                shutil.move(archivo, "Otros")
            except Exception as e:
                print(e)