import math as m
def run():
    my_dict = {i:m.sqrt(i) for i in range(1,1001)}
    print(my_dict)

if __name__ == "__main__":
    run()