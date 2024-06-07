# Databricks notebook source
container_name = {CONTAINER_NAME}
storage_account_name = {STORAGE_ACCOUNT_NAME}

dbutils.fs.mount(
    source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
    mount_point = "/mnt/data"
)


# COMMAND ----------

print("will it work?")

# COMMAND ----------

print("will it work again?")
