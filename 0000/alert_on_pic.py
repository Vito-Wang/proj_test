# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont


def alert_on_pic(picpath, num):
    im = Image.open(picpath)
    x, y = im.size
    thefont = ImageFont.truetype('arial.ttf', x / 3)
    draw = ImageDraw.Draw(im)
    draw.text((7*x / 12, 0), str(num), font=thefont, fill='red')
    im.save('alert_message.jpg')
    im.show()

if __name__ == '__main__':
    alert_on_pic('C:/Users/wwd/Desktop/funny_baby.jpg', 99)