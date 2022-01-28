import json
import csv

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8' ) as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf,delimiter=';')

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

    return jsonArray

#open template
with open('./panetone-template/svg-text.txt', 'r') as file:
    template = file.read()

#import and parse json into CSV
csvFilePath = r'config_prod.csv'
jsonFilePath = r'data.json'
config_array = csv_to_json(csvFilePath, jsonFilePath)
print(config_array)

#changes the configuration
for options in config_array:
    if options['activated'] == "1":
        color_changed = template.replace('#bc2a66', str(options["color"]))
        phrase_changed = color_changed.replace('strawberry', str(options["phrase"]))

        if options["qrcode"] == "0":
            pass

        with open("myfile"+str(options["color"])+".txt", "w") as file1:
            file1.write(phrase_changed)
            file1.close()
