"""
OFFICIAL DOC: https://pypi.org/project/cloudscraper/
Requirements:
  -python
  -pip
"""
# import cloudscraper
import sys
# from Utils.utils import write_file, get_page_content
from Utils.utils import write_file, get_page_content

def scan_write_file(url, file_name):
    html_content = get_page_content(url)
    write_file(html_content,file_name) 

# MAIN
file_name = "HTMLContent"

if len(sys.argv) > 1:
  local_url = sys.argv[1]
  scan_write_file(local_url,file_name)
else:
  url = input("Insert the url: ").strip()
  if url:
    scan_write_file(url,file_name)
  else:
    print("Insert a valid URL")
