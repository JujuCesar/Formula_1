# Projeto: Análise de Dados da Fórmula 1
# Autores:
# Júlio César Corrêa - GES - N° 404 - C11
# Petterson Ikaro Bento de Souza - GEC - N° 1894 - C111
# Lucas da Silva Pádua - GEC - N° 2234 - C11

# ----------------------------------------

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

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
# PERGUNTA 4:
# Qual foi o país com mais vitórias?
# ----------------------------------------

# Pegando as vitórias e o país dos pilotos ganhadores
vitorias = results[results['positionOrder'] == 1]
# Juntando com o dataset de drivers para pegar o país
vitorias_por_pais = vitorias.merge(drivers, on='driverId')  

# Agrupando por país e contando as vitórias
vitorias_por_pais = vitorias_por_pais.groupby('nationality').size().sort_values(ascending=False)

# Calculando a porcentagem de vitórias
vitorias_por_pais_percentual = (vitorias_por_pais / vitorias_por_pais.sum()) * 100

# Criando o DataFrame para exibição
dados_vitorias = pd.DataFrame({
  'nacionalidade': vitorias_por_pais.index,
  'qtd_vitorias': vitorias_por_pais.values,
  'percentual_vitorias': vitorias_por_pais_percentual.values
}).head(10)


# Criando o gráfico
fig, ax1 = plt.subplots()
# Gráfico de barras para a quantidade de vitórias
ax1.barh(dados_vitorias['nacionalidade'], dados_vitorias['qtd_vitorias'], color='blue', alpha=0.7, label='Quantidade de Vitórias')
ax1.set_xlabel('Quantidade de Vitórias')
ax1.set_ylabel('Países')
ax1.set_title('Top 10 Países com Mais Vitórias na Fórmula 1')
ax1.invert_yaxis()  # Primeiro lugar no topo
ax1.grid(True, axis='x')
# Adicionando um eixo secundário para a porcentagem de vitórias
ax2 = ax1.twiny()
ax2.plot(dados_vitorias['percentual_vitorias'], dados_vitorias['nacionalidade'], 'r--', label='Porcentagem de Vitórias')
ax2.set_xlabel('Porcentagem de Vitórias')
# Adicionando legenda
fig.legend(loc='lower right', ncol=2, frameon=True)
plt.show()

# ----------------------------------------
# PERGUNTA 5:
# Qual a média de voltas por corrida?
# ----------------------------------------

# Calculando o número máximo de voltas por corrida (ou seja a última volta é a quantidade de total de voltas)
voltas_por_corrida = lap_times.groupby('raceId')['lap'].max()
# Juntando os dados de voltas com o dataset de corridas para obter os circuitos
voltas_com_circuito = voltas_por_corrida.reset_index().merge(races[['raceId', 'circuitId']], on='raceId')

# Calculando a média de voltas por circuito
media_voltas_por_circuito = voltas_com_circuito.groupby('circuitId')['lap'].mean().reset_index()

# Calculando estatísticas descritivas
media_geral_voltas = media_voltas_por_circuito['lap'].mean()
mediana_voltas = media_voltas_por_circuito['lap'].median()
desvio_padrao_voltas = media_voltas_por_circuito['lap'].std()

# Exibindo as estatísticas
print("\nEstatísticas das voltas por circuito:")
print(f"Média Geral de Voltas: {media_geral_voltas:.2f}")
print(f"Mediana de Voltas: {mediana_voltas:.2f}")
print(f"Desvio Padrão de Voltas: {desvio_padrao_voltas:.2f}")

# ----------------------------------------
# PERGUNTA 4:
# Qual piloto correu mais GPs?
# ----------------------------------------

# Cotando participações
gps_por_piloto = results['driverId'].value_counts()


# Criando DataFrame com os pilotos que mais correram
top_gps = gps_por_piloto.reset_index()
top_gps.columns = ['driverId', 'qtd_corridas']

# Juntando com os nomes dos pilotos
top_pilotos = top_gps.merge(drivers, on='driverId')

# Criando coluna de nome completo
top_pilotos['nome_completo'] = top_pilotos['forename'] + ' ' + top_pilotos['surname']

# Saída de dados
print(top_pilotos[['nome_completo', 'qtd_corridas']].head(10))

# ----------------------------------------
# PERGUNTA 5:
# Qual piloto obteve mais pole positions?
# ----------------------------------------

# Pegando pitlotos que largaram da pole
poles = results[results['grid'] == 1]

# Contando quantas poles cada piloto teve
poles_por_piloto = poles['driverId'].value_counts().reset_index()
poles_por_piloto.columns = ['driverId', 'pole_positions']

# Juntando com os nomes dos pilotos
poles_com_nomes = poles_por_piloto.merge(drivers, on='driverId')
poles_com_nomes['nome_completo'] = poles_com_nomes['forename'] + ' ' + poles_com_nomes['surname']

# Saída de dados
top_poles = poles_com_nomes[['nome_completo', 'pole_positions']].head(10)
print(top_poles)


# ----------------------------------------
# PERGUNTA 6:
# Qual GP mais recebeu corridas?
# ----------------------------------------

# Contando quantas vezes cada GP apareceu
gps_mais_corridas = races['name'].value_counts().reset_index()
gps_mais_corridas.columns = ['GP', 'Quantidade_de_Corridas']

# Saída de dados
top_10_gps = gps_mais_corridas.head(10)

# Substituir "Grand Prix" por "GP" para simplificar o nome
top_10_gps['GP'] = top_10_gps['GP'].str.replace('Grand Prix', 'GP')

plt.barh(top_10_gps['GP'], top_10_gps['Quantidade_de_Corridas'], color='seagreen')
plt.xlabel('Número de Corridas')
plt.title('Top 10 GPs que mais receberam corridas')
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()

# ----------------------------------------
# PERGUNTA 7:
# Top 10 PitStops mais rapidos
# ----------------------------------------

# Filtrar pit stops com tempos válidos
pit_stops_validos = pit_stops[pit_stops['milliseconds'].notnull()]
pit_stops_validos = pit_stops_validos[pit_stops_validos['milliseconds'] > 0]

# Ordenar pelos mais rápidos e pegar os 10 primeiros
top_pitstops = pit_stops_validos.sort_values('milliseconds').head(10).copy()
top_pitstops = top_pitstops.reset_index(drop=True)

# Adicionar nome completo do piloto
top_pitstops = top_pitstops.merge(drivers, on='driverId')
top_pitstops['nome_completo'] = top_pitstops['forename'] + ' ' + top_pitstops['surname']

# Converter milissegundos para segundos
top_pitstops['tempo_segundos'] = top_pitstops['milliseconds'] / 1000

# Garantir ordenação correta no gráfico (mais rápido em cima)
top_pitstops = top_pitstops.sort_values('tempo_segundos', ascending=True)

# Plot
plt.barh(top_pitstops['nome_completo'], top_pitstops['tempo_segundos'], color='purple')
plt.xlabel('Tempo do Pit Stop (s)')
plt.title('Top 10 Pit Stops Mais Rápidos da História da F1')
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()


# ----------------------------------------
# PERGUNTA 8:
# Pilotos com mais segundo lugar
# ----------------------------------------

# Filtrar resultados em 2º lugar
segundos_lugares = results[results['positionOrder'] == 2]

# Contar quantas vezes cada piloto ficou em segundo
segundos_por_piloto = segundos_lugares['driverId'].value_counts().reset_index()
segundos_por_piloto.columns = ['driverId', 'segundos_lugares']

# Pegar os top 10
top_segundos = segundos_por_piloto.head(10)

# Juntar com os nomes dos pilotos
top_segundos = top_segundos.merge(drivers, on='driverId')
top_segundos['nome_completo'] = top_segundos['forename'] + ' ' + top_segundos['surname']

# Ordenar para garantir que o gráfico esteja do maior para o menor (visual)
top_segundos = top_segundos.sort_values('segundos_lugares', ascending=True)

# Plot
plt.barh(top_segundos['nome_completo'], top_segundos['segundos_lugares'], color='steelblue')
plt.xlabel('Número de 2º Lugares')
plt.title('Top 10 Pilotos com Mais Segundos Lugares na História da F1')
plt.grid(True)
plt.show()

# ----------------------------------------
# PERGUNTA 9:
# Qual a média de voltas por corrida?
# ----------------------------------------

# Calculando o número máximo de voltas por corrida (ou seja a última volta é a quantidade de total de voltas)
voltas_por_corrida = lap_times.groupby('raceId')['lap'].max()
# Juntando os dados de voltas com o dataset de corridas para obter os circuitos
voltas_com_circuito = voltas_por_corrida.reset_index().merge(races[['raceId', 'circuitId']], on='raceId')

# Calculando a média de voltas por circuito
media_voltas_por_circuito = voltas_com_circuito.groupby('circuitId')['lap'].mean().reset_index()

# Calculando estatísticas descritivas
media_geral_voltas = media_voltas_por_circuito['lap'].mean()
mediana_voltas = media_voltas_por_circuito['lap'].median()
desvio_padrao_voltas = media_voltas_por_circuito['lap'].std()

# Exibindo as estatísticas
print("\nEstatísticas das voltas por circuito:")
print(f"Média Geral de Voltas: {media_geral_voltas:.2f}")
print(f"Mediana de Voltas: {mediana_voltas:.2f}")
print(f"Desvio Padrão de Voltas: {desvio_padrao_voltas:.2f}")

# ----------------------------------------
# PERGUNTA 10:
# Qual foi o país com mais vitórias? (Gráfico de porcentagem)
# ----------------------------------------

# Pegando as vitórias e o país dos pilotos ganhadores
vitorias = results[results['positionOrder'] == 1]
# Juntando com o dataset de drivers para pegar o país
vitorias_por_pais = vitorias.merge(drivers, on='driverId')

# Agrupando por país e contando as vitórias
vitorias_por_pais = vitorias_por_pais.groupby('nationality').size().sort_values(ascending=False)

# Calculando a porcentagem de vitórias
vitorias_por_pais_percentual = (vitorias_por_pais / vitorias_por_pais.sum()) * 100

# Criando o DataFrame para exibição
dados_vitorias = pd.DataFrame({
  'nacionalidade': vitorias_por_pais.index,
  'qtd_vitorias': vitorias_por_pais.values,
  'percentual_vitorias': vitorias_por_pais_percentual.values
}).head(10)


# Criando o gráfico
fig, ax1 = plt.subplots()
# Gráfico de barras para a quantidade de vitórias
ax1.barh(dados_vitorias['nacionalidade'], dados_vitorias['qtd_vitorias'], color='blue', alpha=0.7, label='Quantidade de Vitórias')
ax1.set_xlabel('Quantidade de Vitórias')
ax1.set_ylabel('Países')
ax1.set_title('Top 10 Países com Mais Vitórias na Fórmula 1')
ax1.invert_yaxis()  # Primeiro lugar no topo
ax1.grid(True, axis='x')
# Adicionando um eixo secundário para a porcentagem de vitórias
ax2 = ax1.twiny()
ax2.plot(dados_vitorias['percentual_vitorias'], dados_vitorias['nacionalidade'], 'r--', label='Porcentagem de Vitórias')
ax2.set_xlabel('Porcentagem de Vitórias')
# Adicionando legenda
fig.legend(loc='lower right', ncol=2, frameon=True)
plt.show()


# ----------------------------------------
print("\n Análise concluída com sucesso!")
