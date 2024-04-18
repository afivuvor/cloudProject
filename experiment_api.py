import requests
import csv
import json

url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_7_1_Trade_related_Indicators_CO2_emissions_embodied_in_trade/FeatureServer/0/query?where=1%3D1&outFields=ISO2,ISO3,CTS_Code,Country,F2010,F2011,F2012,F2013,F2014,F2015,F2016,F2017,F2018&outSR=4326&f=json"

response = requests.get(url)
co2_data = response.json()["features"]
cleaned_data = []
countries = []

for obj in co2_data:
    if obj["attributes"]["CTS_Code"] == "ECBTP":
        cleaned_data.append(obj["attributes"])


# put data in json file
with open('co2_production_data.json', 'w') as output_file:
    json.dump(cleaned_data, output_file)


# turn json file into csv
with open('co2_production_data.json') as json_file:
    data = json.load(json_file)

    # Open CSV file in write mode with newline='' to prevent empty rows
    with open('co2_production_data_per_year.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header row
        header = data[0].keys()  # Assuming all dictionaries in the list have the same keys
        csv_writer.writerow(header)

        # Write data rows
        for co2 in data:
            csv_writer.writerow(co2.values())

# concatenate columns into one column

# Path to the input CSV file
with open('co2_production_data_per_year.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    # Path to the output CSV file
    with open('co2_production_data.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['ISO2', 'ISO3', 'CTS_Code', 'Country', 'Total_CO2'])

        for row in csv_reader:
            total_co2 = sum(float(value) for value in row[4:])
            csv_writer.writerow([row[0], row[1], row[2], row[3], round(total_co2, 3)])



