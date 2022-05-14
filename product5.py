# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 01:49:32 2022
@author: JYH
"""

import os


#讀取檔案
def read_file(filename):
    product = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            name, price = line.strip().split(',') # strip \n and then split comma
            product.append([name, price])      
    return product #上方只完成print proudct, 還需要把值return到product
    


# =============================================================================
# products = []
# with open('product2.csv', 'r', encoding = 'utf-8') as f:
#     for line in f:
#         if '商品, 價格' in line:
#             continue
#         name, price = line.strip().split(',') # strip \n and then split comma
#         products.append([name, price])      
# print(products)
# =============================================================================

#使用者輸入商品到一個已存在的檔案
def user_input(product):
    while True:
        name = input('Please key in product names:')
        if name == 'q':
            break
        price = input('Please key in price:')
        price = int(price) #input 輸入context為str, 轉成int方便之後運算
        product.append([name, price]) # add p into product list
    print(product)
    return product


##印出購買紀錄
def print_product(product):
    for q in product:
        print(q[0],'price is:', q[1])


#write product into a string file txt    

##寫入檔案
def write_file(filename, product):
    with open(filename, 'w', encoding = 'utf-8') as f:
        #f.write('商品' + ',' + '價格' + '\n') 
        f.write('商品, 價格\n')
        for r in product:
            f.write(r[0] + ',' + str(r[1]) + '\n') #prices were int and csv file context is divided with coma


######################本文開始##################################

def main():
    filename = 'product.csv'
    if os.path.isfile(filename): #check file exist or not
            print('found it!')
            product = read_file(filename)
    else:
            print('could not find the file')
            
    product = user_input(product)
    print_product(product)
    write_file('product.csv', product)
    

main()