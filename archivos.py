def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Juan", "José", "Paulina", "Jazmín", "Mariano"]
    with open("./files/names.txt", "w", encoding="utf-8") as fi:
        for name in names:
            fi.write(f"{name}\n")


def run():
    read()
    write()

if __name__ == "__main__":
    run()