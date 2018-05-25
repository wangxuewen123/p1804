def ystemMean():
    print("*"*30)
    print("欢迎使用名片管理系统")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("4.修改名片")
    print("5.删除名片")
    print("6.退出系统")
    print("*"*30)
list_card=[]
def xinjian():
    print("请新建一个名片")
    name=input("请输入你的姓名: ")
    com=input("请输入公司: ")
    sex=input("请输入性别: ")
    phone=input("请输入电话: ")
    youxiang=input("请输入邮箱: ")
    dic={'姓名':name,
         '公司':com,
         '性别':sex,
         '电话':phone,
         '邮箱':youxiang}
    list_card.append(dic)
    for i in list_card:
        for a in i.items():
            print(a)
def xianshi():
    print("显示所有已创建的名片")
    print(list_card)
def chaxun():
    print("查询名片")
    xinjian=input("请输入你要查询的名字： ")
    for a in list_card:
        if xinjian == a['姓名'] :
            print("姓名: %s"%a['姓名'])
            print("公司: %s"%a["公司"])
            print("电话: %s"%a['电话'])
            print("性别: %s"%a['性别'])
            print("邮箱: %s"%a['邮箱'])
        else:
            print('输入错误')
def xiugai():
    for i in list_card:
        print("修改名片")
        gai1=input("你要修改名片的什么： ")
        gai2=input("请输入你要改得内容： ")
        i[gai1]=gai2
        print("名片修改成功")
        print(list_card)
def shanchu():
    for key in list_card:
        shan1=input("请输入你要删除名片的姓名： ")
        if shan1==key['姓名']:
            key.pop('姓名')
            key.pop('公司')
            key.pop('电话')
            key.pop('邮箱')
            key.pop('性别')
            print('删除成功')
def exit():
    print("成功退出系统退出")


