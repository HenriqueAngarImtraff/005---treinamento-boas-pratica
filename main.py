# INSTRUÇÕES
# Separe o código em módulos em arquivos diferentes, sendo estes main, get_data e process_data
# Renomeie o código para nomes que indiquem as funcionalidades
# Insira comentários sobre as funções

import pandas as pd
import process_data
import get_data as gd

def main():
    df = gd.import_data()
    df = process_data(df)
    df.to_excel('RESUMO.xlsx')
