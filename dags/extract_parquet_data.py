@dag(
    start_date=datetime(2023, 1, 1),
    schedule=[Dataset("start")],
    catchup=False,
    tags=["part_2"]
)
def extract_parquet_data():

    @task(outlets=[Dataset("duckdb://include/dwh/in_emissions")])
    def load_parquet_to_duckdb(
        duckdb_conn_id: str,
        table_name: str,
        parquet_path: str
    ):
        from duckdb_provider.hooks.duckdb_hook import DuckDBHook

        conn = DuckDBHook(duckdb_conn_id).get_conn()
        cursor = conn.cursor()

        cursor.sql(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM read_parquet('{parquet_path}');
        """)

    load_parquet_to_duckdb(
        duckdb_conn_id=gv.CONN_ID_DUCKDB,
        table_name="in_emissions",
        parquet_path="include/climate_data/weather.parquet"
    )

extract_parquet_data()
