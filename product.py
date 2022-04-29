# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 01:49:32 2022

@author: JYH
"""
#讀取檔案
products = []
with open('product2.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品, 價格' in line:
            continue
        name, price = line.strip().split(',') # strip \n and then split comma
        products.append([name, price])      
print(products)

#使用者輸入
products = []
while True:
   name = input('Please key in product names:')
   if name == 'q':
       break
   price = input('Please key in price:')
   #p = []
   #p.append(name) # add name into p
   #p.append(price) # add price into p
   #p = [name, price]
   products.append([name, price]) # add p into product list
print(products)

print(products [0][0]) ## find the 1st column in 1st row

##印出購買紀錄
for q in products:
    print(q[0],'price is:', q[1])

#write product into a string file txt    

##寫入檔案
with open('product2.csv', 'w', encoding = 'utf-8') as f:
    #f.write('商品' + ',' + '價格' + '\n') 
    f.write('商品, 價格\n')
    for r in products:
        f.write(r[0] + ',' + r[1] + '\n')


    