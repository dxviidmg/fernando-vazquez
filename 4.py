def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def suma_fibonacci():
    n = 0
    r = 0
    suma = 0

    while True:
        r = fibonacci(n)
        n+=1
        if r < 100:
            continue

        if r > 10000:
            break

        suma += r

    print(suma)

def main():
    suma_fibonacci()

if __name__ == "__main__":
    main()