import os  # Módulo para manejar rutas y verificar existencia de archivos/carpetas
import shutil  # Módulo para mover archivos y directorios

try:
    # Solicita al usuario las rutas necesarias
    usuario_carpeta = input("Ingresa la ruta de la carpeta donde se encuentra el documento: ")
    usuario_documento = input("Ingresa la ruta del documento: ")
    usuario_trasladar = input("Ingresa la ruta de la carpeta para trasladar el documento: ")

    # Verifica que la carpeta donde está el documento existe
    if os.path.isdir(usuario_carpeta):
        # Verifica que la carpeta de destino existe
        if os.path.isdir(usuario_trasladar):
            # Verifica que el documento existe antes de moverlo
            if os.path.exists(usuario_documento):
                shutil.move(usuario_documento, usuario_trasladar)  # Mueve el archivo a la carpeta destino
                print("Documento trasladado correctamente.")
            else:
                print("Documento no encontrado.")  # Mensaje de error si el archivo no existe
        else:
            print("Carpeta de destino no encontrada.")  # Mensaje de error si la carpeta destino no existe
except Exception as error:
    # Captura cualquier error inesperado y lo muestra en pantalla
    print(f"Error en el programa: {error}.")
