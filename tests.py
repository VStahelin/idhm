from idhm.api.GetCasosCovid19 import pegaCasosCovid

# municipio = "São Pedro de Alcântara"
municipio = "São José"
# municipio = "asdasdasd"
uf = "SC"

json = pegaCasosCovid(municipio, uf)
print(json)