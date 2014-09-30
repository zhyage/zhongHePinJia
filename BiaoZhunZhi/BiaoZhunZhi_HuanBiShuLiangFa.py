# -*- coding:utf-8 -*-
from scipy import *
import numpy as np
from commonUtils import isInt
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt

def BiaoZhunZhi_HuanBiShuLiangFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_HuanBiShuLiangFa"
    zhengZhiBiao = argsList[0]
    huanBiLine = argsList[1]
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    huanBiArr = matrix[huanBiLine, :]
    biaoZhunZhi = 0.0
    print "huanbiLine"
    print huanBiArr

    if '0' == zhengZhiBiao:
        for i in range(0, lineArr.size):
            wuLiangLineArr[i] = lineArr[i] / huanBiArr[i]
    else:
        for i in range(0, lineArr.size):
            wuLiangLineArr[i] = huanBiArr[i] / lineArr[i]


def BiaoZhunZhi_HuanBiShuLiangFa_Prompt_function(sheet):
    result = True
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
    else:
        return False, []
    maxLine = sheet.sheetNarray.shape[0]
    tipList = []
    for i in range(0, maxLine):
        ss = str(i) + " line " + str(i)
        tipList.append(ss)

    print "please input HuanBi Line :"
    for tip in tipList:
        print tip
    huanBiLine = raw_input("please select :")
    if False == isInt(huanBiLine):
        return False, []
    if int(huanBiLine) < 0 or int(huanBiLine) >= maxLine:
        return False, []

    returnArgList.append(huanBiLine.strip())
    return True, returnArgList
