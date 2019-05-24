# -*- coding: UTF-8 -*-
from rabboni import *

rabo = Rabboni(mode = "BLE") #先宣告一個物件
rabo.scan() #掃描所有藍芽Device
rabo.print_device() # 列出所有藍芽Device
rabo.connect("D1:FA:F0:F2:12:29")#依照MAC連接
rabo.discover_characteristics()#掃描所有服務 可略過
rabo.print_char()#列出所有服務 可略過
# print (rabo.characteristics)
# print (rabo.Status)
rabo.read_data()#讀取資料 必跑

try:
    while True:#一直打印資料 直到結束程式
        rabo.print_data()#print資料
        if rabo.Cnt == 100:
            rabo.rst_count()
except KeyboardInterrupt:#結束程式
    print('Shut done!')
    print (rabo.Accx_list)#印出到結束程式時的所有Accx值
    rabo.stop()#停止dongle
    rabo.write_csv(data = rabo.Accx_list,file_name ="AccX")#將Accx寫出csv檔
    rabo.plot_pic(data = rabo.Accx_list,file_name = "AccX",show = True)#將Accx畫出圖案並存檔
finally:
    rabo.stop()


