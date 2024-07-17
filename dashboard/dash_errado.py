import streamlit as st
import duckdb
import pandas as pd

# Função para carregar dados do arquivo CSV e executar a consulta
def create_duckdb():
    result = duckdb.sql("""
    SELECT
        cidade,
        min(temperatura) as temperatura_minima,
        cast(avg(temperatura) as DECIMAL(3,1)) as temperatura_media,
        max(temperatura) as temperatura_maxima
    FROM read_csv('data/measurements.txt', AUTO_DETECT=FALSE, sep=';', COLUMNS={'cidade': 'VARCHAR', 'temperatura': 'DECIMAL(3,1)'})
    GROUP BY cidade
    ORDER BY cidade
    """)
    # Convertendo o resultado para DataFrame
    df = result.df()
    return df

# Função principal para criar o dashboard
def main():
    st.title("Weather Station Summary")
    st.write("This dashboard shows the summary of weather")
    
    # Carregar os dados
    data = create_duckdb()  # Chama a função para executar a consulta
    
    # Exibir os dados em formato de tabela
    st.dataframe(data)

if __name__ == "__main__":
    main()
