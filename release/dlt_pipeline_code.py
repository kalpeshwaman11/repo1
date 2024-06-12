# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE baby_names_sql_raw
# MAGIC COMMENT "Popular baby first names in New York. This data was ingested from the New York State Department of Health."
# MAGIC AS SELECT Year, `First Name` AS First_Name, County, Sex, Count FROM read_files(
# MAGIC   '/Volumes/dev_workspace_github2/default/myManagedVolume/babynames.csv',
# MAGIC   format => 'csv',
# MAGIC   header => true,
# MAGIC   mode => 'FAILFAST')

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE baby_names_sql_prepared(
# MAGIC   CONSTRAINT valid_first_name EXPECT (First_Name IS NOT NULL),
# MAGIC   CONSTRAINT valid_count EXPECT (Count > 0) ON VIOLATION FAIL UPDATE
# MAGIC )
# MAGIC COMMENT "New York popular baby first name data cleaned and prepared for analysis."
# MAGIC AS SELECT
# MAGIC   Year AS Year_Of_Birth,
# MAGIC   First_Name,
# MAGIC   Count
# MAGIC FROM live.baby_names_sql_raw;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REFRESH LIVE TABLE top_baby_names_sql_2021
# MAGIC COMMENT "A table summarizing counts of the top baby names for New York for 2021."
# MAGIC AS SELECT
# MAGIC   First_Name,
# MAGIC   SUM(Count) AS Total_Count
# MAGIC FROM live.baby_names_sql_prepared
# MAGIC WHERE Year_Of_Birth = 2021
# MAGIC GROUP BY First_Name
# MAGIC ORDER BY Total_Count DESC
# MAGIC LIMIT 10;
