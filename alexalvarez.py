
import pandas as pd
import matplotlib.pyplot as plt 
path = "ContratosMenores"
extension = ".csv"

#FUNCIÓN 3
def EmpresaSeccionAños(company,section,years):
    """
    FUNCIÓN QUE LEE CSV DE CONTRATOS MENORES.
    LEERÁ EL CSV CORRESPONDIENTE AL AÑO QUE SE INTRODUZCA COMO PARÁMETRO O LOS CSV CORRESPONDIENTES SI SE TRATA DE UNA LISTA.
    A SU VEZ, REQUIERE QUE SE INTRODUZCA EL NOMBRE DE LA EMPRESA SOBRE A QUE SE QUIERE OBTENER LA INFORMCIÓN ASÍ COMO LA SECCIÓN.
    PARÁMETROS:
        company: nombre de la empresa 
        sección: sección de la cual se quiere obtener el total facturado
        years: lista de años sobre los que se quiera obtener la información
    DEVUELVE : Esta función devuelve un diccionario con el número de contratos y el total facturado por la empresa solicitada a la sección en los años introducidos por el usuario.
    """
    numberContracts = 0
    totalEarned = 0
    fullData = []
    for year in years:
        fullData.append(pd.read_csv(path + year + extension, encoding="latin1", sep=";"))
    for data in fullData:
        #NOMBRE DE LA COLUMNA
        if ("CONTRATISTA" in list(data)):
            companyColumn = "CONTRATISTA"
        elif("Contratista" in list(data)):
            companyColumn = "Contratista"
        elif ("Tercero" in list(data)):
            companyColumn = "Tercero"
        # NOMBRE COLUMNA SECCIÓN
        if ("SECCION" in list(data)):
            sectionColumn = "SECCION"
        elif ("Descripción" in list(data)):
            sectionColumn = "Descripción"
        # NOMBRE DE LA COLUMNA DE IMPORTE
        if ("IMPORTE" in list(data)):
            paymentColumn = "IMPORTE"
        elif("Importe" in list(data)):
            paymentColumn = "Importe"
        elif ("      Importe" in list(data)):
            paymentColumn = "      Importe"
        elif ("       Importe" in list(data)): #QUE ES LO DE LIST DATA? Y LO DE ...COLUMN?
            paymentColumn = "       Importe"  
        #CÁLCULO
        for i in range (data.shape[0]): 
            if (data.iloc[i][companyColumn] == company and data.iloc[i][sectionColumn] == section):
                numberContracts += 1
                totalEarned += float(data.iloc[i][paymentColumn].replace(".", "").replace(",", "").replace("x80",""))
    return {"NÚMERO DE CONTRATOS":numberContracts, "TOTAL FACTURADO": totalEarned}

#print(EmpresaSeccionAños("ANGAVA S A .", "PRESIDENCIA DEL PLENO", ["2015", "2016", "2017", "2018", "2019"]))


#FUNCIÓN1 DIANA (para usar más abajo)
def getCompanyInfo(company, years):
    numContracts = 0
    totalEarned = 0
    fullData = []
    for year in years:
        fullData.append(pd.read_csv(path + year + extension, encoding="latin1", sep = ";"))
    for data in fullData:
    #NOMBRE DE LA COLUMN EMPRESA
        if ("CONTRATISTA" in list(data)):
            companyColumn = "CONTRATISTA"
        elif ("Contratista" in list(data)):
            companyColumn = "Contratista"
        elif ("Tercero" in list(data)):
            companyColumn = "Tercero"
    #NOMBRE DE LA COLUMNA CORRESPONDIENTE AL IMPORTE
        if ("IMPORTE" in list(data)):
            paymentColumn = "IMPORTE"
        elif("Importe" in list(data)):
            paymentColumn = "Importe"
        elif ("      Importe" in list(data)):
            paymentColumn = "      Importe"
        elif ("       Importe" in list(data)):
            paymentColumn = "       Importe"
    #CÁLCULO EN SÍ
        for i in range (data.shape[0]):
            if (data.iloc[i][companyColumn] == company):
                numContracts += 1
                totalEarned += float(data.iloc[i][paymentColumn].replace(".","").replace(",",".").replace("\x80", ""))
    return {"NÚMERO DE CONTRATOS": numContracts, "TOTAL FACTURADO": totalEarned}

#FUNCION 4
def TopEarnings(n,years):
    """
    FUNCIÓN QUE CALCULA LAS EMPRESAS SOLICITADAS QUE MÁS HAN FACTURADO EN "X" TIEMPO, ORDENADAS DE MAYOR A MENOR Y REPRESENTADAS EN UN GRÁFICO
    PARÁMETROS: Son necesarios 2 parámetros
        n : corresponde al numero de empresas de las cuales se quiere mostrar la información
        years : años de los cuales se quiere mostrar la información
    DEVUELVE: La función devuelve una lista con diccionarios en los que se podrán encontrar las n empresas, con sus correspondientes nombres, ordenadas de mayor a menor facturación así como un gráfico que ilustra dichos datos.
    """
    fullData = []
    for year in years:
        fullData.append(pd.read_csv(path + year + extension, encoding = "latin1", sep =";"))
    for data in fullData:
        #NOMBRE DE LA COLUMNA EMPRESA
        if ("CONTRATISTA" in list(data)):
            companyColumn = "CONTRATISTA"
        elif ( "Contratista" in list(data)):
            companyColumn = "Contratista"
        elif ("Tercero" in list(data)):
            companyColumn = "Tercero"
        companies = []
        companyInfo = []
        for i in range(data.shape[0]):
            if (data.iloc[i][companyColumn] not in companies):
                companies.append(data.iloc[i][companyColumn])
                companyInfo.append({"EMPRESA": data.iloc[i][companyColumn], "TOTAL FACTURADO" : getCompanyInfo(data.iloc[i][companyColumn],years)["TOTAL FACTURADO"]})
    companyInfo = sorted(companyInfo, key=lambda k: k["TOTAL FACTURADO"], reverse = True)
    info = companyInfo[:n]
    valores = []
    numeroEmpresas = list(range(n))
    for i in range(len(info)):
        valores.append(info[i]["TOTAL FACTURADO"])
    #print(valores)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(numeroEmpresas,valores)
    plt.show()
    return info
 

#para comprobar que la funcion 1 funciona, y si funciona
#print(getCompanyInfo("SERPROSA COMERCIALIZADORA S A", ["2015", "2016", "2017", "2018", "2019"]))
print(TopEarnings(5, ["2019"]))
# devuelve lo siguiente:
# [{'EMPRESA': 'EXTERION MEDIA SPAIN S A', 'TOTAL FACTURADO': 118425.10999999999}, {'EMPRESA': 'DISTRIBUIDORA DE MATERIAL DE OFICINA S A', 'TOTAL FACTURADO': 93729.16}, {'EMPRESA': 'TRITOMA S.L.', 'TOTAL FACTURADO': 69905.09}, {'EMPRESA': 'LUCES Y SOMBRAS SOCIEDAD COOPERATIVA MADRILEÑA', 'TOTAL FACTURADO': 62342.61000000001}, {'EMPRESA': 'STAFF RESOURCE S.L.', 'TOTAL FACTURADO': 57355.939999999995}]
