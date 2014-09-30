#-*- coding:utf-8 -*-
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt


def BiaoZhunZhi_JunZhiFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_JunZhiFa"
    biaoZhunZhi = 0.0
    zhengZhiBiao = argsList[0]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    lineArr = matrix[arrayNum, :]

    biaoZhunZhi = np.mean(lineArr)
    # k = x/b, x = k * b
    # for i in range(0, lineArr.size):
    #     wuLiangLineArr[i] = lineArr[i] * biaoZhunZhi
    guangYiZhiShuFaWuLiangGangHuaConv(
        lineArr, wuLiangLineArr, biaoZhunZhi, zhengZhiBiao)

    # print lineArr
    # print wuLiangLineArr
    # print "------------------------"


def BiaoZhunZhi_JunZhiFa_Prompt_function(sheet):
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
        return True, returnArgList
    else:
        return False, []
