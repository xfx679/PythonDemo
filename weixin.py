from wxpy import *

# 初始化一个对象，就相当于拿到了这个人的微信
#生成网页版的二维码
bot = Bot()
friends = bot.friends()
print(friends)
