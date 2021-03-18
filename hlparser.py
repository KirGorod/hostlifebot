import requests
from bs4 import BeautifulSoup
from constants import *
import time


def close_tickets():
    with requests.Session() as s:
        login_data = {
            'login': USERNAME,
            'pass': PASSWORD
        }
        try:
            r = s.post(URL, data=login_data)
            r = s.get('https://order.hostlife.net/je4KfGJ0.php?do=tickets')
        except:
            pass

        #clear tickets x times
        for x in range(0, 4):

            #main logic
            soup = BeautifulSoup(r.content, 'html.parser')
            items = (soup.find_all('a'))
            pattern = "?do=tickets&sub=view&id"

            #get links collection
            links = []
            for item in items:
                links.append(item.get('href'))

            #close tickets that are in collection
            for i, link in enumerate(links):
                try:
                    if pattern in link:
                        print(f"Oppening link {i}...")
                        s.get(HOST + link)
                except:
                    pass
            time.sleep(3)
            print(f"Iteration #{x}")



if __name__ == "__main__":
    close_tickets()