def divisors(num):
    try:
        if num < 1:
            raise ValueError("Debes ingresar un numero mayor a cero")
        divisors=[i for i in range(1,num+1) if num % i == 0]
        return divisors
    except ValueError as ve:
        return ve
    
def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()