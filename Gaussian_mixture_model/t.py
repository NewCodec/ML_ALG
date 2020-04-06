# -*- coding: utf-8 -*-

import numpy as np
import openpyxl

def LoadData(xlsxName,data_loaded=[]):
    data_loaded.clear()
    wb = openpyxl.load_workbook(xlsxName)
    sheet = wb['Sheet1']
    for row in sheet.iter_rows():
        data_loaded.append((row[0].value,row[1].value,row[2].value))

class GaussianMixtureModel(object):

    def __init__(self,data,model_num,):
        self.data = data
        self.model_num = model_num
        self.init_args = []
        self.next_args = []
        self.lamda = []
        pass
    def initArgs(self):
        a_v = np.divide(1,self.model_num)
        ainit = (a_v,a_v,a_v)
        uinit = (data[6],data[22],data[27])
        einit = []
    def Caculate_lambda(self):
        pass


learn_num = 3;
data=[]
LoadData('watermelon_datasheet_4_0.xlsx',data)
print(data)
#test = GaussianMixtureModel(data,3,)



