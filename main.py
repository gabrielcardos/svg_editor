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
        code_changed = phrase_changed.replace('00-0001', str(options["code"].zfill(4)))

        #if QR code is identified, it adds the code
        if options["qrcode"] != "0":
            qr_code_added = code_changed.replace('fill="#2B2B2B" d=""',
                                                  'fill="#2B2B2B" d="'+str(options["qrcode"])+'" ')


            with open("./build_files/Panetone" + str(options["color"]) + ".svg", "w") as file1:
                file1.write(qr_code_added)
                file1.close()

        else:
            remove_text = code_changed.replace('#191919', '#FFFFFF')
            #if QR code is not identified, it removes the letters
            with open("./build_files/Panetone"+str(options["color"])+".svg", "w") as file1:
                file1.write(remove_text)
                file1.close()
