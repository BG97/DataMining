# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:13:14 2018

@author: benny
"""
import sys

#get data
unclean_list = []
check_list = []
with open('trans_unclean.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.replace(';',' ').split(" ") for line in stripped if line)
    with open('codeprodmap.txt','r') as check_file:
        stripped = (line.strip() for line in check_file)
        check_code = (line.split(" ") for line in stripped if line)
 

        for i in lines:
            unclean_list.append(i)
        
        for i in check_code:
            check_list.append(i)
        

#data preprocessing
clean_list = []

for i in range(len(unclean_list)):
    for j in range(len(unclean_list[i])):
        for k in range(len(check_list)):
            if unclean_list[i][j] == check_list[k][1]:
                unclean_list[i][j] = check_list[k][0]

check_list = list(map(list,zip(*check_list)))
for i in range(len(unclean_list)):     
    if unclean_list[i][-1] == '':
        unclean_list[i].pop()
    boolean = True
    for j in range(len(unclean_list[i])):
        if unclean_list[i][j] in check_list[0]:
            continue
        else:
            boolean = False
            break
    if boolean:
        clean_list.append(unclean_list[i]) 
                        
#Apriori
#count maximum itermset
max_itemset = 0
for i in range(len(clean_list)):
    if len(clean_list[i]) > max_itemset:
        max_itemset = len(clean_list[i])

#sort itemset
for i in range(len(clean_list)):
    clean_list[i] = sorted(clean_list[i])
    
#big list for all the possible frequesnt itemset relation
big_list = []
num_item = 1
rows = len(clean_list)
while max_itemset >= num_item:
    for i in range(rows):
        for j in range(len(clean_list[i])):
            k=0
            following = j
            group_item = []
            while k<num_item and following<len(clean_list[i]):
                group_item.append(clean_list[i][following])
                following += 1
                k += 1
                if group_item not in big_list:
                    big_list.append(group_item)
    num_item += 1

#count frequency in big list for each itemset
support = 5
output = []
for i in range(len(big_list)):
    num_support = 0 
    for j in range(len(clean_list)):
        for k in range(len(big_list[i])):
            if big_list[i][k] in clean_list[j]:
                in_list = True
            else:
                in_list = False
                break
        if in_list == True:
            num_support += 1
    big_list[i].append(num_support)

#output
for i in range(len(big_list)):
    if big_list[i][-1] >= support:
        output.append(big_list[i])

output_file = open("output.txt","w")
output_file.write(str(output))
output_file.close()


