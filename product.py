products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    price = input('請輸入商品價格：')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    products.append([name, price])
print(products)

for p in products:
	print(p)

with open ('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')