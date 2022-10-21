def divisors(num):
    #AFIRMO QUE EL NUMERO DEBE SER MAYOR A 0
    assert num > 0, "Debes ingresar un numero mayor a 0"
    divisors=[i for i in range(1,num+1) if num % i == 0]
    return divisors
    
def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))


if __name__ == '__main__':
    run()