#计算这个矩阵的对角线[[3，8，9], [6，11，2], [7，18，5]]

#编写输入任意一张银行卡号，输出银行卡号的前6位和后4位，剩下的所有数字用星号（*）表示
	#如：card("5189301239921331") -> 518930******1331

# card=input("请输入银行银行卡卡号:")
# a=card[7:-4].replace(card[7:-4],"*")
# b=card[0:6]
# c=card[-4:]
# def yinhangka(card):
#     if isinstance(card,str) and
#         a = card[0:6]
#         b = "*"*(len(card)-10)
#         c = card[-4:]
#         return a,b,c
# card = input("请输入银行银行卡卡号:")
#
# m=yinhangka(card)
# print(m)

#打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d" % (j,i,i*j),end="" )
#     print( )
class Person():
    # def __init__(self,name,age,hobby="吹牛"):
    #     self.name=name
    #     self.age=age
    #     self.hobby=hobby
    def run(self,name,age,hobby):
        print("%s今年%d岁爱好是%s" % (name,age,hobby))

m=Person()
m.run("徐萌",27,"打篮球")












