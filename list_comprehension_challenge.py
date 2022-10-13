def run():
    multiply = [ i for i in range(1,1000000) if i%4 == 0 and i%6 == 0 and i%9 ==0 ]
    print(multiply)

if __name__ == "__main__":
    run()