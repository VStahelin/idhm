from idhm_api.dao.OpracoesSQL import getUltimoDadoCovidDaCidade, getIdhmCidade, validCidade, \
    getGraficoCovidPorCidadeTodoTempo, getStatusGeralBrasilDB


def getUltimoStatusCidade(cidade, uf):
    if not validCidade(cidade, uf):
        return {}

    covid = getUltimoDadoCovidDaCidade(cidade, uf)
    idhm = getIdhmCidade(cidade, uf)

    city = {}
    city['name'] = idhm[0]
    city['state'] = idhm[5]
    city['federal_region'] = idhm[7]
    city['uf'] = idhm[6]

    city_stats = {}
    city_stats['population'] = int(covid[8])
    city_stats['idhm'] = idhm[1]
    city_stats['idhm_educational'] = idhm[4]
    city_stats['idhm_income'] = idhm[2]

    covid_status = {}
    covid_status['last_update'] = covid[0].strftime("%d/%m/%Y")
    covid_status['last_confirmeds'] = ''  # TODO
    covid_status['total_confirmeds'] = int(covid[4])
    covid_status['last_deaths'] = ''  # TODO
    covid_status['total_death'] = int(covid[5])
    covid_status['death_rate'] = float(covid[11])

    city['city_stats'] = city_stats
    city['covid_status'] = covid_status

    return city


def getGraficoStatusCidade(cidade, uf):
    if not validCidade(cidade, uf):
        return {}

    idhm = getIdhmCidade(cidade, uf)
    city = {}
    city['name'] = idhm[0]
    city['state'] = idhm[5]
    city['federal_region'] = idhm[7]
    city['uf'] = idhm[6]

    values = []
    for row in getGraficoCovidPorCidadeTodoTempo(cidade, uf):
        covid_status = {}
        covid_status['date'] = row[0].strftime("%d/%m/%Y")
        covid_status['last_confirmeds'] = ''  # TODO
        covid_status['total_confirmeds'] = int(row[4])
        covid_status['last_deaths'] = ''  # TODO
        covid_status['total_death'] = int(row[5])
        covid_status['death_rate'] = float(row[11])
        values.append(covid_status)

    city['values'] = values

    return city


def getStatusGeralEstados():
    dados = getStatusGeralBrasilDB()

    estados = []
    for row in dados:
        estado = {}
        estado['date'] = row[0].strftime("%d/%m/%Y")
        estado['name'] = row[2]
        estado['uf'] = row[1]
        estado['population'] = row[5]
        estado['total_confirmeds'] = int(row[3])
        estado['last_confirmeds'] = ''  # TODO
        estado['last_deaths'] = ''  # TODO
        estado['total_death'] = int(row[4])
        estado['death_rate'] = float(row[6])
        estados.append(estado)

    return estados


def getStatusGeralEstadosIndexadoPorNome():
    dados = getStatusGeralBrasilDB()

    # estados = []
    estados = {}
    for row in dados:
        vars = {}
        vars['uf'] = row[1]
        vars['date'] = row[0].strftime("%d/%m/%Y")
        vars['population'] = row[5]
        vars['total_confirmeds'] = int(row[3])
        vars['last_confirmeds'] = ''  # TODO
        vars['last_deaths'] = ''  # TODO
        vars['total_death'] = int(row[4])
        vars['death_rate'] = float(row[6])
        estados[row[2]] = vars

    return estados


def getStatusGeralConfirmadosBrasilGeoChart():
    dados = getStatusGeralBrasilDB()

    chart = {}
    chart['column1'] = 'Country'
    chart['column2'] = 'Casos confirmados'
    chart['header1'] = 'Brazil'
    chart['header2'] = 0

    estados = []
    for row in dados:
        value = {}
        value['name'] = str(row[2])
        value['total_confirmeds'] = int(row[3])
        estados.append(value)
    chart['estados'] = estados
    return chart


if __name__ == "__main__":
    # print(getGraficoStatusCidade("sao pedro de alcantara", "sc"))
    # print(getStatusGeralBrasil())
    # a = {'estados': getStatusGeralBrasil()}
    print(getStatusGeralEstadosIndexadoPorNome())
