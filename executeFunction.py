# -*- coding:utf-8 -*-

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


def ComposeMethodAndExecute(node, sheet, lineNum):

    # print_node(node)
    methodName = node.text
    methodName = methodName.strip()

    lst_node_child = node.getchildren()
    callFunction = ""
    argsList = []
    for childNode in lst_node_child:
        if childNode.tag == "callFunction":
            callFunction = childNode.text
            callFunction = callFunction.strip()
            print "callFunction %s " % callFunction
        if childNode.tag == "functionArgs":
            lst_args_child = childNode.getchildren()
            for argNode in lst_args_child:
                argsList.append(argNode.text)

    print "call function :" + callFunction
    print "lineNum %d:" % lineNum
    print "args :"
    print argsList

    # 等价于from os import path, pip
    module = __import__(methodName, globals(), locals(), [callFunction])
    ds = getattr(module, callFunction)
    res = ds(sheet.sheetNarray, sheet.sheetWuLiangNarray, lineNum, argsList)

    # print res


def executeFunction(sheet, configFile):
    configPatternFileName = configFile
    lineNum = sheet.sheetNarray.shape[0]
    xmlText = open(configPatternFileName).read()
    root = fromstring(xmlText)
    array_nodes = root.getiterator('array')

    for line in range(0, lineNum):
        # print_node(array_nodes[line])
        methodNodes = array_nodes[line].getiterator('method')

        for methodNode in methodNodes:
            if methodNode.attrib.has_key("select") > 0:
                select = methodNode.attrib['select']
                if "yes" == select.strip():
                    ComposeMethodAndExecute(methodNode, sheet, line)

    print "src matrix -------------"
    print sheet.sheetNarray
    print "dst matrix -------------"
    print sheet.sheetWuLiangNarray
