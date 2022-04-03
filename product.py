# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 01:49:32 2022

@author: JYH
"""
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
##------------------------------------------------------------##
for q in products:
    print(q[0],'price is:', q[1])

#write product into a string file txt    

with open('product.csv', 'w', encoding = 'utf-8') as f:
    #f.write('product' + ',' + 'price' + '\n')
    f.write('product, price\n')
    for r in products:
        f.write(r[0] + ',' + r[1] + '\n')
    