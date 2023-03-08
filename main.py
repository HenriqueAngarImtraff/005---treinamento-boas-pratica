# INSTRUÇÕES
# Separe o código em módulos em arquivos diferentes, sendo estes main, get_data e process_data
# Renomeie o código para nomes que indiquem as funcionalidades
# Insira comentários sobre as funções

from process_data import prd
from get_data import import_data


def main():
    df = import_data()
    df = prd(df)
    df.to_excel('RESUMO.xlsx')