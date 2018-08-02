import json
import csv

csvfile = open('Roots.csv', 'r')
jsonfile = open('Roots.json', 'w')

def parseThoughts(thoughts):
    thoughts = thoughts.replace("\"", "")
    thoughts = thoughts.replace("  ", " ")
    
    thoughtsArray = thoughts.split(";")
    tstring = ""
    num = 1 
    for t in thoughtsArray:
        tstring += "\"" + str(num) + "\":\"" + t + "\","
        num += 1
    tstring = tstring[:-1] 
    return tstring


fieldnames = ("title","body","thoughts","verses","type", "set_name")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('{ "roots" : {\n'.encode('utf8'))
for row in reader:
    row["body"] = row["body"].replace("\"","\'")
    thoughts = parseThoughts(row["thoughts"])
    jsonfile.write('"' + row["title"] + '":\n{"title":"' + row["title"] + '","body": "' + row['body'] + '","thoughts": {' + thoughts + '},"verses": "' + row['verses'] +'","type": "' + row['type'] + '","set_name": "' + row['set_name'] + '"},\n')
jsonfile.write('}}')
jsonfile.close