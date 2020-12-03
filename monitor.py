from discord import send_hook
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime
import time

pid = ['6795199', '6795151', '8448262']

proxy_list = []


def privateProxies():
    with open('proxies.txt') as f:
      file_content = f.read()
    file_rows = file_content.split('\n')
    for i in range(len(file_rows)):
      if ':' in file_rows[i]:
        tmp = file_rows[i]
        tmp = tmp.split(':')
        proxies = {'http': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/',
                     'https': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/'}
        proxy_list.append(proxies)
        f.close()


privateProxies()


while True:
  for i in range(len(pid)):
    proxy = random.choice(proxy_list)
    url = "https://www.argos.co.uk/product/{}".format(pid[i])
    try:
      response = requests.get(url, proxies=proxy)
      soup = BeautifulSoup(response.text,'html.parser')
      try:
        subcopy = soup.find('p', attrs={'id': 'subCopy'}).get_text()
        if subcopy == 'We\'re working hard to get more stock.':
          print('[{}] OOS'.format(str(datetime.now())))
        else:
          print('[{}] in stock'.format(str(datetime.now())))
          send_hook(url)
      except:
        print('[{}] in stock'.format(str(datetime.now())))
        send_hook(url)
    except ConnectionError:
      print(ConnectionError)
    except TimeoutError:
      print(TimeoutError)
  time.sleep(random.randint(10,25))
