# LIBRERÍAS
import pandas as pd

# VARIABLES FICHEROS DE DATOS
path = "data/ContratosMenores"
extension = ".csv"

def getCompanyInfo(company, years):
    """
    DOC STRING
    La función getCompanyInfo sirve para que al recibir una lista de años y una compañia, lea el csv del 
    año indicado y devuelva un dicconario con el nº de contratos y el total facturado en esos años.
    Los parametros de esta función son: 
    Company: hay que introducir la empresa.
    Years: hay que introducir la lista de años. 
    Return: nos devuelve un diccionario con el nº de contratos y el total facturado. 
    """
    numContracts = 0
    totalEarned = 0
    fullData = []
    for year in years :
        fullData.append(pd.read_csv(path + year + extension, encoding='latin1', sep=';'))
    for data in fullData :
        # NOMBRE COLUMNA EMPRESA
        if ("CONTRATISTA" in list(data)) :
            companyColumn = "CONTRATISTA"
        elif("Contratista" in list(data)) :
            companyColumn = "Contratista"
        elif ("Tercero" in list(data)) :
            companyColumn = "Tercero"
        # NOMBRE COLUMNA IMPORTE
        if ("IMPORTE" in list(data)) :
            paymentColumn = "IMPORTE"
        elif ("Importe" in list(data)) :
            paymentColumn = "Importe"
        elif("      Importe" in list(data)) :
            paymentColumn = "      Importe"
        elif("       Importe" in list(data)) :
            paymentColumn = "       Importe"
        # CÁLCULO
        for i in range(data.shape[0]):
            if (data.iloc[i][companyColumn] == company) :
                numContracts += 1
                totalEarned += float(data.iloc[i][paymentColumn].replace(".","").replace(",",".").replace("\x80",""))
    return {"NÚMERO DE CONTRATOS" : numContracts, "TOTAL FACTURADO" : totalEarned}


def getSectionInfo(section, years):
    """
    DOC STRING:
    Esta función al recibir una sección y una lista de años, busca en el csv del año indicado, y 
    nos devuelve un diccionario con el nº de contratos y el total facturado de la sección en los años
    indicados.
    Los parámetros de esta función son:
    Section: hay que introducir la sección
    Years: hay que introducir la lista de años. 
    Return: nos devuleve un diccionario con el total facturado y el nº de contratos.
    """
    numContracts = 0
    totalEarned = 0
    fullData = []
    for year in years :
        fullData.append(pd.read_csv(path + year + extension, encoding='latin1', sep=';'))
    for data in fullData :
        # NOMBRE COLUMNA SECCIÓN
        if ("SECCION " in list(data)):
            sectionColumn = "SECCION "
        elif("Descripción" in list(data)):
            sectionColumn = "Descripción"
        # NOMBRE COLUMNA IMPORTE
        if ("IMPORTE" in list(data)):
            paymentColumn = "IMPORTE"
        elif ("Importe" in list(data)):
            paymentColumn = "Importe"
        elif("      Importe" in list(data)) :
            paymentColumn = "      Importe"
        elif("       Importe" in list(data)) :
            paymentColumn = "       Importe"
        # CÁLCULO
        for i in range(data.shape[0]):
            if (data.iloc[i][sectionColumn] == section) :
                numContracts += 1
                totalEarned += float(data.iloc[i][paymentColumn].replace(".","").replace(",",".").replace("\x80",""))
    return {"NÚMERO DE CONTRATOS" : numContracts, "TOTAL FACTURADO" : totalEarned}