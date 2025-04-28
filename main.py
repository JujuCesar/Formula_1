# Projeto: Análise de Dados da Fórmula 1
# Autores:
# Júlio César Corrêa
# Petterson Ikaro Bento de Souza


# ----------------------------------------


# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configuração opcional para gráficos
#plt.style.use('seaborn-darkgrid')
#plt.rcParams['figure.figsize'] = (10, 6)

# Caminho para a pasta de dados
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

# Carregamento dos datasets
circuits = pd.read_csv(os.path.join(DATA_PATH, 'circuits.csv'))
constructors = pd.read_csv(os.path.join(DATA_PATH, 'constructors.csv'))
constructor_results = pd.read_csv(os.path.join(DATA_PATH, 'constructor_results.csv'))
constructor_standings = pd.read_csv(os.path.join(DATA_PATH, 'constructor_standings.csv'))
drivers = pd.read_csv(os.path.join(DATA_PATH, 'drivers.csv'))
driver_standings = pd.read_csv(os.path.join(DATA_PATH, 'driver_standings.csv'))
lap_times = pd.read_csv(os.path.join(DATA_PATH, 'lap_times.csv'))
pit_stops = pd.read_csv(os.path.join(DATA_PATH, 'pit_stops.csv'))
qualifying = pd.read_csv(os.path.join(DATA_PATH, 'qualifying.csv'))
races = pd.read_csv(os.path.join(DATA_PATH, 'races.csv'))
results = pd.read_csv(os.path.join(DATA_PATH, 'results.csv'))
seasons = pd.read_csv(os.path.join(DATA_PATH, 'seasons.csv'))
status = pd.read_csv(os.path.join(DATA_PATH, 'status.csv'))

# Exibir os 5 primeiros registros de exemplo de cada dataset (apagar depois se quiser)
#print("🏁 Races")
#print(races.head())
#print("\n🏎️ Drivers")
#print(drivers.head())

# ----------------------------------------
# PERGUNTA 1:
# Quantas corridas aconteceram por temporada desde 1981?
# ----------------------------------------

# Pegando corridas depois de 1981
racesAfter81 = races[races['year'] >= 1981]

# Agrupando as corridas por ano
corridasPorAno = racesAfter81.groupby('year')['raceId'].count()

print("Corridas desde 1981:")
print(corridasPorAno)
print("")


# ----------------------------------------
# PERGUNTA 2:
# Quais pilotos mais venceram ao longo da história?
# ----------------------------------------

# Pegando as vitórias e o nome dos piltos ganhadores
vitorias = results[results['positionOrder'] == 1]
vitorias_por_piloto = vitorias['driverId'].value_counts()

# Criando DataFrame
top_vitorias = vitorias_por_piloto.head(10).reset_index()
top_vitorias.columns = ['driverId', 'qtd_vitorias']

# Juntando com dataset de Drivers para pega o nome
top_pilotos = top_vitorias.merge(drivers, on='driverId')

# Criando colunas
top_pilotos['nome_completo'] = top_pilotos['forename'] + ' ' + top_pilotos['surname']

# Saída de dados
print("Top 10 ganhadores da história:")
print(top_pilotos[['nome_completo', 'qtd_vitorias']])

# ----------------------------------------
# PERGUNTA 3:
# Qual equipe teve mais vitórias?
# ----------------------------------------

# Pegando as vitorias das equipes
vitorias_por_equipe = vitorias['constructorId'].value_counts()

# Criando o DataFrame de vitórias
top_equipe_vitorias = vitorias_por_equipe.reset_index()
top_equipe_vitorias.columns = ['constructorId', 'qtd_vitorias']

# Juntando com os dados dos constructors para pegar o nome
top_equipes = top_equipe_vitorias.merge(constructors, on='constructorId')

# Selecionando o Top 10
top10_equipes = top_equipes.head(10)

# Criando o gráfico
plt.barh(top10_equipes['name'], top10_equipes['qtd_vitorias'], color='darkred')
plt.xlabel('Vitórias')
plt.title('Top 10 Equipes com Mais Vitórias na Fórmula 1')
plt.gca().invert_yaxis()  # Primeiro lugar no topo
plt.grid(True)
plt.show()


# ----------------------------------------
print("\n Análise concluída com sucesso!")
