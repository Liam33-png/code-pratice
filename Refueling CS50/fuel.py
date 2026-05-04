def main():
    fuel = input("Fuel:")
    print(gauge(convert(fuel)))


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        return (f"{int(int(x) / int(y) * 100)}")
    


def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    elif int(percentage) >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
