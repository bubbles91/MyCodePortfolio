# AppName: Link Checker
# Use: Checks links that are added to a txt file for validity and emails using webhook the outcome.
# Created by John Lovelace, 10/12/21


import time
import requests
from os.path import exists
from datetime import datetime
# Init variables
now = datetime.now()
broken_links = []
date = now.strftime(" -- %m/%d/%y")
IFTTT_url = 'https://maker.ifttt.com/trigger/{}/with/key/'

# Defines the function to checks the links. requests https get request checks status code and if 404 adds to the
# broken link list. Also try except will add any other errors to broken link list.
def find_broken_links(url):
    for i in url:
        try:
            requestObj = requests.get(i)
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

# if the bad_links.txt file doesn't exist it is created
    if not exists('bad_links.txt'):
        g = open('bad_links.txt', 'w')
# Iterate through the list and write link to file
    for i in broken_links:
        g = open('bad_links.txt', 'a')
        g.write(i)
        g.write(date)
        g.write('\n')
        g.close()
    f.close()
# Returns either no bad links or a list of the bad links for the webhook
    if not broken_links:
        resp = 'No Bad Links!'
    else:
        resp ='Bad Links: <br>' + '\n'.join([i for i in broken_links])

    return  resp

# Defines the function for the webhook. One value output and repeats every 6 hours.
def post_ifttt_webhook(event, value1):
    data1 = {'value1': value1}
    ifttt_event_url = IFTTT_url.format(event)
    requests.post(ifttt_event_url, data1)
    time.sleep(21600)

# Inits the link file variable and reads file to list
link_file = 'Links.txt'
new_links = []
with open(link_file, 'r') as f:
    new_links = f.read().splitlines()

# Main function
while True:
    post_ifttt_webhook('Link_Check', find_broken_links(new_links))
