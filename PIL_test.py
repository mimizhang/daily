# 打开网络链接图片
from PIL import Image
from io import BytesIO
from urllib.request import urlopen

from requests import get
import pyocr

# http://image.58.com/showphone.aspx?t=v55&v=415A29148D7F206B2B8F5CAE15460728E
# http://image.58.com/showphone.aspx?t=v55&v=41A2DD339188E208XBD3E27EBCAB60748
# http://image.58.com/showphone.aspx?t=v55&v=351B5E297475CF355CAB4AF43F6C0503
url = 'http://image.58.com/showphone.aspx?t=v55&v=33ECF6A227C1420A80E191F3146717743'
# urllib
image_bytes = urlopen(url).read()
# requests
image_bytes = get(url).content
data_stream = BytesIO(image_bytes)
pil_image = Image.open(data_stream)

# 更改尺寸
# pil_image = pil_image.resize((100, 30), Image.ANTIALIAS)


# 二值化
pil_image = pil_image.convert('L')
data = pil_image.getdata()
print(data)
print(pil_image.size)
pil_image.show()

tools = pyocr.get_available_tools()
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[2]
print("Will use lang '%s'" % (lang))
digits = tool.image_to_string(
    pil_image,
    lang=lang,
    builder=pyocr.builders.DigitBuilder(),
)
print(digits.replace(' ', ''))
