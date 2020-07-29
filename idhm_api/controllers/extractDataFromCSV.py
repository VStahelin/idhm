import csv
from idhm_api.dao.OpracoesSQL import *


def extaiCidades():
    with open('../planilhas/cidades.csv', newline='') as arquivo:
        reader = csv.DictReader(arquivo, delimiter=',')
        fist = True
        for row in reader:
            if fist:
                fist = False
                continue

            valores = row.get('sep=;').split(";")
            nome = valores[1][0:len(valores[1]) - 4]
            uf = valores[1][len(valores[1]) - 3:len(valores[1]) - 1]
            idEstado = getIdEstadoFromUf(uf)
            instCidade(str(idEstado), nome, valores[2], valores[3], valores[4], valores[5])


def extraiEstados():
    with open('../planilhas/estados.csv', 'r') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        fist = True
        for row in reader:
            if fist:
                fist = False
                continue
            insertEstado(row[0], row[1], row[2], row[3], row[5])


if __name__ == '__main__':
    extraiEstados()
    extaiCidades()
