import os
from pathlib import Path
import json, sys

    


def work(file):

    #get file path
    BASE_DIR = Path(__file__).resolve().parent
    JSON_DIR = os.path.join(BASE_DIR, file)


    #Deserialize from file
    with open(JSON_DIR, 'r', encoding='utf8', newline='') as f:
        decode_data = json.load(f)





    #function to store and dump dictionary data after each loop and fulfilling if/else conditions
    def storage(k, copy, store={}):
        store.update({k : copy})
        jason = json.dumps(store, indent=4)
        dump_destination = 'schema/schema_1.json'

        #Serialize the JSON file and have it dumped into the dump_destination specified.
        with open(dump_destination, 'w', encoding='utf-8', newline='') as jw:
            jw.write(jason)
        print('Program has been successfully run. Go to schema/schema_1.json to see output.')

    #loop to iterate through python object and get desired data type info
    for key, value in decode_data["message"].items():

        diction = {}
        if (type(value)) == dict:
            diction.update({'type': 'Object'})
            diction.update({'tag':''})
            diction.update({'description':''})
            diction.update({'required':False})

            storage(key, diction)

        elif (type(value)) == str:
            str.update({'type': 'String'})
            diction.update({'tag':''})
            diction.update({'description':''})
            diction.update({'required':False})

            storage(key, diction)

        elif (type(value)) == int:
            diction.update({'type': 'Integer'})
            diction.update({'tag':''})
            diction.update({'description':''})
            diction.update({'required':False})

            storage(key, diction)

        elif (type(value)) == list:
            diction.update({'type': 'Array/List'})
            diction.update({'tag':''})
            diction.update({'description':''})
            diction.update({'required':False})

            storage(key, diction)

        elif (type(value)) == bool:
            diction.update({'type': 'Boolean'})
            diction.update({'tag':''})
            diction.update({'description':''})
            diction.update({'required':False})

            storage(key, diction)

        else:
            print('Not any of these!')

if __name__ == "__main__":
    print('Welcome to the Chike JSON Schema Coverter made for Data2Bots Assessment. Please enter the JSON relative file path')
    file_name = ""

    ## test if file name given in command line
    if len(sys.argv) == 2:
		## grab from command line
	    file_name = sys.argv[1]
    else:
		## Get file from user
	    file_name = input("Please enter file name i.e data/data_1.json: ")
    
    work(file_name)


