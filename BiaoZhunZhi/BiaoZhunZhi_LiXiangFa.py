# -*- coding:utf-8 -*-

import sys
sys.path.append("../")
sys.path.append("")
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt

from commonUtils import *


def BiaoZhunZhi_LiXiangFa(matrix, wuLiangMatrix, arrayNum, argsList):
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    zhengZhiBiao = argsList[0]
    biaoZhunZhi = float32(argsList[1])
    guangYiZhiShuFaWuLiangGangHuaConv(
        lineArr, wuLiangLineArr, biaoZhunZhi, zhengZhiBiao)


def BiaoZhunZhi_LiXiangFa_Prompt_function(sheet):
    result = True
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
    else:
        return False, []
    LiXiangZhiRes = raw_input("please input LiXiangZhi :")

    if False == isNum(LiXiangZhiRes):
        print "invalid LiXiangZhi"
        return False, returnArgList

    returnArgList.append(LiXiangZhiRes.strip())
    return True, returnArgList
