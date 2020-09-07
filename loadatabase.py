import psycopg2
import json
import codecs
import glob

result = {}

files = glob.glob('./result/*.json')

with codecs.open('combined_results.json', 'w', encoding='utf-8') as outfile:
    for file in files:
        f = open(file, 'r')
        data = json.load(f)
        json.dump(data, outfile, ensure_ascii=False, indent=None)
        outfile.write("\n")


# path_to_file = input('Enter path to json file:')
with open('combined_results.json', 'r') as data_file:
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
