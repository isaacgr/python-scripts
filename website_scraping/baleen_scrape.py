# Scrape http://baleen.districtdatalabs.com/
# Put content into a csv file
import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    data = []

    feeds_page = "http://baleen.districtdatalabs.com/"
    request = requests.get(feeds_page)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    topics = soup.find_all('a', {'class': 'list-group-item'}, href=True)
    tables = soup.find_all('table', {'class': 'table'})

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            data.append([element for element in cols if element])
            data.append(topics[tables.index(table)]['href'])

    for feed in data:
        for element in feed:
            if '\n' in element:
                feed.remove(element)
        if isinstance(feed, list):
            feed.append(data[data.index(feed)+1])


    for topic in data:
        if isinstance(topic, unicode):
            data.remove(topic)

    new_data = []
    for row in data:
        title, url, topic = row
        for url in url.split(','):
            new_data.append([title, url, topic])

    result = pd.DataFrame(new_data, columns=['Title', 'URL', 'Topic'])

    write_excel(result)
    write_csv(result)


def write_excel(result):
    writer = pd.ExcelWriter('feeds.xlsx')
    result.to_excel(writer, 'Feeds')
    writer.save()


def write_csv(result):
    with open('feeds.csv', 'w') as f:
        result.to_csv(f, sep=',', encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
