'''
Scrapes images that were liked by given user to local storage.
'''
import requests
from bs4 import BeautifulSoup as BS
import re

def url_from_soup(soup):
  links = []
  for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))
  return(links)

def image_url_from_list(links):
  for link in links:
    pass
  
def soup_from_url(url):
  req_raw = requests.get(url)
  if not (req_raw.status_code == 200):
    # Needs to do something about the broken return
    print("error with %s" % url)
  soup = BS(req_raw.text, 'html.parser')
  return soup
  
def main():
  web_URL = "http://www.funnyism.com/user/foodeatsi"
  
  user_page_soup = soup_from_url(web_URL)
  user_feed_links = url_from_soup(user_page_soup)

if __name__=="__main__":
  main()
