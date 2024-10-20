def decimal_2binary(n):
    if n > 1:
        return decimal_2binary(n // 2) + str(n % 2)
    return str(n)

n = int(input("ENTER A NUMBER.........:)"))
def reverse_num(number):
    reversed_binary = decimal_2binary(number)[::-1]
    print("The reversed binary form of your input is...", reversed_binary)

reverse_num(n)