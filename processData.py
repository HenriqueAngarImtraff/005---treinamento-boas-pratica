
def process(data):
    """Controls data process

    Returns:
        A final dataframe object
    """

    data['area'] = calc_area(data['xi'], data['xf'], data['yi'], data['yf'])
    info = organize_info(data)

    return info


def calc_area(xi, xf, yi, yf):
    """Calc area in meters of px labels

    Args:
        xi: initial x value px
        xf: end x value px
        yi: initial y value px
        yf: end y value px

    Returns:
        A float of area in meters
    """
    xi = convert_to_meters(xi)
    xf = convert_to_meters(xf)
    yi = convert_to_meters(yi)
    yf = convert_to_meters(yf)

    area = (xi - xf)*(yi - yf)
    return area


def convert_to_meters(value):
    """Convert the px value to meters

    Arg:
        value: coordinate value in px int

    Returns:
        return a float
    """
    value = (value*3.5)/960
    return value


def organize_info(info):
    """Organize data information for dowload

    Arg:
      info: dataframe object

    Returns:
        final data frame object
    """
    info.drop(columns=['width', 'height', 'xi',
              'xf', 'yi', 'yf'], inplace=True)

    info = info.groupby('defect').sum('area')
    info = info.sort_values(by='area', ascending=False)
    return info
