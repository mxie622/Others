library(RPostgreSQL)
library(ggplot2)
drv<-dbDriver("PostgreSQL")
conn_aws<-dbConnect(
  drv,
  host='wigramdbinstance.c5iztr3mmppo.us-east-2.rds.amazonaws.com', # AWS
  port=5432, # 
  dbname='xxx', # 
  user='yyy', # 
  password='zzz' # 
)
data_aws <- fetch(dbSendQuery(conn_aws,'select * from macro.data where seriesid=105'), -1) # 

submitQuery<-function(conn, SQL) {
  return(fetch(dbSendQuery(conn,SQL),-1))
}

data_easy <- submitQuery(conn_aws, 'select * from macro.desc') # 
data_easy[1:10,c(1,3)]
