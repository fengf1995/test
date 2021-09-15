# Databricks notebook source
display(dbutils.fs.ls("dbfs:/FileStore"))

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls /FileStore/

# COMMAND ----------

# MAGIC %fs cd /FileStore/
# MAGIC %fs ls

# COMMAND ----------

dbutils.fs.put("/tmp/my_new_file", "This is a file in cloud storage.")

# COMMAND ----------

df = spark.read.csv("dbfs:/FileStore/train.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

