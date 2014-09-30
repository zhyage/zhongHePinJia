#-*- coding:utf-8 -*-


import os
import os.path

import sys
from xml.etree.ElementTree import fromstring, ElementTree, Element
#from xml.etree.ElementTree import fromstring, Element
#import lxml.etree as etree
#from xml.etree import ElementTree
from xml.etree import ElementTree as ET  



def print_node(node):
    '''print node infomation'''
    print "=============================================="
    print "node.attrib:%s" % node.attrib
    if node.attrib.has_key("select") > 0 :
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

def insertOneConfigureNode(patternNode):
    rootDir = 'BiaoZhunZhi'
    for parent,dirnames,filenames in os.walk(rootDir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        for filename in filenames:                        #输出文件信息
            #print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            fullName = os.path.join(parent,filename)
            if fullName[-4:] == '.xml' :
                insertNode = getMethodPatternNode(fullName)
                patternNode.append(insertNode)
                

def insertMethodPatternNodeIntoConfigurePattern(configFile):
    xmlText = open(configFile).read()
    root = fromstring(xmlText)
    lst_node = root.getiterator('array')
    for node in lst_node:
        insertOneConfigureNode(node)

    #ElementTree(root).write(sys.stdout, encoding='utf-8')
    ElementTree(root).write(configFile, encoding='utf-8')   

    root = ET.parse(configFile).getroot()
    indent(root)
    #ET.dump(root)
    ElementTree(root).write(configFile, encoding='utf-8') 


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def selectMethod(lineNum):
    configPatternFileName = 'configurePattern.xml'
    xmlText = open(configPatternFileName).read()
    root = fromstring(xmlText)
    array_nodes = root.getiterator('array')    

    
    for line in range(0, lineNum):
        #print_node(array_nodes[line])
        methodNodes = array_nodes[line].getiterator('method')
        num = 0
        methodQuestionList = []
        for methodNode in methodNodes:
            #print_node(methodNode)
            optionStr = str(num) + ' : ' + methodNode.attrib['methodName']
            methodQuestionList.append(optionStr)
            num = num + 1
        arrayStr = "array " + str(line) + ' '    
        print arrayStr + "optional methods as follwing"
        for option in methodQuestionList:
            print option

        selected = raw_input("please input your select for " + arrayStr + " : " )
        if int(selected) >= num:
            print "incorrect select"
            exit()






def generateMethodPattern(lineNum):
    configPatternFileName = 'configurePattern.xml'
    configPatternBaseFileName = 'configurePatternBase.xml'

    resetPatternFile(configPatternBaseFileName, configPatternFileName)

    generateEmptyLineNode(configPatternFileName, lineNum)

    insertMethodPatternNodeIntoConfigurePattern(configPatternFileName)


if __name__ == '__main__':
    generateMethodPattern(5)
    selectMethod(5)


