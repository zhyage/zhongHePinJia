# -*- coding: utf-8 -*-
from scipy import *
import xdrlib
import sys
import xlrd
from xlrd import open_workbook, cellname
import numpy as np
#from importSheetData import *
import os
import os.path

sys.path.append("")

from commonUtils import RadioSelect
from loadConfig import LoadConfigFile
from importSheetData import ImportSheet
from executeFunction import executeFunction


class sheetData:

    def __init__(self):
        self.sheetFileName = ''
        self.sheetName = ''
        self.sheetRowNum = 0
        self.sheetColNum = 0
        self.rowNameList = []
        self.colNameList = []
        self.sheetAngle = 0

    def GenerateSheetNarray(self, angle):
        if(angle == 0):
            self.sheetNarray = np.zeros(
                (self.sheetRowNum, self.sheetColNum), float32) #原始数据
            self.sheetWuLiangNarray = np.zeros(
                (self.sheetRowNum, self.sheetColNum), float32) #无量纲化后的数据存储矩阵
        else:
            self.sheetNarray = np.zeros(
                (self.sheetColNum, self.sheetRowNum), float32) #原始数据
            self.sheetWuLiangNarray = np.zeros(
                (self.sheetColNum, self.sheetRowNum), float32) #无量纲化后的数据存储矩阵

    def AssignedDataToMatrix(self, x, y, value):
        self.sheetNarray[x, y] = value #原始数据

    def AssignedDataToWuLiangMatrix(self, x, y, value):
        self.WuLiangNarray[x, y] = value #无量纲化后的数据


    def GetSheetMatrix(self):
        #matrix = self.sheetNarray[0:self.sheetRowNum, 0:self.sheetColNum]
        return self.sheetNarray

    def ShowSheetMatrix(self):
        print "----------sheet matrix-------------"
        print self.GetSheetMatrix()


def main():

    sheet = sheetData()
    sheet = ImportSheet("t3.xls", sheet)
    sheet.ShowSheetMatrix()
    configFile = LoadConfigFile(sheet)
    executeFunction(sheet, configFile)


if __name__ == "__main__":
    main()
