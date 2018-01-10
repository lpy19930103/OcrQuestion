# -*- coding: utf-8 -*-

from aip import AipOcr
import screenshot
import webbrowser
import re
import urllib.parse

# 百度OCR API
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 截图
screenshot.check_screenshot()


def get_file(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file("./screenshot.png")

""" 调用通用文字识别（高精度版） """
result = client.basicAccurate(image);
words = result['words_result']
for word in words:
    matchData = re.match(r'^(\d\.)(.*\?+)', word['words'])
    if matchData:
        print(matchData.group(2))
        parseresult = urllib.parse.quote(matchData.group(2))
        print(parseresult)
        webbrowser.open('https://baidu.com/s?wd=' + parseresult)
