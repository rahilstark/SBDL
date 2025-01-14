from pyspark.sql import SparkSession
from transform import entity_transform

spark = SparkSession.builder.getOrCreate()

account_df = spark.read.csv("test_data/accounts/account_samples.csv", header=True, sep=',').limit(10)
parties_df = spark.read.csv("test_data/parties/party_samples.csv", header=True, sep=',').limit(10)
address_df = spark.read.csv("test_data/party_address/address_samples.csv", header=True, sep=',').limit(10)

inter_df = account_df.join(parties_df, "account_id", "left").drop(parties_df["account_id"])
res_df = inter_df.join(address_df, "party_id", "left").drop(address_df["party_id"])
res_df.show()


transformed_df = res_df.rdd.map(
    lambda row: entity_transform(row)).toDF()
transformed_df.show()