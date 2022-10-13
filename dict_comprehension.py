def run():
    dic_com = {i:i**3 for i in range(1,101) if i%3 != 0}
    print(dic_com)

if __name__ == "__main__":
    run()