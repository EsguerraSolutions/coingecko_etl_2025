from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
print("Spark version:", spark.version)
spark.range(5).show()
spark.stop()