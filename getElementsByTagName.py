from bs4 import BeautifulSoup
from Utils.utils import write_file
from pprint import pprint
import sys
import json

# Lee el archivo de la pagina que se ha escaneado y guardado y parsea a HTML 
# para poder buscar elementos como en HTML
soup = BeautifulSoup(open('./HTMLContent.html'), 'html.parser')

# MAIN
tag = sys.argv[1]
html_elements = soup.find_all(tag)
if tag is None:
  print("""We need a HTML TAG when you call the script.\n
          Example: python getElementsByTagName.py img
        """)
  sys.exit

# Se recorre el array de elementos encontrados con el TAG pasado por 
# consola y por un FOR se puede ir buscando lo que se quiera, ya sea ATTR, VALUE...
# Ver DOC: BeautifulSoup
json_elements = [{"src": element.get('src'), "data-src": element.get("data-src")} for element in html_elements]

write_file(json.dumps(json_elements, indent=2), "tags", "json")