import random

## 

print('猜数字游戏')
n = random.randint(0,100)

while True:
    ni =int(input('请输入要猜的数字： '))
    if ni >n:
        print('猜大了，请继续')
    elif ni < n :
        print('猜小了，请继续')
    else:
        print('恭喜猜对了')
        break
