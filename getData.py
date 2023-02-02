import pandas as pd


def import_data():
    """Controls data import

    Returns:
        A correct dataframe object
    """
    content = pd.read_csv('table.csv', sep=';', header=0)
    content = rename_data(content)
    content = format_data(content)
    return content


def rename_data(content):
    """Correct columns name

    Arg:
        content: dataframe object

    Returns:
        data frame object
    """
    content.rename(columns={
        'km': 'name',
        'largura': 'width',
        'altura': 'height',
        'patologia': 'defect'
    }, inplace=True)
    return content


def format_data(content):
    """Format name to km from content

    Arg:
        content: dataframe object

    Returns:
        data frame object
    """
    content['km'] = content['name'].str.split('_', expand=True)[0]
    content['km'] = content['km'].str.split('-', expand=True)[0]
    content.drop(columns=['name'], inplace=True)
    return content
