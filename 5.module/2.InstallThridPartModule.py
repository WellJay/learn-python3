'''
安装第三方模块

    在Python中，安装第三方模块，是通过包管理工具pip完成的。

    如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。

    如果是windows，则要在安装python时候确认勾选了pip和Add python.exe to Path。
    在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。
'''

'''
    现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
    不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。


    pip install Pillow


    耐心等待下载并安装后，就可以使用Pillow了。

    有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
'''
from PIL import Image

im = Image.open('test.png')
print(im.format, im.size, im.mode)
# PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

'''
    其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。
'''
