import re
import pickle
import codecs
import jieba
'''
读取原始数据
'''

def txt_load(path):
    reader = codecs.open(path,'r','UTF-8')
    lines = reader.readlines()
    return lines

def join_list(ss):
    c = ""
    for k in ss:
        c+=k
    return c


def pickle_writer(input_,name):
    '''

    :param input_: 待保存的数据
    :param name:  存放路径
    :return:  None
    '''
    writer = open(name,"wb")
    pickle.dump(input_,writer)
    writer.close()
    print("finish to write data")

# 定义读plk文件函数
def pickle_load(input_):
    '''

    :param input_: 路径
    :return:  原始数据
    '''
    raeder = open(input_,"rb")
    content = pickle.load(raeder)
    raeder.close()
    print("finish to read data")
    return content


def jieba_cut(content):
    '''

    :param content: str 句子 待分词
    :return: 分好词的list
    '''
    cut = jieba.cut(content)
    l = []
    for con in cut:
        if con!=" ":
            l.append(con)
    return l

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return uchar
    elif uchar == re.sub('[^a-zA-Z]', '', uchar):
        return str(uchar).lower()
    else:
        return ''





