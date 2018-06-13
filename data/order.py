import datetime
import tushare
import pandas
import time

import common.file
import data.stock

__all__ = ['get_all_order', 'get_order']
order_root = 'order\\'


def get_all_order(code, update_time=-1, retry_time=-1):
    begin_date = datetime.datetime.strptime(
        str(data.stock.get_all().loc[code].timeToMarket), '%Y%m%d').date()
    end_date = datetime.date.today()

    date = begin_date
    df = pandas.DataFrame()
    holiday = tushare.trade_cal()
    holiday = holiday[holiday.isOpen == 0]['calendarDate'].values

    retry_count=0

    while date != end_date:
        if date.isoweekday() in [6, 7] or datetime.datetime.strftime(date, '%Y-%m-%d') in holiday:
            date = date+datetime.timedelta(1)
            continue
        
        try:
            get_order(code, date, update_time, 0.6)
            #df = df.append(get_order(code, date, update_time, 0.1), ignore_index=True)
            print(code+'/'+datetime.datetime.strftime(date, '%Y-%m-%d'))
            retry_count=0
            date = date+datetime.timedelta(1)
        except Exception as e:
            print(e)
            print(date)
            print(retry_count)
            if retry_time>=0 and retry_count>=retry_time:
                time.sleep(600)
            retry_count=retry_count+1
    return df


def get_order(code, date, update_time=-1, sleep=0):
    date_str = date.strftime('%Y%m%d')
    data_file = order_root+code+'\\'+date_str
    date_query = date.strftime('%Y-%m-%d')
    if date == datetime.date.today():
        # TODO
        return None

    df = common.file.file2df(data_file, update_time)
    if (df is None):
        df = tushare.get_tick_data(code, date=date_query, retry_count=1, pause=sleep)
        df=df.assign(date=lambda _: date_str)
        common.file.df2file(df, data_file) 
    #TODO： 判断停盘正确方法
    if df.index.size>0 and str(df.iat[0,2]) == 'nan':
        df.drop(df.index, inplace=True)
    return df
