# compõe a parte de processamento dos dados


def prd(data):
    data['area'] = calc_area(data['xi'], data['xf'], data['yi'], data['yf'])
    info = organize_info(data)

    return info


def calc_area(xi, xf, yi, yf):
    # renomeie para calc_area
    # separe essa função de modo a operação ser feita em função a parte
    # altere a função para (value*3.5)/960
    xi = (xi*3)/96
    xf = (xf*3)/96
    yi = (yi*3)/96
    yf = (yf*3)/96

    area = (xi - xf)*(yi - yf)
    return area


def organize_info(info):

    # renomeie para organize_info
    # Descomente a parte do código que foi desativada
    info.drop(columns=['width', 'height', 'xi',
              'xf', 'yi', 'yf'], inplace=True)

    info = info.groupby('defect').sum('area')
    # info = info.sort_values(by='area', ascending=False)
    return info