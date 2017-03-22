# coding=utf-8
# https://github.com/tesseract-ocr
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
try:
    from pyocr import pyocr
    from PIL import Image
    import pyocr.builders
except ImportError:
    print('模块导入错误,请使用pip安装,pytesseract依赖以下库：')
    print('http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil')
    print('http://code.google.com/p/tesseract-ocr/')
    raise SystemExit
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
print("Using '%s'" % (tools[0].get_name()))
print('a')
# tools[0].image_to_string(Image.open('D:\\123.png'), lang='eng')
print(tools[0].image_to_string(Image.open('/Users/zhangmimi/Desktop/CheckCodeCaptcha'), lang='eng'))
# print tools[0].image_to_string(Image.open('D:\\3535.png'),lang='chi_sim')
