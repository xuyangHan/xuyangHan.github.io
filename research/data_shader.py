import datashader as ds, pandas as pd
import datashader.transfer_functions as tf
import os

csv_dir = r'C:\Users\62707\Downloads\AIS_ASCII_by_UTM_Month\2017_v2\AIS_ASCII_by_UTM_Month\2017_v2'
os.chdir(csv_dir)

df = pd.read_csv('AIS_2017_01.csv', usecols=['LON', 'LAT'])
print(df.info(memory_usage='deep'))

cvs = ds.Canvas(plot_width=400, plot_height=400)
agg = cvs.points(df, 'LON', 'LAT')
img = tf.shade(agg, cmap=['lightblue', 'darkblue'], how='log')

ds.utils.export_image(img, "pic")
