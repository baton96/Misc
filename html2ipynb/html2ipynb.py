import json

from bs4 import BeautifulSoup

dictionary = {'nbformat': 4, 'nbformat_minor': 1, 'cells': [], 'metadata': {}}

with open('file.html') as inputFile:
    soup = BeautifulSoup(inputFile.read(), 'html.parser')

for div in soup.findAll('div'):
    if 'class' in div.attrs.keys():
        for _class in div.attrs['class']:
            if _class == 'input_area':
                cell = {'metadata': {}, 'outputs': [], 'source': [div.get_text().strip()],
                        'execution_count': None, 'cell_type': 'code'}
                dictionary['cells'] += [cell]
            elif _class == 'text_cell_render':
                cell = {'metadata': {}, 'source': [div.decode_contents().strip()], 'cell_type': 'markdown'}
                dictionary['cells'] += [cell]

with open('file.ipynb', 'w') as outputFile:
    outputFile.write(json.dumps(dictionary))
