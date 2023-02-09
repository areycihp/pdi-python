# Listar archivos en la carpeta de New Images 
from os import scandir, getcwd


def ls(ruta = 'Images/PreImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


print(ls())


def lsReal(ruta = 'Images/NewImages/'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


print(lsReal())