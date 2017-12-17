# Scrape http://baleen.districtdatalabs.com/
# Put content into a csv file
import requests
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

def main():
    data = []

    feeds_page = "http://baleen.districtdatalabs.com/"
    r = requests.get(feeds_page)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    topics = soup.find_all('a', {'class': 'list-group-item'}, href=True)
    tables = soup.find_all('table', {'class': 'table'})

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            data.append([element for element in cols if element])

    for feeds in data:
        for feed in feeds:
            if '\n' in feed:
                feeds.remove(feed)

    new_data = []
    for row in data:
        x, y = row
        for y in y.split(','):
            new_data.append([x,y])

    result = pd.DataFrame(new_data, columns=['Title', 'URL'])

    write_excel(result)


def write_excel(result):
    writer = pd.ExcelWriter('feeds.xlsx')
    result.to_excel(writer, 'Feeds')
    writer.save()


if __name__=='__main__':
    main()
