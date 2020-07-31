import unidecode

from idhm_api.dao.OpracoesSQL import getCitysAndUf, insertCityInCidades2

lista = getCitysAndUf()

for row in lista:
    cidade = (row[0], row[1], str(unidecode.unidecode(row[0])))
    print(cidade)
    insertCityInCidades2(cidade)
