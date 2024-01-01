import threading
import requests
import csv

def obtener_data():
    lista = []
    # Simulación de obtener información de una URL (puedes cambiar este método)
    # Esto es solo un ejemplo, deberás modificar esta función según tus necesidades
    #lista_urls = [
    #    "https://www.ejemplo.com",
    #    "https://www.otroejemplo.com",
    #    "https://www.ultimo-ejemplo.com"
    #]
    with open("C:/UTPL 3semestre/Programacion Avanzada/Ejemplos/Semana_12/ae2-2bim-aa23/informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            # pass
             cadena = row[0].split("|")[1]
             cadena = cadena.replace(" ", "+")
             lista.append(cadena)    

    return lista

def worker(url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url))
    # Obtener el contenido de la URL
    response = requests.get(url)
    if response.status_code == 200:
        # Escribir el contenido en un archivo de texto
        url2=url.replace('https://', '').replace('www.', '').replace('es.wikipedia.org/wiki/', '')
        print(url2)
        with open(f"salida/"+url2+".txt", "w", encoding='utf-8') as file:
            file.write(response.text)
        print(f"Contenido de {url} guardado en archivo")
    else:
        print(f"No se pudo obtener el contenido de {url}")

    print("Finalizando %s" % (threading.current_thread().getName()))

# Obtener las URLs a procesar
urls = obtener_data()

for url in urls:
    # Crear hilos para procesar cada URL
    hilo = threading.Thread(name='descargando', target=worker, args=(url,))
    hilo.start()
