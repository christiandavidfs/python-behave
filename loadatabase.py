import psycopg2
import json
import codecs
import glob



read_files = glob.glob("result/*.json")
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

with open("merged_file.json", "w") as outfile:
    json.dump(output_list, outfile)


# path_to_file = input('Enter path to json file:')
with open('merged_file.json', 'r') as data_file:
    data = json.load(data_file)

collection_array = []
for item in data:
    collection_array.append(json.dumps(item))



try:
    conn = psycopg2.connect(database="behavee", user="postgres", password="m1jnkj03MK",host="127.0.0.1",port="5432")
    print ("opened  database successfully")
    cur = conn.cursor()

    for element in collection_array:
        cur.execute("INSERT INTO results (json_column_name) VALUES (%s)", (element,))
    print("successfully inserted records")    


except psycopg2.Error as e:
    raise

finally:
    conn.commit()
    conn.close()
    print("connection is closed")
