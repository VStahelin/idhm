import mysql.connector

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

