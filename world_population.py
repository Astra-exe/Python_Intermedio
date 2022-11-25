import csv
import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    plt.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

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

def run():
    data = reader('./files/world_population.csv')
    countries = [country['Country/Territory'] for country in data]
    percentage = [float(country['World Population Percentage']) for country in data]
    generate_pie_chart(countries, percentage)
    

if __name__ == '__main__':
    run()