

import mingpian1
while True:
    mingpian1.ystemMean()
    user=int(input("请输入你要选择的类型对应数字就是： "))
    print('*'*30)
    if user==1:
        mingpian1.xinjian()
    elif user==2:
        mingpian1.xianshi()
    elif user==3:
        mingpian1.chaxun()
    elif user==4:
        mingpian1.xiugai()
    elif user==5:
        mingpian1.shanchu()
    else:
        mingpian1.exit()
        break

