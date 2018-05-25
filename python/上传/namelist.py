
name_list = []
while True:
    tong_xue_name = input("请输入你要保存的姓名： ")
    if tong_xue_name == "t":
        break
    name_list.append(tong_xue_name)
    print(name_list)
print(name_list[3])
print(name_list[5])
print(name_list[8])
print(name_list[10])
name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
print("长度是",len(name_list))
#len(name_list)
print("最后一位同学是:%s "% name_list.pop())
print(name_list)
shu=input("请输入要并接的东西：")
name_list.extend(shu)
print(name_list)
print("小明的下标是",name_list.index("小明"))
#print(name_list.index("小明"))


'''
             #key  ：value  输出key就可以得到value
wangxuewen={'name':'王学文',
            'sex':'男',
            'com':"百度科技有限公司",
            'phone':'17535209561',}
wang2   =  {'name':'王2',
            'sex':'男',
            'com':'阿里云科技有限公司',
            'phone':'12636362771',}
longs=int(input('请输入你的身高：'))
wangxuewen['longss']=longs
long2=int(input('请输入你的身高：'))
wang2['long2']=long2
list_mingpian = []#list的初始值
list_mingpian.append(wangxuewen)#把上面的wangxuewen放进list初始值里面
list_mingpian.append(wang2)
print(list_mingpian)
'''
