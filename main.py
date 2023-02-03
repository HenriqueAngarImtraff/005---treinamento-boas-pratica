

# INSTRUÇÕES
# Renomeie o código para nomes que indiquem as funcionalidades
# Insira comentários sobre as funções

import pandas as pd


def main():
    df = imp()
    df = prd(df)
    df.to_excel('RESUMO.xlsx')


# compõe a parte de processamento dos dados


def prd(data):
    data['area'] = caca(data['xi'], data['xf'], data['yi'], data['yf'])
    info = orgi(data)

    return info


def caca(xi, xf, yi, yf):
    # renomeie para calc_area
    # separe essa função de modo a operação ser feita em função a parte
    # altere a função para (value*3.5)/960
    xi = (xi*3)/96
    xf = (xf*3)/96
    yi = (yi*3)/96
    yf = (yf*3)/96

    area = (xi - xf)*(yi - yf)
    return area


def orgi(info):

    # renomeie para organize_info
    # Descomente a parte do código que foi desativada
    info.drop(columns=['width', 'height', 'xi',
              'xf', 'yi', 'yf'], inplace=True)

    info = info.groupby('defect').sum('area')
    # info = info.sort_values(by='area', ascending=False)
    return info
