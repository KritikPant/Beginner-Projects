while True:
    num = int(input("Enter a number:\n"))
    div = [n for n in range(2, num) if num % n == 0]

    def prime(num):
        if len(div) == 0 and num > 1:
            print("Prime")
        else:
            print("Not prime")
            print("Facotrs are: ")
            print(*div, sep="\n")
            print("\n\n")

    prime(num)
