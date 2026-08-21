from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("mySQL ETL pipeline") \
    .config(
        "spark.jars",
        r"D:\JDBC\mysql-connector-j-26.7.0.jar"
    ) \
    .getOrCreate()

transection_df = spark.read.csv(r"D:\Downloads\Sales_June_2019.csv", header=True, inferSchema=True)
# transection_df.show()


transection_df2=transection_df.withColumn("insert_date",current_date())

transection_df2.show()

#writing data to ETL_pipeline

transection_df2.write.format("jdbc")\
    .option("url", "jdbc:mysql://localhost:3306/ETL_pipeline")\
        .option("driver", "com.mysql.cj.jdbc.Driver")\
            .option("dbtable", "transaction_details")\
                .option("user", "root")\
                    .option("password", "Ashish@123")\
                        .option("batchsize", "1000")\
                            .mode("append") \
                                .save()


spark.stop()


# .option("url", "jdbc:mysql://localhost:3306/ETL_pipeline")\ ->
#it is the JDBC connection URL. It tells Spark where your MySQL database is located and which database you want to connect to.

# jdbc:mysql://localhost:3306/etl_pipeline3
# │    │       │         │    │
# │    │       │         │    └── Database name
# │    │       │         └─────── MySQL port
# │    │       └───────────────── MySQL server
# │    └───────────────────────── MySQL JDBC protocol
# └────────────────────────────── JDBC
       

#.option("driver", "com.mysql.cj.jdbc.Driver")\ -->  "Use the MySQL JDBC driver to communicate with MySQL."   