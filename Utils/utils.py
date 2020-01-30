"""
OFFICIAL DOC: https://pypi.org/project/cloudscraper/
Requirements:
  -python
  -pip
"""
import cloudscraper

def write_file(content,name, extension = "html"):
  file_name = name + "." + extension
  file = open(file_name, 'w+')
  file.write(content)
  print(f"The file: {file_name} has been created")

"""
Funcion que se salta el DDOS-protect de cloudflare
y sirve el contenido de la pagina
"""
def get_page_content(uri):
  # uri = "https://eltelegrafo.com.ec/"
  scraper = cloudscraper.create_scraper()
  content = scraper.get(uri).text
  return content