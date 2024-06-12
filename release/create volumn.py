# Databricks notebook source
# MAGIC %sh
# MAGIC wget -O "/Volumes/dev_workspace_github2/default/myManagedVolume/babynames.csv" "https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME myManagedVolume
# MAGIC     COMMENT 'This is my example managed volume';

# COMMAND ----------

# MAGIC %sql
# MAGIC describe volume myManagedVolume

# COMMAND ----------

df = spark.read.table("demo_catalog2.default.employees")
df.display()

# COMMAND ----------

from pyspark.sql.functions import col
df1 = df.groupBy(col("deparment"))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT unix_timestamp();
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT months_between('2024-09-10', '2024-06-01');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT last_day('2024-06-10');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT from_unixtime(unix_timestamp(), 'yyyy-MM-dd')
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT dayofweek('2024-06-10') AS day_of_week;
# MAGIC
