#-*- coding:utf-8 -*-
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv


def BiaoZhunZhi_JiZhiHuaFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_JiZhiHuaFa"
    ZhengZhiBiao = argsList[0]
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    # print lineArr
    biaoZhunZhi = 0.0

    if ZhengZhiBiao == '0':  # 正指标
        biaoZhunZhi = np.max(lineArr)
    else:
        biaoZhunZhi = np.min(lineArr)

    guangYiZhiShuFaWuLiangGangHuaConv(lineArr, wuLiangLineArr, biaoZhunZhi, ZhengZhiBiao)


def BiaoZhunZhi_JiZhiHuaFa_Prompt_function(sheet):
    result = True
    returnArgList = []
    print "ZhengZhiBiao or NiZhiBiao ?"
    print "0 ZhengZhiBiao"
    print "1 NiZhiBiao"
    ZhengZhiBiaoRes = raw_input("please select :")
    if ZhengZhiBiaoRes.strip() != '0' and ZhengZhiBiaoRes.strip() != '1':
        print "invalid ZhengZhiBiao NiZhiBIao option"
        return False, returnArgList

    returnArgList.append(ZhengZhiBiaoRes.strip())
    return True, returnArgList
