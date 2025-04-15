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
print("🏁 Races")
print(races.head())
print("\n🏎️ Drivers")
print(drivers.head())

# ----------------------------------------
# PERGUNTA 1:
# Ex: Quantas corridas aconteceram por temporada?
# ----------------------------------------

# Seu código aqui...


# ----------------------------------------
# PERGUNTA 2:
# Ex: Quais pilotos mais venceram ao longo da história?
# ----------------------------------------

# Seu código aqui...


# Continue com as perguntas 3 a 10 seguindo esse mesmo padrão.
# Você pode criar gráficos com matplotlib para cada uma também:
# plt.plot(...), plt.bar(...), etc.

# ----------------------------------------
# FIM DO SCRIPT
# ----------------------------------------
print("\n Análise concluída com sucesso!")
