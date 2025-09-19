from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = (SparkSession.builder
         .appName("bronze_ingest_delta")
         .config("spark.sql.catalog.lake", "org.apache.iceberg.spark.SparkCatalog")
         .config("spark.sql.catalog.lake.type", "hive")
         .config("spark.sql.catalog.lake.uri", "thrift://hive-metastore:9083")
         .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
         .config("spark.sql.catalog.delta", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
         .getOrCreate())

landing = "s3a://lakehouse/landing/unimed/claims/*.csv"

df = (spark.read.option("header", True).csv(landing)
      .withColumn("_ingest_ts", current_timestamp()))

spark.sql("CREATE NAMESPACE IF NOT EXISTS delta.bronze")
spark.sql(
    """
    CREATE TABLE IF NOT EXISTS delta.bronze.claims (
        claim_id string,
        patient_id string,
        provider_id string,
        service_date string,
        amount string,
        status string,
        _ingest_ts timestamp
    ) USING delta
    LOCATION 's3a://lakehouse/delta/bronze/claims'
    """
)

df.write.format("delta").mode("append").save("s3a://lakehouse/delta/bronze/claims")

spark.stop()
