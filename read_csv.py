import csv 

def read_csv(path):
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
    data=read_csv('./files/world_population.csv')
    print(data[0])

if __name__ == '__main__':
    run()