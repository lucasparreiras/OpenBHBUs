# A API OpenBHBus

O OpenBHBus é uma API RESTFul que fornece dados sobre as linhas de ônibus da região metropolitana de Belo Horizonte. OpenBHBus está disponível no endereço https://openbhbus.herokuapp.com e possui código aberto sob licença GNU GPL 3.0.
O formato de retorno dos dados respeita a estrutura RESTFul e é entregue no formato JSON.
O intuito da API é fornecer dados sobre os modais de transporte de Belo Horizonte-MG, para que aplicativos possam consumir estes dados e fornecer soluções para a sociedade.

## Funcionalidades

Estão disponíveis na OpenBHBus as seguintes funcionalidades:

* Linhas
  * BuscarTarifa
  * BuscarHorarioDiaUtil
  * BuscarHorarioSabado
  * BuscarHorarioDomingoFeriado
  * BuscarHorarioDiaAtipico
  * BuscarItinerario

### Linhas

A categoria Linhas possibilita a consultas pelas linhas de ônibus da cidade de Belo Horizonte-MG, possibilitando o retorno de informações como: tarifas, horários e itinerário.
Nesta categoria existem os seguintes métodos de consulta disponíveis: BuscarTarifas, BuscarHorarioDiaUtil, BuscarHorarioSabado, BuscarHorarioDomingoFeriado, BuscarHorarioDiaAtipico e BuscarItinerario.

#### BuscarTarifa
	
Realiza uma busca de tarifa da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.

	Parâmetro [string] - Código da Linha
	
	GET linhas/BuscarTarifa
	GET linhas/BuscarTarifa/<código linha>
	
```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarTarifa/101')
print(r.json())
```

#### BuscarHorarioDiaUtil
Realiza uma busca de quadro de horários para dias úteis da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.
	
	Parâmetro [string] - Código da Linha
	GET linhas/BuscarHorarioDiaUtil
	GET linhas/BuscarHorarioDiaUtil/<código linha>
	Ex.:

```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarHorarioDiaUtil/101')
print(r.json())
```

#### BuscarHorarioSabado

Realiza uma busca de quadro de horários para sábados da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.

	Parâmetro [string] - Código da Linha
	GET linhas/BuscarHorarioSabado
	GET linhas/BuscarHorarioSabado/<código linha>
	Ex.:

```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarHorarioSabado/101')
print(r.json())
```

#### BuscarHorarioDomingoFeriado

Realiza uma busca de quadro de horários para domingos e feriados da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.

	Parâmetro [string] - Código da Linha
	GET linhas/BuscarHorarioDomingoFeriado
	GET linhas/BuscarHorarioDomingoFeriado/<código linha>
	Ex.:

```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarHorarioDomingoFeriado/101')
print(r.json())
```

#### BuscarHorarioDiaAtipico
Realiza uma busca de quadro de horários para dias atípicos da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.
	
	Parâmetro [string] - Código da Linha
	GET linhas/BuscarHorarioDiaAtipico
	GET linhas/BuscarHorarioDiaAtipico/<código linha>
	Ex.:

```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarHorarioDiaAtipico/101')
print(r.json())
```

#### BuscarItinerario

Realiza uma busca do itinerário da linha do sistema com base no parâmetro informado. Caso nenhum parâmetro seja informado, serão retornados dados de todas as linhas do sistema.

	Parâmetro [string] - Código da Linha
	GET linhas/BuscarItinerario
	GET linhas/BuscarItinerario/<código linha>
	Ex.:

```python
import requests

r = requests.get('https://openbhbus.herokuapp.com/linhas/BuscarItinerario/101')
print(r.json())
```

## Tecnologia

API foi desenvolvida utilizando a linguagem Python (versão 3.5.2) e os dados são armazenados em banco de dados MongoDB.
Foram utilizadas as bibliotecas Python Flask e PyMongo.
Flask é um micro-framework desenvolvido em Python e baseado em WerkZeug. PyMongo é uma distribuição Python que contém ferramentas para trabalhar com o MongoDB.
O OpenBHBus está hospedado no Heroku, uma Plataforma como Serviço (PaaS) baseada em contêiner.

