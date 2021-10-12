import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from datetime import datetime

now = datetime.now()
searched_links = []
broken_links = []
date = now.strftime(" -- %m/%d/%y")
def find_broken_links(url):
    if(url not in searched_links) and (("mailto:") not in url) and ("Javascript:" not in url) and ((".png") not in url) and ((".jpg") not in url) and ((".jpeg") not in url):
            for i in url:
                try:
                    requestObj = requests.get(i)
                    searched_links.append(i)
                    if (requestObj.status_code == 404):
                        broken_links.append("Broken: link " + i)
                        print(broken_links[-1])
                    elif (i == ''):
                        break
                    else:
                        print("Not broken: link " + i)

                except Exception as e:
                    print("ERROR ERROR: Bad Link " + i)
                    broken_links.append(i)

    else:
        print('Something else went wrong.')

    if not 'bad_links.txt':
        g = open('bad_links.txt', 'x')
    else:
        for i in broken_links:
            g = open('bad_links.txt','a')
            g.write(i)
            g.write(date)
            g.write('\n')
    f.close()
    g.close()

link_file = 'Links.txt'
new_links = []
with open(link_file,'r') as f:
    new_links = f.read().splitlines()

find_broken_links(new_links)
