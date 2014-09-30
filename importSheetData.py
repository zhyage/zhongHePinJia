# -*- coding: utf-8 -*-
from scipy import *
import xdrlib
import sys
import xlrd
from xlrd import open_workbook, cellname
import numpy as np

sys.path.append("")

from commonUtils import RadioSelect



def ImportSheet(xlsFileName, sheetInstance):
    #sheetInstance = sheetData()
    sheetInstance.sheetFileName = xlsFileName

    book = open_workbook(xlsFileName, on_demand=True)
    sheet = book.sheet_by_index(0)
    sheetInstance.sheetRowNum = sheet.nrows - 1
    sheetInstance.sheetColNum = sheet.ncols - 1
    sheetInstance.SheetName = book.sheet_names()

    sheet = book.sheet_by_index(0)
    if(sheet.nrows != 0 and sheet.ncols != 0):
        sheetInstance.rowNameList = sheet.row_values(0)
        sheetInstance.colNameList = sheet.col_values(0)

    
    # print "please select Sheet's angle "
    # # angleStr = "please input " + sheetInstance.sheetName + \
    # #     "'s angle 0: ZhongXiang, 1: HengXiang"
    # print "0: ZhongXiang"
    # print "1: HengXiang"    
    # angleStr = "please input " + sheetInstance.sheetName + "'s angle :"    
    # angle = raw_input(angleStr.encode('utf-8'))
    # if('0' != angle and '1' != angle):
    #     print "only accept 0 or 1, exit"
    #     exit()

    tipList = ["please select sheet's angle :\n",
               "0: ZhongXiang\n"
               "1: HengXiang\n"
               "please input your select :"]

    maxOptions = 2

    angle = RadioSelect(tipList, maxOptions)    


    if(0 == angle):  # 竖向
        sheetInstance.sheetAngle = 0
    else:
        sheetInstance.sheetAngle = 1

    sheetInstance.GenerateSheetNarray(sheetInstance.sheetAngle)

    sheet = book.sheet_by_index(0)
    if(sheetInstance.sheetAngle == 0):
        for rowIndex in range(1, sheet.nrows):
            for colIndex in range(1, sheet.ncols):
                # print sheet.cell(rowIndex, colIndex).value
                value = sheet.cell(rowIndex, colIndex).value
                sheetInstance.AssignedDataToMatrix(
                    rowIndex - 1, colIndex - 1, value)
    else:
        for colIndex in range(1, sheet.ncols):
            for rowIndex in range(1, sheet.nrows):
                value = sheet.cell(rowIndex, colIndex).value
                sheetInstance.AssignedDataToMatrix(
                    colIndex - 1, rowIndex - 1, value)

    return sheetInstance


def ShowImportSheet():
    print "no data"
