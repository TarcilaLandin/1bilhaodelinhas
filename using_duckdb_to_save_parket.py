import duckdb
import time

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
    result.show()

    #Save the result to a Parquet file
    result.write_parquet('data\measurements_summary.parquet')

if __name__ == "__main__":
    import time
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} sec")