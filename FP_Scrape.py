'''
Scrapes images that were liked by given user to local storage.
'''
import requests
from bs4 import BeautifulSoup as BS
def url_from_soup(soup):
  for link in soup.find_all('a'):
    if ("i/funnypics/" in link.get('href')):
      print(link)
  
def main():
  web_URL = "http://www.funnyism.com/user/foodeatsi"
  req_raw = requests.get(web_URL)
  if not (req_raw.status_code == 200):
    print("Error with url request")
    return

  soup = BS(req_raw.text, 'html.parser')

if __name__=="__main__":
  main()
