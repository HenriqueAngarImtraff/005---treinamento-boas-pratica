import pandas as pd


# Essa parte compõe importação
def imp():
    # renomeie para import_data
    content = pd.read_csv('table.csv', sep=';', header=0)
    content = ren(content)
    content = fmt(content)
    return content


def ren(content):
    # renomeie para rename_columns
    content.rename(columns={
        'km': 'name',
        'largura': 'width',
        'altura': 'height',
        'patologia': 'defect'
    }, inplace=True)
    return content


def fmt(content):
    # renomeie para format_data
    content['km'] = content['name'].str.split('_', expand=True)[0]
    content['km'] = content['km'].str.split('-', expand=True)[0]
    content.drop(columns=['name'], inplace=True)
    return content
