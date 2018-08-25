# -*- coding: UTF-8 -*-
'''
Created on Aug 25, 2018

@author: Antoni

Primero se debe identificar la estructura del cuerpo del sitio del cual queremos obtener la información. 
inspeccionar para ver el codigo fuente del sitio, en primera instancia nos importará obtener la URL de la imagen
para que posteriormente usar esa URL en nuestro programa con la finalidad de poder guardar a nivel local todas las imagenes que queramos de este sitio de comics.
en el sitio cada imagen está enumerada, lo cual significa que existe un patrón del cual se puede sacar provecho para poder obtener las magenes.
Las imagenes del sitio se descargarán en el directorio del proyecto
'''
import urllib.request  # va a permitir guardar de manera muy sencilla las imagenes
from bs4 import BeautifulSoup # nos permite parsear ese texto (obtener el String de HTML) y ponerlo modificar y acceder a el como si fuera un arbol. Esta libreria nos dará una serie de herramientas para que podamos obtener información del sitio.
import requests # Nos permite hacer solicitudes a internet y podernos traer el contenido HTML o cualquier otro contenido que se puede transferir a travez de internet (archivos con formatos: json, xml y en este caso html)  de diferentes sitios web  


def run():
    for i in range(1, 6):
        #requests hace una solicitud a la página web y usamos la función "get" de requests, la dirección del sitio como parametro, se formatea ese String de parámetro para que se agrege el número del rango cuando se itere
        response = requests.get('https://xkcd.com/{}'.format(i))
        # Se desea parsear el documento, para eso vamos a crear una instancia de BeautifulSoup, BeautifulSoup nos va a permitir parsear el contenido de la respuesta, y para obtenerla vamos a acceder al atributo content de la respuyesta. Como segundo parámetro para construir este parseador vamos a decirle que el contenido que vamos a revibir es un HTML- BeautifulSoup nos permite parsear distintos tipos de contenidos y para poderlo hacer le tenemos que especificar que parseador necesitamos utilizar 
        soup = BeautifulSoup(response.content,'html.parser')
        # image_container es una referencia a la etiqueta imagen. Le decimos al documento parseado que encuentre el nodo con id='comic' 
        image_container = soup.find(id='comic')
        # Una vezque ya tenemos una referencia al div vamos a poder obtener la URL. usamo el método find para ahora si encontrar la etiqueta image (img) y acceder al atributo source(src) porque allí se encuentra la información que necesitamos.
        image_url = image_container.find('img')['src']
        # vamos a obtener una referencia al nombre de la imagen para porla guardar con el nombre original con la que se guardó en el servidor. Tomamos la URL y la dividimos por las diagonales que contiene y vamos a obtener la referencia a la última diagonal. Accedimos a indices, el -1 estamos obteniendo el último elemento, el nombre de la imagen.
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen: {}'.format(image_name))
        # último paso es poder guardar esta imagen. la función urlretrieve del paquete urllib necesita dos parámetos: la URL de donde se encuentra nuestra imagen (HTTPS lo colocamos ya que el cógigo html5 utiliza // que es una notación que significa, utiliza el mismo transporte de la página web: https). como no tenemos esta información en image_url (simplemente tenemos //) para poder hacer una solicitud correcta necesitamos decir https:{}. Vamos a formatear este String y vamos a darle la URL de la imagen como primer parametro y como segundo parámetro el nombre del archivo con el cual vamos a guardar la imagen, en este caso: image_name
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
    run()