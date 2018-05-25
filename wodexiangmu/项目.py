money={'您的余额为':0}
def fuwu():
    print("<"*30)#主要功能
    print("欢迎进入（玩-的-嗨）网咖操作系统^_^")
    print("1.创建本网吧的账户")
    print("2.查看您创建的帐号")
    print("3.充值上网金额")
    print("4.选择vip区域和普通区域")
    print("5.续费")
    print("6.注销")
    print("7.退出")
    print(">"*30)
list_o=[]
dicw={'帐号':"a",'密码':'b'}#创建一个空的字典 下面的操作可以认识帐号
def cjian():
    print("创建账户")
    x=input("请输入您要创建的帐号: ")
    dicw['帐号']=x#把帐号添加到上面的字典里面
    y=input("请输入您要保存的密码: ")
    dicw['密码']=y
    dic = {'帐号':x,
           '密码':y}
    list_o.append(dic)
    for i in list_o:
        for x,y in i.items():
            print(x,y)
    print("创建成功")
def cha():#创建一个查看函数
    print("=========查看您在本网把创建的帐号=========")
    for i in list_o:
        for x,y in i.items():#获得所有字典中的所有元素，给出一个列表
            print(x,y)
def czhi():#创建一个充值的函数
    print("充值")
    jine=float(input("请输入你要充值的上网金额：  "))
    money['您的余额为']=money["您的余额为"]+jine#总金额=总金额加上你要输入的那个数字
    print("充值成功  您的余额为:%.2f"%money['您的余额为'])
def quyu():#创建一个选择区域的函数
    print("选择区域")
    print("会员区4元/时")
    print("普通区2元/时")
    user=int(input("您要上多少钱的网： "))
    money['您的余额为']=money['您的余额为']-user#总金额=总金额-输入的哪个金额同上
    if user > money['您的余额为']:
        print('您的余额不足，请充值')
        czhi()#调用了一下上面的那个函数
    else:
        print('您的余额为： %d元'%money['您的余额为'])#余额够用，先是一下余额
    a1=user/4
    print("您可以在会员区上%.1f小时的网"%a1)
    b2=user/2#进行了一次除法运算
    print("您可以在普通区上%.1f小时的网"%b2)#打印输出除法的那个结果
    xuan=input("你要在哪个区域上网 a--会员区 | b--普通区: ")
    if xuan=='a':
        print("请前往会员区上网")
    elif xuan=='b':
        print("请前往普通区上网")
def xufei():#创建一个续费的函数
    print("续费")
    while True:#用这个循环显示效果
        user12=input("请输入您的账号： ")
        if user12==dicw['帐号']:
            czhi()
            break
        else:#如果不满足上面的那个条件，就返回那个while继续循环
            print("帐号输入错误，请重新输入")
def zhuxiao():#创建一个注销的函数
    print("注销")
    for key in list_o:#通过遍历进行下面的操作
        while True:
            user13=input("请输入您要注销的帐号： ")
            if user13==key['帐号']:
                del key["帐号"]
                del key["密码"]
                print('注销成功')
                break
            else:
                print("帐号输入错误，请重新输入")
def tuichu():#创建一个退出的函数
    print("感谢您的使用")
    print("欢迎您下次再来坑死人网吧～～～")
#主运行在另一个文件夹里，以便于对这两个文件进行修改
