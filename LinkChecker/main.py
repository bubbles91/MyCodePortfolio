import time

import requests
from os.path import exists
from datetime import datetime

now = datetime.now()
searched_links = []
broken_links = []
date = now.strftime(" -- %m/%d/%y")
IFTTT_url = 'https://maker.ifttt.com/trigger/{}/with/key/'
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

    if not exists('bad_links.txt'):
        g = open('bad_links.txt', 'w')

    for i in broken_links:
        g = open('bad_links.txt', 'a')
        g.write(i)
        g.write(date)
        g.write('\n')
        g.close()
    f.close()

    if not broken_links:
        resp = 'No Bad Links!'
    else:
        resp ='Bad Links: <br>' + '\n'.join([str(i[9:]) for i in broken_links])

    return  resp

def post_ifttt_webhook(event, value1):
    data1 = {'value1': value1}
    ifttt_event_url = IFTTT_url.format(event)
    requests.post(ifttt_event_url, data1)
    time.sleep(21600)

link_file = 'Links.txt'
new_links = []
with open(link_file, 'r') as f:
    new_links = f.read().splitlines()

while True:
    post_ifttt_webhook('Link_Check', find_broken_links(new_links))
