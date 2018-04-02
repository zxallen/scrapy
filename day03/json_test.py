# coding:utf8

import json


# dict_data = '{"this is dict": "这是_dict"}'
# python中支持单引号，但转换数据类型的时候，需要使用双引号
dict_data = '{"this is dict": "这是_dict"}'
print(dict_data)
print(type(dict_data))


print("************************")
# 转成json字符串 默认使用ascii编码，需要设置ensure_ascii为False
# json_data = json.dumps(dict_data, ensure_ascii=False)
# print(json_data)
# print(type(json_data))



dict_data_str = json.loads(dict_data)
# print(dict_data_str)
# print(type(dict_data_str))

# 把字典转成json写入文件,写文件如果遇到编码ascii错误,可以指定编码格式为utf8
# f = open('data.json', 'w', encoding='utf8')
# json.dump(dict_data_str, f, ensure_ascii=False)

# 读取json文件中的内容，转成字典
f = open('data.json', 'r', encoding='utf8')
dict_data = json.load(f)
print(dict_data)