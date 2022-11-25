import csv
import matplotlib.pyplot as plt

def reader(path):
    with open(path, 'r') as file:
        reader=csv.reader(file)
        header=next(reader)
        data = []
        for row in reader:
            iterable=zip(header, row) # zip the header and row
            country_data = dict(iterable) # create a dictionary
            data.append(country_data) # append the dictionary to the list
        return data

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    plt.bar(labels, values)
    plt.show()

def run():
    data=reader('./files/world_population.csv')
    pais = input("Ingrese el nombre del país: ")
    country_data = [country for country in data if country['Country/Territory'] == pais]
    simplified_data = {
        "2022": int(country_data[0]['2022 Population']),
        "2020": int(country_data[0]['2020 Population']),
        "2015": int(country_data[0]['2015 Population']),
        "2010": int(country_data[0]['2010 Population']),
        "2000": int(country_data[0]['2000 Population']),
        "1990": int(country_data[0]['1990 Population']),
        "1980": int(country_data[0]['1980 Population']),
        "1970": int(country_data[0]['1970 Population']),
    }
    labels = list(simplified_data.keys())
    values = list(simplified_data.values())
    generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()