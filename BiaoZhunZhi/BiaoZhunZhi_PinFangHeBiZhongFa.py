#-*- coding:utf-8 -*-
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt


def BiaoZhunZhi_PinFangHeBiZhongFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_PinFangHeBiZhongFa"
    biaoZhunZhi = 0.0
    zhengZhiBiao = argsList[0]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    lineArr = matrix[arrayNum, :]

    tmp = np.sum(lineArr ** 2)
    biaoZhunZhi = np.sqrt(tmp)
    guangYiZhiShuFaWuLiangGangHuaConv(
        lineArr, wuLiangLineArr, biaoZhunZhi, zhengZhiBiao)


def BiaoZhunZhi_PinFangHeBiZhongFa_Prompt_function(sheet):
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
        return True, returnArgList
    else:
        return False, []
