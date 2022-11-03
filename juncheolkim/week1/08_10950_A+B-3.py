input_item = int(input(""))

for i in range(input_item):
    globals()[f'input_{i}'] = input()


for i in range(input_item):
    x = eval(f'input_{i}')
    y = int(x.split(" ")[0]) + int(x.split(" ")[1])
    print(y)