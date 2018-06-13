
import common.file
import pandas
"""
print(common.file.json2df('123\\425336',10))
common.file.df2json(pandas.DataFrame(), '123\\425336')
print(common.file.json2df('123\\425336',10))


print(ts.get_tick_data('600848',date='2014-01-09'))
"""


"""
import data.order
print(data.order.get_order('600848','2018-05-30'))
print(data.order.get_all_order('600848'))
"""

import tushare as ts
import data.order
import datetime 
#print(data.order.get_all_order('600848'))
#print(ts.get_stock_basics().dtypes)
import json
"""
a=data.stock.get_all().dtypes
#print(data.stock.get_all())
json_str = json.dumps(a)
print(json_str)"""
import numpy
import os
'''
a=ts.get_stock_basics()
print(a.dtypes)
print(type(a.dtypes))

b=a.dtypes.to_dict()
print(type(b['name'].name))
print(type(b['name']).name)

a.dtypes.to_csv('test.csv')
b=pandas.read_csv('file:\\'+os.path.abspath('test.csv'))

print(b)


print(a.dtypes.to_json())
print(b.to_json())
print(a.dtypes.to_json()==b.to_json())
print(b)
dt=numpy.dtype('float64')
print(dt)
'''
'''
c=ts.get_stock_basics()
#print(type(c.dtypes['name']))
print(type(c.dtypes.to_dict()['name']))

type_dict=c.dtypes.to_dict()
for pair in type_dict:
    print(pair)
'''


#print(data.order.get_order('600048'),)
all_list=data.stock.get_all()
index=all_list.index
length=index.size
exist=['000606','002607','002681','002813','002886','002903','300247','300390','300505','300549','300615','300647','300679','300687','300746','600666','601138','603776','603890','002364','002622','002782','002849','002897','300235','300249','300490','300508','300565','300638','300663','300686','300745','600645','600960','603486','603829']
for i in range(length):
    if index[i] in exist or int(index[i]) % 10==0: 
        data.order.get_all_order(index[i], retry_time=10)

'''
a=data.stock.get_all()
a=a.set_index('code')
b=a.index
print(a)
'''
