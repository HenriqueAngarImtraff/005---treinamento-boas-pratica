import pandas as pd

def import_data():

    content = pd.read_csv('table.csv', header=0)
    content = rename_columns(content)
    content = format_data(content)
    return content


def rename_columns(content):

    content.rename(columns={
        'km': 'name',
        'largura': 'width',
        'altura': 'height',
        'patologia': 'defect'
    }, inplace=True)
    return content


def format_data(content):

    content['km'] = content['name'].str.split('_', expand=True)[0]
    content['km'] = content['km'].str.split('-', expand=True)[0]
    content.drop(columns=['name'], inplace=True)
    return content


