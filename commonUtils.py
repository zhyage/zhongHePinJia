# -*- coding:utf-8 -*-

import os
import os.path
import sys


def RadioSelect(tipList, maxOptions):
    selectNum = -1
    # for tip in tipList[0:-1]:
    #     print tip
    while selectNum not in range(0, maxOptions):
        for tip in tipList[0:-1]:
            print tip
        select = raw_input(tipList[-1])

        if True != isInt(select):
            warningStr = "only options "
            for i in range(0, maxOptions):
                warningStr = warningStr + str(i) + " "
            warningStr = warningStr + " is valid !"
            print '    ' + warningStr
            continue

        selectNum = int(select)
        if (selectNum not in range(0, maxOptions)):
            warningStr = "only options "
            for i in range(0, maxOptions):
                warningStr = warningStr + str(i) + " "
            warningStr = warningStr + " is valid !"
            print '    ' + warningStr

        # if(selectNum not in range(0, maxOptions)):
        #     warningStr = "only options "
        #     for i in range(0, maxOptions):
        #         warningStr = warningStr + str(i) + " "
        #     warningStr = warningStr + " is valid !"
        #     print warningStr

    return selectNum


def FileSelectPrompt(path):
    rootDir = path
    fileNameList = []
    i = 0

    for parent, dirnames, filenames in os.walk(rootDir):
        if parent == ".":
            i = 0
            for filename in filenames:
                fullName = os.path.join(parent, filename)
                if filename[-4:] == '.xml':
                    fileNameList.append(filename)
                    i = i + 1

    selectNum = -1
    while selectNum not in range(0, len(fileNameList)):
        print("please select the file :")
        i = 0
        for filen in fileNameList:
            print str(i) + ": " + filen
            i = i + 1
        select = raw_input("please input your select :")
        selectNum = int(select)
        if selectNum not in range(0, len(fileNameList)):
            print "invalid input!"

    # print "now selected filename is " + fileNameList[selectNum]
    return fileNameList[selectNum]


def strType(var):
    try:
        if int(var) == float(var):
            return 'int'
    except:
        try:
            float(var)
            return 'float'
        except:
            return 'str'


def isNum(var):
    if strType(var) == 'int' or strType(var) == 'float':
        return True
    else:
        return False


def isInt(var):
    if strType(var) == 'int':
        return True
    else:
        return False


def isFloat(var):
    if strType(var) == 'float':
        return True
    else:
        return False


def isStr(var):
    if strType(var) == 'str':
        return True
    else:
        return False




# def main():
#     tipList = ["there'are 3 options:\n",
#                "0: option0\n"
#                "1: option1\n"
#                "2: option2\n"
#                "please input your select :"]

#     maxOptions = 3

#     RadioSelect(tipList, maxOptions)


# if __name__ == "__main__":
#     main()
