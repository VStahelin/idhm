import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="idhms"
)


def insertEstado(ibge, estado, uf, regiao, sntaxe):
    mycursor = mydb.cursor()
    sql = "INSERT INTO estados (idEstado, nome, uf, regiao, sintaxe) VALUES (%s, %s, %s, %s, %s);"
    val = (ibge, estado, uf, regiao, sntaxe)
    mycursor.execute(sql, val)
    mydb.commit()


def instCidade(idEstado, cidade, idhm, idhmRenda, idhmLongv, idhmEdu):
    mycursor = mydb.cursor()
    sql = "INSERT INTO cidades (idEstado, nome, idhm, idhmRenda, idhmLongv, idhmEdu) VALUES (%s, %s, %s, %s, %s, %s);"
    val = (idEstado, cidade, idhm, idhmRenda, idhmLongv, idhmEdu)
    mycursor.execute(sql, val)
    mydb.commit()


def getIdEstadoFromUf(uf):
    mycursor = mydb.cursor()
    mycursor.execute("select idEstado from estados where uf = '{}';".format(uf))
    for id in mycursor:
        return id[0]


def getUltimoDadoCovidDaCidade(cidade, uf):
    sql = 'SELECT * FROM casofullcovid where place_type = "city" and city="{}" and ' \
          'state="{}" and is_last = "true";'.format(cidade, uf)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()[0]


def getGraficoCovidPorCidadePorData(cidade, uf, data_inicial, data_final):
    sql = 'SELECT * FROM casofullcovid where place_type = "city" and city="{}" and state="{}" and date BETWEEN "{}" ' \
          'AND "{}";'.format(cidade, uf, data_inicial, data_final)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()[0]


def getGraficoCovidPorCidadePorTimestamp(cidade, uf, ts_inicial, ts_final):
    data_inicial = datetime.fromtimestamp(ts_inicial)
    data_final = datetime.fromtimestamp(ts_final)
    return getGraficoCovidPorCidadePorData(cidade, uf, data_inicial, data_final)


def getGraficoCovidPorCidadeTodoTempo(cidade, uf):
    sql = 'SELECT * FROM casofullcovid where place_type = "city" and city="{}" and ' \
          'state="{}" order by date asc;'.format(cidade, uf)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()


def getIdhmCidade(cidade, uf):
    sql = 'Select cidades.nome, cidades.idhm, cidades.idhmRenda, cidades.idhmLongv, cidades.idhmEdu, estados.nome, ' \
          'estados.uf, estados.regiao FROM cidades join estados on cidades.idEstado = estados.idEstado where ' \
          'cidades.nome="{}" and uf="{}";'.format(cidade, uf)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()[0]


def validUf(uf):
    sql = 'SELECT uf FROM idhms.estados where uf = "{}";'.format(uf)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    for i in mycursor:
        return True
    return False


def validCidade(cidade, uf):
    if validUf(uf):
        sql = 'SELECT cidades.nome FROM cidades join estados on cidades.idEstado = estados.idEstado where cidades.nome = "{}";'.format(
            cidade)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        for i in mycursor:
            return True
        return False
    else:
        return False


def getCitysAndUf():
    sql = 'SELECT city, state FROM casofullcovid where place_type = "city" and is_last = "true" order by city asc;'
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()


def insertCityInCidades2(lista):
    sql = 'INSERT INTO cidades2 (city, state, city_normal) VALUES ("{}", "{}", "{}")'.format(lista[0],lista[1],lista[2])
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()


if __name__ == "__main__":
    for row in getGraficoCovidPorCidadeTodoTempo("sao pedro de alcantara", "sc"):
        print(row)
