import glob
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import json
from pandas import json_normalize

#merge jsons

read_files = glob.glob("result/*.json")
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

with open("source.json", "w") as outfile:
    json.dump(output_list, outfile)


# path_to_file = input('Enter path to json file:')
with open('source.json', 'r') as data_file:
    data = json.load(data_file)

collection_array = []
for item in data:
    collection_array.append(json.dumps(item))

df = pd.read_json (r'source.json')
export_csv = df.to_csv (r'end.csv',columns=['name','status','steps','start','stop','uuid','historyId','labels'], index = None, header=True, sep=';')

# connect to the database
conn = psycopg2.connect(host='localhost',
                       dbname='behavee',
                       user='postgres',
                       password='m1jnkj03MK',
                       port='5432')  
#create a cursor object 
#cursor object is used to interact with the database
cur = conn.cursor()

#create table with same headers as csv file
cur.execute("CREATE TABLE IF NOT EXISTS results(name text,status text,steps text,start text,stop text,uuid text,historyId text,labels text)")

#open the csv file using python standard file I/O
#copy file into the table just created 
with open('end.csv', 'r') as f:
    next(f) # Skip the header row.
    #f , <database name>, Comma-Seperated
    cur.copy_from(f, 'results', sep=';')
    #Commit Changes
    conn.commit()
    #Close connection
    conn.close()


f.close()