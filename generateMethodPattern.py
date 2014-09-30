#-*- coding:utf-8 -*-


import os
import os.path
from scipy import *
import xdrlib
import sys
import xlrd
from xlrd import open_workbook, cellname
import numpy as np
from xml.etree.ElementTree import fromstring, ElementTree, Element
from xml.etree import ElementTree as ET

sys.path.append("")
sys.path.append("BiaoZhunZhi")

from commonUtils import RadioSelect
from commonUtils import FileSelectPrompt


def print_node(node):
    '''print node infomation'''
    print "=============================================="
    print "node.attrib:%s" % node.attrib
    if node.attrib.has_key("select") > 0:
        print "node.attrib['select']:%s" % node.attrib['select']
        select = node.attrib['select']
        if "yes" == select:
            print "method %s is selected" % node.attrib['methodName']
    print "node.tag:%s" % node.tag
    print "node.text:%s" % node.text


def resetPatternFile(srcFile, destFile):
    open(destFile, "wb").write(open(srcFile, "rb").read())


def generateEmptyLineNode(configFile, lineNum):
    xmlText = open(configFile).read()

    root = fromstring(xmlText)
    for line in range(0, lineNum):
        ele = Element('array', {'arrayNum': str(line)})
        root.append(ele)

    ElementTree(root).write(configFile, encoding='utf-8')


def getMethodPatternNode(methodPatternFileName):
    srcXmlText = open(methodPatternFileName).read()
    root = fromstring(srcXmlText)
    node = root.find('method')
    return node


# def insertOneConfigureNode(patternNode):
def getOneConfigureNode():
    rootDir = 'BiaoZhunZhi'
    insertNodeList = []
    num = 0
    methodQuestionList = []

    arrayStr = "optional methods as follwing :"

    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(rootDir):

        for filename in filenames:  # 输出文件信息
            # print "the full name of the file is:" +
            # os.path.join(parent,filename) #输出文件路径信息
            fullName = os.path.join(parent, filename)
            if fullName[-4:] == '.xml':
                insertNode = getMethodPatternNode(fullName)
                insertNodeList.append(insertNode)

    for methodNode in insertNodeList:
        optionStr = str(num) + ' : ' + methodNode.attrib['methodName']
        methodQuestionList.append(optionStr)
        num = num + 1

    methodQuestionList.append("please input your select :")

    selected = RadioSelect(methodQuestionList, num)
    selectedNode = insertNodeList[selected]
    selectedNode.set('select', 'yes')

    # patternNode.append(selectedNode)
    return selectedNode


                # patternNode.append(insertNode)
def insertMethodPatternNodeIntoConfigurePattern(configFile):
    xmlText = open(configFile).read()
    root = fromstring(xmlText)
    lst_node = root.getiterator('array')
    insertNode = getOneConfigureNode()
    for node in lst_node:
        # insertOneConfigureNode(node)
        node.append(insertNode)

    #ElementTree(root).write(sys.stdout, encoding='utf-8')
    ElementTree(root).write(configFile, encoding='utf-8')

    root = ET.parse(configFile).getroot()
    indent(root)
    # ET.dump(root)
    ElementTree(root).write(configFile, encoding='utf-8')


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def getArgOfMethod(promptNode):
    print promptNode.attrib['prompt']
    promptTipStr = promptNode.attrib['tip']
    if promptTipStr.find(';') != 0:
        promptList = promptTipStr.split(';')
        for prompt in promptList:
            print prompt.strip()
    else:
        print promptTipStr.strip()

    res = raw_input("please input :")
    return res


    # print promptNode.attrib['prompt']
    # if promptNode.attrib['type'] == 'RADIO':
    #     promptStr = promptNode['tip']
    #     promptList = promptStr.split(';')
    #     for prompt in promptList:
    #         print prompt
    #     raw_input("please input : ")
    # elif promptNode.attrib['type'] == 'NUMBER':
    #     print promptNode.attrib['tip']
    #     raw_input("please input : ")

def PreCheckArg(arg, preCheckStr):
    preCheckStr = preCheckStr.strip()
    if len(preCheckStr) == 0:  # ""
        return True
    if preCheckStr.find('[') == -1:
        rangeList = preCheckStr.split(',')  # "x, y, z"
        for opt in rangeList:
            if arg == opt.strip():
                return True
        return False

    return True
    # todo ...


# def selectMethod(sheet, configFile):
#     configPatternFileName = configFile
#     lineNum = sheet.sheetNarray.shape[0]
#     xmlText = open(configPatternFileName).read()
#     root = fromstring(xmlText)
#     array_nodes = root.getiterator('array')

#     for line in range(0, lineNum):
# print_node(array_nodes[line])
#         methodNodes = array_nodes[line].getiterator('method')
#         num = 0
#         methodQuestionList = []

#         arrayStr = "array " + str(line) + ' '
#         arrayStr = arrayStr + "optional methods as follwing :"
#         methodQuestionList.append(arrayStr)
#         for methodNode in methodNodes:
#             optionStr = str(num) + ' : ' + methodNode.attrib['methodName']
#             methodQuestionList.append(optionStr)
#             num = num + 1

#         methodQuestionList.append("please input your select :")

#         selected = RadioSelect(methodQuestionList, num)

# print "select method = "
# print_node(methodNodes[int(selected)])
#         selectedNode = methodNodes[selected]
#         methodName = selectedNode.text
#         methodName = methodName.strip()
#         selectedNode.set('select', 'yes')
#         argsNode = selectedNode.find('functionArgs')
#         print "argsNode text ---------------" + argsNode.text
#         complexArgFun = argsNode.text
#         complexArgFun = complexArgFun.strip()
#         if len(complexArgFun) != 0:
#             argListRes = executeComplexArgFun(methodName, complexArgFun, sheet)
#             for arg in argListRes:
#                 ele = Element('p', {})
#                 ele.text = arg
#                 argsNode.append(ele)
# else:
# argNodeList = selectedNode.findall("functionArgs/p")
# for argNode in argNodeList:
# print_node(argNode)
# arg = getArgOfMethod(argNode)
# arg = arg.strip()
# if True == PreCheckArg(arg, argNode.attrib['preCheck']):
# argNode.text = arg
# else:
# print "invalid arg of " + argNode.attrib['prompt']

#     ElementTree(root).write(configPatternFileName, encoding='utf-8')

# def selectMethod(sheet, configFile):
#     print "empty"

def configMethodArgs(sheet, configFile):
    configPatternFileName = configFile
    lineNum = sheet.sheetNarray.shape[0]
    xmlText = open(configPatternFileName).read()
    root = fromstring(xmlText)
    array_nodes = root.getiterator('array')

    for line in range(0, lineNum):
        selectedNodes = array_nodes[line].getiterator('method')
        for selectedNode in selectedNodes:  # 事实上只有一个node
            methodName = selectedNode.text
            methodName = methodName.strip()
            argsNode = selectedNode.find('functionArgs')
            print "argsNode text ---------------" + argsNode.text
            print "config line " + str(line) + " arguments"
            complexArgFun = argsNode.text
            complexArgFun = complexArgFun.strip()
            if len(complexArgFun) != 0:
                argListRes = executeComplexArgFun(
                    methodName, complexArgFun, sheet)
                for arg in argListRes:
                    ele = Element('p', {})
                    ele.text = arg
                    argsNode.append(ele)

    ElementTree(root).write(configFile, encoding='utf-8')

    root = ET.parse(configFile).getroot()
    indent(root)
    # ET.dump(root)
    ElementTree(root).write(configFile, encoding='utf-8')                


def executeComplexArgFun(methodName, complexArgFun, sheet):
    # 等价于from os import path, pip
    module = __import__(methodName, globals(), locals(), [complexArgFun])
    ds = getattr(module, complexArgFun)
    res = False
    while res == False:
        res, resList = ds(sheet)

    return resList


def generateMethodPattern(sheet):
    # lineNum = 5
    # print "sheet.sheetNarray.ndim "
    # print sheet.sheetNarray.ndim
    # print "sheet.sheetNarray.shape "
    # print sheet.sheetNarray.shape
    if sheet.sheetNarray.ndim > 2 or sheet.sheetNarray.ndim < 1:
        print "not support yet !!"
        exit()
    lineNum = sheet.sheetNarray.shape[0]

    configPatternFileName = sheet.sheetFileName + \
        "_" + sheet.sheetName + "_" + "configurePattern.xml"
    configPatternBaseFileName = 'configurePatternBase.xml'
    resetPatternFile(configPatternBaseFileName, configPatternFileName)
    generateEmptyLineNode(configPatternFileName, lineNum)
    insertMethodPatternNodeIntoConfigurePattern(configPatternFileName)

    #selectMethod(sheet, configPatternFileName)
    configMethodArgs(sheet, configPatternFileName)

    return configPatternFileName


# if __name__ == '__main__':
#     sys.path.append("")
#     sys.path.append("BiaoZhunZhi")
#     generateMethodPattern(5)
#     selectMethod(5)

def LoadExistMethodPattern(sheet):
    configPatternFileName = FileSelectPrompt(".")
    return configPatternFileName
