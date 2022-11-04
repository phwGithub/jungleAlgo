input_item = int(input(""))


if input_item % 4 == 0 and input_item % 100 != 0  :
    print("1")
elif input_item % 400 == 0:
    print("1")
else:
    print("0")