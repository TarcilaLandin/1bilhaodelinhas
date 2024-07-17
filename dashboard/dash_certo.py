import streamlit as st
import duckdb
import pandas as pd
import os

# Função para carregar dados do arquivo Parquet
def load_data():
    con = duckdb.connect()
    parquet_file_path = os.path.join('data', 'measurements_summary.parquet')
    df = con.execute(f"SELECT * FROM '{parquet_file_path}'").df()
    con.close()
    return df

# Função principal para criar o dashboard
def main():
    st.title("Weather Station Summary")
    st.write("This dashboard shows the summary of weather data from various weather stations.")
    
    # Carregar os dados
    data = load_data()  # Chama a função para executar a consulta
    
    # Exibir os dados em formato de tabela
    st.dataframe(data)

if __name__ == "__main__":
    main()
