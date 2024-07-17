from csv import reader
from collections import defaultdict
import time
from pathlib import Path

# Função para processar as temperaturas de um arquivo de texto
def processar_temperaturas(path_do_txt: Path) -> dict:
    print("Iniciando o processamento do arquivo.")

    start_time = time.time()  # Marca o tempo de início do processamento

    # Dicionário que armazenará listas de temperaturas para cada estação
    temperatura_por_station = defaultdict(list)  

    # Gerenciador de contexto para abrir o arquivo e garantir que ele será fechado após a leitura
    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')  # Lê o arquivo CSV com ';' como delimitador
        for row in _reader:
            # Extrai o nome da estação e a temperatura de cada linha do arquivo
            nome_da_station, temperatura = str(row[0]), float(row[1])
            # Adiciona a temperatura na lista correspondente à estação
            temperatura_por_station[nome_da_station].append(temperatura)
    print("Dados carregados. Calculando estatísticas...")

    # Dicionário para armazenar os resultados das estatísticas calculadas para cada estação
    results = {}

    # Calcula as estatísticas (mínima, média e máxima) para cada estação
    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)  # Calcula a temperatura mínima
        mean_temp = sum(temperatures) / len(temperatures)  # Calcula a temperatura média
        max_temp = max(temperatures)  # Calcula a temperatura máxima
        # Armazena as estatísticas no dicionário de resultados
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatísticas calculadas. Ordenando...")

    # Ordena os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # Formata os resultados para exibir uma string com as temperaturas mínima, média e máxima
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()  # Marca o tempo de término do processamento
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    # Retorna os resultados formatados
    return formatted_results

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Define o caminho do arquivo de texto a ser processado
    path_do_txt: Path = Path(r"data\measurements.txt")
    # Chama a função de processamento e armazena os resultados
    resultados = processar_temperaturas(path_do_txt)
    # Imprime os resultados formatados
    #print(resultados)
