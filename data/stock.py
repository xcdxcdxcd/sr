import pandas
import tushare
import common.file


__all__=['get_all']
data_file='fundmental\\stock_list'

def get_all(update_time=-1):
    df=common.file.file2df(data_file, update_time)
    if (df is None):
        df=tushare.get_stock_basics()
        common.file.df2file(df, data_file)
    return df

def get_industry():
    return None
