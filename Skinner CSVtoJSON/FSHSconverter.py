import csv
import json

csvfile = open('Attributes.csv', 'r')
jsonfile = open('Attributes.json', 'w')


fieldnames = ("index","title","devotional","verses","set_name")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('{ "attributes" : {\n')
for row in reader:
    jsonfile.write('"' + row["title"] + '":\n{"index":' + row["index"] + ',"title":"' + row["title"] + '", "devotional": "' + row['devotional'] + '", "verses": "' + row['verses'] + '","set_name": "' + row['set_name'] + '"},\n')
jsonfile.write('} }')
jsonfile.close