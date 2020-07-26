from idhm.dao.OpracoesSQL import getUltimoDadoCovidDaCidade, getIdhmCidade, validCidade
import json
from datetime import datetime


def getUltimoStatusCidade(cidade, uf):
    if not validCidade(cidade, uf):
        return {}

    covid = getUltimoDadoCovidDaCidade(cidade, uf)
    idhm = getIdhmCidade(cidade, uf)

    city = {}
    city['name'] = idhm[0]
    city['state'] = idhm[5]
    city['federal_region'] = idhm[7]

    city_stats = {}
    city_stats['population'] = int(covid[8])
    city_stats['idhm'] = idhm[1]
    city_stats['idhm_educational'] = idhm[4]
    city_stats['idhm_income'] = idhm[2]

    last_update = covid[0].strftime("%d/%m/%Y")
    covid_status = {}
    covid_status['last_update'] = last_update
    covid_status['last_confirmeds'] = ''  # TODO
    covid_status['total_confirmeds'] = int(covid[4])
    covid_status['last_deaths'] = ''  # TODO
    covid_status['total_death'] = int(covid[5])
    covid_status['death_rate'] = float(covid[11])

    city['city_stats'] = city_stats
    city['covid_status'] = covid_status

    return city


if __name__ == "__main__":
    getUltimoStatusCidade("sao pedro de alcantara", "sc")
