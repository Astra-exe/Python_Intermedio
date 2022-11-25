import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    plt.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    plt.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

def run():
    labels = ['A', 'B', 'C']
    values = [100, 400, 200]
    generate_pie_chart(labels, values)

if __name__ == '__main__':
    run()