'''
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
'''
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)

import pickle

d = dict(name='Bob', age=20, score=88)
e = pickle.dumps(d)
print(e)

f = open('/Users/leonard_tia/PycharmProjects/py36/a', 'wb')
pickle.dump(d, f)
f.close()

f = open('/Users/leonard_tia/PycharmProjects/py36/a', 'rb')
d = pickle.load(f)
f.close()
print(d)

j = json.dumps(d)
print(j)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
jj = json.loads(json_str)
print(jj)
