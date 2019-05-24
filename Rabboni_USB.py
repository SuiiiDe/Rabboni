from rabboni import *

rabbo = Rabboni(mode = "USB") #先宣告一個物件

rabbo.connect()#連結上rabboni，若沒插上會報錯

print ("Status:",rabbo.Status)
try:
    rabbo.read_data()
    while True:#一直打印資料 直到結束程式
        rabbo.print_data()#print資料
        print (rabbo.data_num)
        if rabbo.Cnt > 10:
            rabbo.rst_count() #重置count 會delay一下
        if rabbo.data_num>100:
            rabbo.stop()#停止運作
            break

except KeyboardInterrupt:#結束程式
    print('Shut done!')
    # print (rabbo.Accx_list)#印出到結束程式時的所有Accx值
    rabbo.stop()#停止運作
