cnt = 0 

for i in range(1,5) : 
    #print('百位数为：' , i)
    for e in range(1,5) :
        #print('十位数为：' , e)
        for w in range (1,5):
            #print('个位数为: ' , w)
            #print(i,e,w)
            if ((i != e) and (i != w) and (e != w) ) :
                print(i, e ,w)
                cnt = cnt + 1
print('cnt :',cnt)

           
           # if(i != e) : # 百位和 十位不重复
            #    if(i != w) :# 百位 和 个位不重复
             #       if(e != w) :
              #          print(i, e ,w) 
               

