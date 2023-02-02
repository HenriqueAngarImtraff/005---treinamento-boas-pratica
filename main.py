import getData
import processData


def main():
    """Main application function

    Returns:
        dowload a csv file of result
    """
    data = getData.import_data()
    info = processData.process(data)
    info.to_excel('RESUMO.xlsx')
