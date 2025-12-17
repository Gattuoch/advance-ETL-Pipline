from pyspark.sql import SparkSession
from pyspark.sql.functions import year, avg

spark = SparkSession.builder \
    .appName("ClimateSparkTransform") \
    .getOrCreate()

df = spark.read.format("jdbc") \
    .option("url", "jdbc:duckdb:analytics.db") \
    .option("dbtable", "in_climate") \
    .load()

result = df.withColumn("year", year("dt")) \
           .groupBy("year") \
           .agg(avg("LandAverageTemperature").alias("avg_temp"))

result.write \
    .format("jdbc") \
    .option("url", "jdbc:duckdb:analytics.db") \
    .option("dbtable", "report_climate_spark") \
    .mode("overwrite") \
    .save()
