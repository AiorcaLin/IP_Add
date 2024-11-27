#判断输入的ip地址的类型。A、B、C、D、E

#接收用户输入并储存到变量中
#提示用户进行输入
def Prompt():
    try:
         inp=input('请输入IP地址：')
         if inp=='q':
             print("程序已退出。")
             exit()
         else :
             Ip_Add=inp.split('.')
             ValiFormat()
    except ValueError:
        print("输入无效，请输入一个IP")
        Prompt()

#判断格式ip是否有效
def ValiFormat(IP):
    try:
        if len(IP)==4 and all (part.isdigit() and 0<=int(part)<=255 for part in IP):
        #isdigit()返回 True：如果字符串只包含数字字符（0-9），且字符串非空。
        #for part in ip_parts 是生成器表达式，它依次对列表 ip_parts 中的每个元素执行检查。
        #all() 函数用于检查生成器表达式的所有条件是否都为 True.all([True, True, True, True])  # True
            return list(map(int, IP))
        raise ValueError("无效的IP地址格式")
    #触发异常：raise 用于手动引发一个指定类型的异常。
    # 异常类型可以是 Python 内置的异常（如 ValueError、TypeError 等），也可以是自定义异常。
    # 终止执行流程：当异常被引发时，后续代码不会执行，程序会跳转到异常处理部分（如 except 块）。
    except ValueError as e:
        print(f"错误：{e}")
        return Prompt()

#判断ip类型并返回


#输出ip类型

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #IP_Add=Prompt()
    IP=['100','100','100','100']



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
