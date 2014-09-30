# -*- coding:utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("")

from commonUtils import RadioSelect
from commonUtils import isNum
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv


def BiaoZhunZhi_FenWeiShuFa_Prompt_function(sheet):
    result = True
    returnArgList = []
    matrix = sheet.sheetNarray
    maxFenWeiShu = sheet.sheetNarray.shape[1]
    print "ZhengZhiBiao or NiZhiBiao ?"
    print "0 ZhengZhiBiao"
    print "1 NiZhiBiao"
    ZhengZhiBiaoRes = raw_input("please select :")
    if ZhengZhiBiaoRes.strip() != '0' and ZhengZhiBiaoRes.strip() != '1':
        print "invalid ZhengZhiBiao NiZhiBIao option"
        return False, returnArgList
    print "FenWeiShu type ?"
    print "0 FenWeiShuNum type"
    print "1 FenWeiShuPercent type"
    FenWeiShuTypeRes = raw_input("please select :")
    if FenWeiShuTypeRes.strip() != '0' and FenWeiShuTypeRes.strip() != '1':
        print "invalid FenWeiShu type"
        return False, returnArgList
    if '0' == FenWeiShuTypeRes.strip():
        FenWeiShu = raw_input("please input FenWeiShu Num :")
        if False == isNum(FenWeiShu):
            return False, []
        FenWeiShuDig = int(FenWeiShu.strip())
        if FenWeiShuDig < 0 or FenWeiShuDig >= maxFenWeiShu:
            print "invalid FenWeiShu Num"
            return False, returnArgList
    else:
        FenWeiShu = raw_input("please input FenWeiShu Precent :")
        if False == isNum(FenWeiShu):
            return False, []
        FenWeiShuDig = int(FenWeiShu.strip())
        if FenWeiShuDig < 0 or FenWeiShuDig > 100:
            print "invalid FenWeiShu Precent"
            return False, returnArgList

    returnArgList.append(ZhengZhiBiaoRes.strip())
    returnArgList.append(FenWeiShuTypeRes.strip())
    returnArgList.append(FenWeiShu.strip())

    return True, returnArgList


# def BiaoZhunZhi_FenWeiShuFa(matrix, arrayNum, ZhengZhiBiao,
# FenWenShuType, FenWeiShu):
def BiaoZhunZhi_FenWeiShuFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_FenWeiShuFa"
    ZhengZhiBiao = argsList[0]
    FenWeiShuType = argsList[1]
    FenWeiShu = argsList[2]
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    biaoZhunZhi = 0.0
    # print lineArr

    if FenWeiShuType == '0':  # 序号
        if ZhengZhiBiao == '0':  # 正指标
            biaoZhunZhi = lineArr[int(FenWeiShu)]
        else:  # 逆指标
            biaoZhunZhi = lineArr[(len(lineArr) - 1) - int(FenWeiShu)]
    else:  # 百分比
        realFenWeiShu = round(((len(lineArr) - 1) * int(FenWeiShu)) / 100.0)
        if ZhengZhiBiao == '0':  # 正指标
            biaoZhunZhi = lineArr[realFenWeiShu]
        else:  # 逆指标
            biaoZhunZhi = lineArr[(len(lineArr) - 1) - realFenWeiShu]

    guangYiZhiShuFaWuLiangGangHuaConv(lineArr, wuLiangLineArr, biaoZhunZhi, ZhengZhiBiao)
