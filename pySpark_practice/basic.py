#%%
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder.appName('my_vscode_session').getOrCreate()

# create new data frame

data =[
    (101,"ashish","pune",23),
    (102,"vishal","nagpur",26),
    (103,"ashwini","mumbai",29)
]

columns =["id","name","city","age"]

df=spark.createDataFrame(data,columns)

df.show()

#create data frame with schema
#%%
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder.appName('my_vscode_session').getOrCreate()

schema = StructType([
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True),
    StructField("city",StringType(),True)

])

data =[
    ("ashish",23,"pune"),
    ("vishal",26,"nashik"),
    ("ashwini",29,"mumbai")


]

df1 =spark.createDataFrame(data,schema)
df1.show()
# %%
