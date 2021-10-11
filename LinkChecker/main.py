import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

searched_links = []
broken_links = []

def find_broken_links(url):
    if(url not in searched_links) and (("mailto:") not in url) and ("Javascript:" not in url) and ((".png") not in url) and ((".jpg") not in url) and ((".jpeg") not in url):
            for i in url:
                try:
                    requestObj = requests.get(i)
                    searched_links.append(i)
                    if (requestObj.status_code == 404):
                        broken_links.append("Broken: link " + i)
                        print(broken_links[-1])
                    else:
                        print("Not broken: link " + i)

                except Exception as e:
                    print("Error: " + str(e))

    else:
        print('Something else went wrong.')

link_file = 'C:/Users/johnl/MyCodePortfolio/LinkChecker/Links'
new_links = []
with open(link_file,'r') as f:
    new_links = f.read().splitlines()


correct_link = 'https://www.facebook.com'

find_broken_links(new_links)