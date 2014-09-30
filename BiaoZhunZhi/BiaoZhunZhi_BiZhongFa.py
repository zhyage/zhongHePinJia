# -*- coding:utf-8 -*-
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt


def BiaoZhunZhi_BiZhongFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_BiZhongFa"
    zhengZhiBiao = argsList[0]
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    biaoZhunZhi = np.sum(lineArr)
    guangYiZhiShuFaWuLiangGangHuaConv(
        lineArr, wuLiangLineArr, biaoZhunZhi, zhengZhiBiao)


def BiaoZhunZhi_BiZhongFa_Prompt_function(sheet):
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
        return True, returnArgList
    else:
        return False, []
