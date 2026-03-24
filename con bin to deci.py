decimal_number = int(input("Enter a decimal number: "))

binary_number = bin(decimal_number)

print("Binary representation:", binary_number[2:])
decimal_number = int(input("Enter a decimal number: "))

binary = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary = str(remainder) + binary
    decimal_number = decimal_number // 2

print("Binary representation:", binary)
