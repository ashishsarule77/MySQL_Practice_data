
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,to_timestamp

spark = SparkSession.builder.appName("transformation").getOrCreate()

'''here we have read csv file'''

df = spark.read.csv(r"D:\MySQL_Practice_git\data_practice\Sales_January_2019.csv",header=True,inferSchema=True)

''' our schema of order date is string i we have chnge this to date for that we use cast or to_date or to_timestamp'''
''' To do this we have two methods withColumn and select / WithColumn create new column and after that we need to drop this column // But when we use Select it will simply apply to_date on original column '''
# df = df.withColumn('Order_Date',to_timestamp(col("Order Date"),"MM/dd/yy HH:mm"))
# df = df.drop("Order Date")

df = df.select(col("Order ID").alias("Order_ID"),col("Product"),col("Quantity Ordered").alias("Quantity_Ordered"),col("Price Each").alias("Price_Each"),col("Purchase Address").alias("Purchase_Address"),to_timestamp(col("Order Date"),"MM/dd/yy HH:mm").alias("Order_Date"))

df.show(truncate=False)

'''we will check our data is in required format ( means schema of dataframe is correct or not if not we will assign schema explicitly )'''

# df.printSchema()

''' Now we seperate date and time from Order_date // there are may ways to seperate 1st with to_date/date_formate'''

df = df.select("Order_Date ")