import base64
import json
import csv
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = 692136579

def create_image_tobase(text,size):
    img = Image.new('RGB', (size, 360), color=(255, 255, 255))
    fnt = ImageFont.truetype('/Library/Fonts/Nimbus-Sans-D-OT-Light_32752.ttf', 280)
    d = ImageDraw.Draw(img)
    d.text((15, 15), str(text), font=fnt, fill=(0, 0, 0))
    img.save('pil_text_font.png')
    image = open('pil_text_font.png', 'rb')
    image_read = image.read()
    image_encode = base64.b64encode(image_read)
    image_encode = str(image_encode).replace("b'","")
    image_encode = str(image_encode).replace("'", "")
    return image_encode

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
        #phrase_changed = color_changed.replace('strawberry', str(options["phrase"]))
        #code_changed = phrase_changed.replace('00-0001', str(options["code"].zfill(4)))
        phrase_changed = color_changed.replace('strawberry', "")
        code_changed = phrase_changed.replace('00-0001', "")
        code_changed = code_changed.replace('codebase',str(create_image_tobase(str(options["code"].zfill(4)),940)))
        code_changed = code_changed.replace('phrase', str(create_image_tobase(str(options["phrase"]),4040)))

        #if QR code is identified, it adds the code
        if options["qrcode"] != "0":
            qr_code_added = code_changed.replace('fill="#2B2B2B" d=""',
                                                  'fill="#2B2B2B" d="'+str(options["qrcode"])+'" ')
            with open("./build_files/Panetone"+str(options["color"])+".svg", "w") as file1:
                 file1.write(qr_code_added)
                 file1.close()

        else:
            remove_text = code_changed.replace('#191919', '#FFFFFF')
            #if QR code is not identified, it removes the letters
            with open("./build_files/Panetone"+str(options["color"])+".svg", "w") as file1:
                file1.write(remove_text)
                file1.close()
