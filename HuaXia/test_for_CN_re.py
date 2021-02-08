import re

'''
python 3.7版本
正则匹配中文，固定形式：\u4E00-\u9FA5
'''

words = '11月1日'
regex_str = ".*?([\u4E00-\u9FA5])"
match_obj = re.match(regex_str, words)
if match_obj:
    print(match_obj.group(0))
text = re.sub('[\u4E00-\u9FA5]', ' ', words[:-1]).split(' ')
#text1 = text.split(' ')
print(text)