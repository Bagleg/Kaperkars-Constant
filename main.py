
def main():
    invalid = ["0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999"]
    n = 0
    number = input("Please enter a four digit number: ")
    if len(number) != 4:
        print("Error: invalid entry")
        main()
    else:
        if number in invalid:
            print("Error: invalid entry")
            main()
        mod(number, n)


def mod(number, n):
    order = list(str(number))
    for num in order:
        int(float(num))
    order.sort(reverse=True)
    reverse = order.copy()
    reverse.reverse()
    reverse = "".join(reverse)
    order = "".join(order)
    loop(reverse, order, n)


def loop(reverse, order, n):
    number = int(order) - int(reverse)
    print(number)
    n += 1
    if number == 6174:
        print(n)
    else:
        mod(number, n)


if __name__ == '__main__':
    main()

