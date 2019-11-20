import pandas as pd
import numpy as np

from fbprophet import Prophet
from matplotlib.dates import MonthLocator, num2date
from matplotlib.ticker import FuncFormatter

# def prep_store_data(df):
#     # parse the date column and set it as the index
#     fmt = '%a, %d %b %Y %H:%M:%S %Z'
#     df.sale_date = pd.to_datetime(df.sale_date, format=fmt)
#     df = df.sort_values(by='sale_date').set_index('sale_date')

#     # add some time components as features
#     df['month'] = df.index.strftime('%m-%b')
#     df['weekday'] = df.index.strftime('%w-%a')

#     # derive the total sales
#     df['sales_total'] = df.sale_amount * df.item_price
    
#     return df

# def get_sales_by_day(df):
#     sales_by_day = df.resample('D')[['sales_total']].sum()
#     sales_by_day['diff_with_last_day'] = sales_by_day.sales_total.diff()
#     return sales_by_day

# def get_fitbit_data(df):
#     df1 = pd.read_csv('2018-04-26_and_2018-05-26.csv', nrows=31)
#     df2 = pd.read_csv('2018-05-27_and_2018-06-26.csv', nrows=31)
#     df3 = pd.read_csv('2018-06-27_and_2018-07-27.csv', nrows=31)
#     df4 = pd.read_csv('2018-07-28_and_2018-08-26.csv', nrows=30)
#     df5 = pd.read_csv('2018-08-27_and_2018-09-26.csv', nrows=31)
#     df6 = pd.read_csv('2018-09-27_and_2018-10-27.csv', nrows=31)
#     df7 = pd.read_csv('2018-10-28_and-2018-11-27.csv', nrows=31)
#     df8 = pd.read_csv('2018-11-28_and_2018-12-28.csv', nrows=9)
#     df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], join="inner", ignore_index=True)
#     return df

def prepare_fitbit_data(df):
    df = df.rename(columns = {'Date':'date', 'Calories Burned':'calories_burned', 'Steps':'steps', 'Distance':'distance', 'Floors':'floors', 'Minutes Sedentary':'minutes_sedentary', 'Minutes Lightly Active':'minutes_lightly_active', 'Minutes Fairly Active':'minutes_fairly_active', 'Minutes Very Active':'minutes_very_active', 'Activity Calories':'activity_calories'})
    
    df.calories_burned = df.calories_burned.astype(str)
    df.calories_burned = df.calories_burned.str.replace(',', '').astype(float)

    df.minutes_sedentary = df.minutes_sedentary.astype(str)
    df.minutes_sedentary = df.minutes_sedentary.str.replace(',', '').astype(float)

    df.activity_calories = df.activity_calories.astype(str)
    df.activity_calories = df.activity_calories.str.replace(',', '').astype(float)

    df.steps = df.steps.astype(str)
    df.steps = df.steps.str.replace(',', '').astype(float)

    return df

def prepare_calories_burned_prophet(df):
    df1 = df[['date', 'calories_burned']]
    df1.columns = ['ds', 'y']

    df1.ds = pd.to_datetime(df1.ds)

    m = Prophet()

    m.fit(df1)

    #Create a placeholder dataframe

    future1 = m.make_future_dataframe(periods=14)

    forecast1 = m.predict(future1)
    
    return df1, future1, forecast1

def prepare_steps_prophet(df):
    df2 = df[['date', 'steps']]
    df2.columns = ['ds', 'y']

    df2.ds = pd.to_datetime(df2.ds)

    m = Prophet()

    m.fit(df2)

    #Create a placeholder dataframe

    future2 = m.make_future_dataframe(periods=14)

    forecast2 = m.predict(future2)
    
    return df2, future2, forecast2

def prepare_distance_prophet(df):
    df3 = df[['date', 'distance']]
    df3.columns = ['ds', 'y']

    df3.ds = pd.to_datetime(df3.ds)

    m = Prophet()

    m.fit(df3)

    #Create a placeholder dataframe

    future3 = m.make_future_dataframe(periods=14)

    forecast3 = m.predict(future3)
    
    return df3, future3, forecast3

def prepare_floors_prophet(df):
    df4 = df[['date', 'floors']]
    df4.columns = ['ds', 'y']

    df4.ds = pd.to_datetime(df4.ds)

    m = Prophet()

    m.fit(df4)

    #Create a placeholder dataframe

    future4 = m.make_future_dataframe(periods=14)

    forecast4 = m.predict(future4)
    
    return df4, future4, forecast4

def prepare_minutes_sedentary_prophet(df):
    df5 = df[['date', 'minutes_sedentary']]
    df5.columns = ['ds', 'y']

    df5.ds = pd.to_datetime(df5.ds)

    m = Prophet()

    m.fit(df5)

    #Create a placeholder dataframe

    future5 = m.make_future_dataframe(periods=14)

    forecast5 = m.predict(future5)
    
    return df5, future5, forecast5

def prepare_minutes_lightly_active_prophet(df):
    df6 = df[['date', 'minutes_lightly_active']]
    df6.columns = ['ds', 'y']

    df6.ds = pd.to_datetime(df6.ds)

    m = Prophet()

    m.fit(df6)

    #Create a placeholder dataframe

    future6 = m.make_future_dataframe(periods=14)

    forecast6 = m.predict(future6)
    
    return df6, future6, forecast6

def prepare_minutes_fairly_active_prophet(df):
    df7 = df[['date', 'minutes_fairly_active']]
    df7.columns = ['ds', 'y']

    df7.ds = pd.to_datetime(df7.ds)

    m = Prophet()

    m.fit(df7)

    #Create a placeholder dataframe

    future7 = m.make_future_dataframe(periods=14)

    forecast7 = m.predict(future7)
    
    return df7, future7, forecast7

def prepare_minutes_very_active_prophet(df):
    df8 = df[['date', 'minutes_very_active']]
    df8.columns = ['ds', 'y']

    df8.ds = pd.to_datetime(df8.ds)

    m = Prophet()

    m.fit(df8)

    #Create a placeholder dataframe

    future8 = m.make_future_dataframe(periods=14)

    forecast8 = m.predict(future8)
    
    return df8, future8, forecast8

def prepare_activity_calories_prophet(df):
    df9 = df[['date', 'activity_calories']]
    df9.columns = ['ds', 'y']

    df9.ds = pd.to_datetime(df9.ds)

    m = Prophet()

    m.fit(df9)

    #Create a placeholder dataframe

    future9 = m.make_future_dataframe(periods=14)

    forecast9 = m.predict(future9)
    
    return df9, future9, forecast9