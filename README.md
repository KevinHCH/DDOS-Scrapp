# DDOS-Scrapp
Scripts para saltarse bloqueo de Cloudflare <br>
Requerimientos:
- Python [3]
- Pip [3]
## Pasos a seguir
- Ejecutar el script `deploy.sh` **Ejecutar este script como ROOT**
	- Si aparece error en consola es necesario usar versiones de Python3 y pip3
	- En máquinas CENTOS 7 aparece Error de OpenSSL, significa que es una version antigua de python, es solo una advertencia <br>
**El resto de archivos no es necesario ejecutarlos como ROOT, es mejor cambiar el usuario**
- Ejecutar `index.py`, admite pasarle la URL de la pagina objetivo  + el nombre que se creara y en el que se escribirá el contenido HTML (el nombre es opcional)por parámetro en la invocación del script o el propio script pedirá una URL por consola
	- Ejemplo: `python index.py https://example.es <mi_archivo>`
	El script creará una archivo con todo el contenido HTML que haya conseguido de la página objetivo
- Ejecutar script `getElementsByTagName.py`, en la llamada de este script **es necesario** pasarle **primero el nombre del archivo(sólo el nombre, NO hace falta la extension)** y **el nombre de la etiqueta HTML** que se va a buscar en el archivo prviamente creado 
	- Ejemplo: `python getElementsByTagName.py HTMLContent img` (Buscará en el archivo HTML previamente creado con el script anterior y buscara todas las etiquetas img, y creará un archivo `JSON` con los datos obtenidos)

Todos estos scripts son modificables en función de lo que se quiera obtener
### Links DOC oficiales
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) : Permite buscar elementos HTML con sus valores, atributos, childnodes como en JS
- [Cloupscraper](https://pypi.org/project/cloudscraper/) : Salta bloqueo DDOS de cloudflare, permite muchas configuraciones (guardar cookies, sessiones, usar otros clientes para evitar bloqueo)
