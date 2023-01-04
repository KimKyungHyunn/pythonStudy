'''
Created on 2023. 1. 4.

@author: kdkin
'''
import random
import Higher_Lower.art as art
import Higher_Lower.data as data

#constants
name = "name"
followerCount = "follower_count"
copyDataList = data.dataList

#random pick index -> pick another index -> choose ->
#if win: remove data of lower index & count++ & pick another index
#else: break

#get first index & data & follower_count & remove data at list
preIndex = random.randint(0, len(copyDataList)-1)
preData = copyDataList[preIndex]

del copyDataList[preIndex]

playGame = True
count = 0

print(art.logo)

while len(copyDataList) > 0:
    newIndex = random.randint(0, len(copyDataList)-1)
    newData = copyDataList[newIndex]

    print(preData[name] + " " + str(preData[followerCount]))
    print(art.vs)
    print(newData[name] + " " + str(newData[followerCount]))
    
    answer = 0
    
    if preData[followerCount] > newData[followerCount]:
        answer = 1
    else:
        answer = 2
    
    pickedNum = int(input("who's follower_count is bigger? choose number in 1 & 2 \n"))
    
    #win 
    if answer == pickedNum:
        #remove newData at list
        del copyDataList[newIndex] 
        
        #change preData
        if answer == 2:
            preIndex = newIndex
            preData = newData             
        
        count += 1
        
        #case: list empty
        if len(copyDataList) == 0:
            print(f"your final winner, times {count}\n")
            break
        else:              
            print(f"you win, times {count}\n")
    
    #loose    
    else:
        print(f"you loose, times {count}\n")
        break

    

