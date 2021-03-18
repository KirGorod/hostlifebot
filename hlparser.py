import requests
from bs4 import BeautifulSoup
from constants import *


def close_tickets():
    with requests.Session() as s:
        login_data = {
            'login': USERNAME,
            'pass': PASSWORD
        }
        try:
            print("Try post")
            r = s.post(URL, data=login_data)
            print("Try get")
            r = s.get('https://order.hostlife.net/je4KfGJ0.php?do=tickets')
            print("Logged in")
        except:
            print(BaseException)

        soup = BeautifulSoup(r.content, 'html.parser')
        items = (soup.find_all('a'))

        links = []
        for item in items:
            links.append(item.get('href'))

        pattern = "?do=tickets&sub=view&id"
        for i, link in enumerate(links):
            try:
                if pattern in link:
                    print(f"Oppening link {i}...")
                    s.get(HOST + link)
            except:
                pass



if __name__ == "__main__":
    close_tickets()



