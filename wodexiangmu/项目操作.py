import 项目
while True:
    项目.fuwu()
    user=input("请选择你要操作的功能： ")
    if user == "1":
        项目.cjian()
    elif user == "2":
        项目.cha()
    elif user == "3":
        项目.czhi()
    elif user == "4":
        项目.quyu()
    elif user == "5":
        项目.xufei()
    elif user == "6":
        项目.zhuxiao()
    elif user == "7":
        项目.tuichu()
        break
    else:
        print("不存在此选项，请重试")

