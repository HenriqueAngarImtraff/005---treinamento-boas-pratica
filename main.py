

# INSTRUÇÕES
# Separe o código em módulos em arquivos diferentes, sendo estes main, get_data e process_data
# Renomeie o código para nomes que indiquem as funcionalidades
# Insira comentários sobre as funções

import get_data
import process_data


def main():
    df = get_data.imp()
    df = process_data.prd(df)
    df.to_excel('RESUMO.xlsx')


# compõe a parte de processamento dos dados
