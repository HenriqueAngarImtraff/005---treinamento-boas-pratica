import get_data as gd
import process_data as prd

import pandas as pd


def main():
    df = gd.import_data()
    df = prd.process_data(df)
    df.to_excel('RESUMO.xlsx')


main()
