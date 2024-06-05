# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE sample_table (
# MAGIC     id INT PRIMARY KEY,
# MAGIC     name VARCHAR(50),
# MAGIC     age INT,
# MAGIC     city VARCHAR(50)
# MAGIC );
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO hive_metastore.default.sample_table VALUES
# MAGIC (1, 'Alice', 30, 'New York'),
# MAGIC (2, 'Bob', 25, 'Los Angeles'),
# MAGIC (3, 'Charlie', 35, 'Chicago'),
# MAGIC (4, 'Diana', 28, 'San Francisco');
# MAGIC

# COMMAND ----------

print("hello world")

# COMMAND ----------

print("abhay")
