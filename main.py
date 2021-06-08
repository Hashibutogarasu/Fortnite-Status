import sys
import urllib.request
import bs4

import time

def main_sub(url="https://status.epicgames.com/",search_text='Fortnite           Under Maintenance'):

    html = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    title = soup.select('.lxl-inCateList ul li a dl dt')
    price = soup.find_all("dd", class_="l-price")

    texts = (soup.text.replace('\n',''))

    if (search_text in texts) == True:
        print("Fortnite is offline.")
    else:
        print("Fortnite is online.")

def main():
    while True:
        main_sub()
        time.sleep(60*60*24)

if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()