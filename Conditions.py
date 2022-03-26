def armstrongnum(x):
    sum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if x == sum:
        return True
    else:
        return False


def divby5(x):
    if x % 5 == 0:
        return True
    else:
        return False


def largest(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


def check_EvenorOdd(x):
    if x % 2 == 0:
        return True
    else:
        return False



if __name__ == "__main__":

    x = int(input("Enter 1st Num "))
    y = int(input("Enter 2nd Num "))
    z = int(input("Enter 3rd Num "))

    armstrong = armstrongnum(x)
    print(armstrong)

    divby = divby5(x)
    print(divby)

    large = largest(x, y, z)
    print(large)

    evenorodd = check_EvenorOdd(x)
    print(evenorodd)