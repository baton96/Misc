import os

import pandas as pd
from bs4 import BeautifulSoup
from requests import get

headers = {
    'User-Agent': 'Chrome/50.0.2661.102 Safari/537.36'
}
nPages = 1


def fetch_metadata_freepik():
    if not os.path.exists('freepik'):
        os.makedirs('freepik')

    metadata = open('freepik/metadata.csv', 'w')
    metadata.write('URL,Likes,Downloads,Keyword,Title\n')

    for i in range(1, nPages + 1):
        page = get(f'https://www.freepik.com/search?type=icon&page={i}', headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        figures = soup.find_all('figure')
        for figure in figures:
            image = figure['data-image'].split('/')[-1]
            likes = figure['data-likes']
            downloads = figure['data-downloads']
            keyword = figure['data-first-keyword']
            title = figure.find('p', class_='title').text

            metadata.write(f'{image},{likes},{downloads},{keyword},{title}\n')
    metadata.close()


def fetch_imgs_freepik():
    if not os.path.exists('freepik/img'):
        os.makedirs('freepik/img')
    metadata = pd.read_csv('freepik/metadata.csv')
    for url in metadata['URL']:
        with open(f'freepik/img/{url}', 'wb') as f:
            f.write(get(f'https://image.freepik.com/free-icon/{url}').content)


def fetch_metadata_flaticon():
    if not os.path.exists('flaticon'):
        os.makedirs('flaticon')

    metadata = open('flaticon/metadata.csv', 'w')
    metadata.write('URL,Downloads,Name,Keyword,Category_id,Category_name\n')

    for i in range(1, nPages + 1):
        page = get(
            f'https://www.flaticon.com/search/{i}?search-type=icons&license=selection&color=1&stroke=1',
            # f'https://www.flaticon.com/search/{i}?search-type=icons&license=selection&color=1&stroke=2',
            headers=headers
        )
        soup = BeautifulSoup(page.content, 'html.parser')
        icons = soup.find_all('li', class_='icon')
        for icon in icons:
            try:
                img = '/'.join(icon['data-icon_src'].split('/')[5:])
                img = img.split('.')[0] + '.png'
                downloads = icon['data-downloads']
                name = icon['data-name']
                keyword = icon['data-keyword']
                category_id = icon['data-category_id']
                category_name = icon['data-category_name']
                metadata.write(f'{img},{downloads},{name},{keyword},{category_id},{category_name}\n')
            except:
                break
    metadata.close()


def fetch_imgs_flaticon():
    if not os.path.exists('flaticon/img'):
        os.makedirs('flaticon/img')
    metadata = pd.read_csv('flaticon/metadata.csv')
    for url in metadata['URL']:
        filename = '_'.join(url.split('/'))
        with open(f'flaticon/img/{filename}', 'wb') as f:
            f.write(get(f'https://image.flaticon.com/icons/png/512/{url}').content)
