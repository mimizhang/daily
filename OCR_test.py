from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[2]
print("Will use lang '%s'" % (lang))

# TextBuilder用法
txt = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/creditquery!getValidateImg.jpeg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print(txt)
# 输出的结果为字符串
# txt is a Python string

# WordBoxBuilder用法
word_boxes = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/creditquery!getValidateImg.jpeg'),
    lang=lang,
    builder=pyocr.builders.WordBoxBuilder()
)
for elem in word_boxes:
    print(elem.content, elem.position)
# 返回的是一个list,list中的每个元素为box objects,box objects中存着box.content内容和每个词的位置box.position
# # list of box objects. For each box object:
# #   box.content is the word in the box
# #   box.position is its position on the page (in pixels)
# #
# # Beware that some OCR tools (Tesseract for instance)
# # may return empty boxes

# LineBoxBuilder用法
line_and_word_boxes = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/creditquery!getValidateImg.jpeg'),
    lang=lang,
    builder=pyocr.builders.LineBoxBuilder()
)
# line_and_word_boxes也是list,list中的每个line objects有line.word_boxes(结构和box
# objects相同),line.content(每一行的内容)和位置line.position
print(len(line_and_word_boxes))
for line in line_and_word_boxes:
    for word in line.word_boxes:
        print(word.content, word.position)
    print(line.content, line.position)
# # list of line objects. For each line object:
# #   line.word_boxes is a list of word boxes (the individual words in the line)
# #   line.content is the whole text of the line
# #   line.position is the position of the whole line on the page (in pixels)
# #
# # Beware that some OCR tools (Tesseract for instance)
# # may return empty boxes
# 识别数字
# Digits - Only Tesseract (not 'libtesseract' yet !)
digits = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/creditquery!getValidateImg.jpeg'),
    lang=lang,
    builder=pyocr.builders.DigitBuilder(),
)

print(digits.replace(' ', ''))
# digits is a python string
