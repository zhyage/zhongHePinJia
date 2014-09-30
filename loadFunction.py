#-*- coding:utf-8 -*-

import sys
#from xml.etree import ElementTree
from xml.etree.ElementTree import fromstring, ElementTree, Element
#from BiaoZhunZhi_JiHuaZhiFa import BiaoZhunZhi_JiHuaZhiFaCheckArg 


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

def ComposeMethod(xmlFileName):
    #root = ElementTree.fromstring(xmlText)
    xmlText = open(xmlFileName).read()
    root = fromstring(xmlText)
    node = root.find('method')
    print_node(node)
    methodName = node.text
    methodName = methodName.strip()

    lst_node_child = node.getchildren()
    callFunction = ""
    checkFunction = ""
    argsList = []
    for childNode in lst_node_child:
    #    print_node(childNode)
        if childNode.tag == "callFunction":
            callFunction = childNode.text
            callFunction = callFunction.strip()
            print "callFunction %s " % callFunction
        if childNode.tag == "checkFunction":
        	checkFunction = childNode.text
        	checkFunction = checkFunction.strip()
        	print "checkFunction %s " % checkFunction
        if childNode.tag == "functionArgs":
        	lst_args_child = childNode.getchildren()
        	for argNode in lst_args_child:
        		argsList.append(argNode.text)
        	print "arguments "
        	print argsList


    module = __import__(methodName,globals(),locals(),[callFunction])  #等价于from os import path, pip
    ds = getattr(module,callFunction)
    res = ds(1,2)
    print res
    ds = getattr(module, checkFunction)
    res = ds(2, 2)
    print res

    	  	
def GetMethodNode(xmlText):
    #root = ElementTree.fromstring(xmlText)
    root = fromstring(xmlText)
    node = root.find('method')
    return node

def AppendNodeIntoPattern(srcXmlFileName, destXmlFileName):
    srcXmlText = open(srcXmlFileName).read()
    destXmlText = open(destXmlFileName).read()
    appendNode = GetMethodNode(srcXmlText)
    print_node(appendNode)
    #destRoot = ElementTree.fromstring(destXmlText)
    destRoot = fromstring(destXmlText)	 
    lst_node = destRoot.getiterator('line')
    for node in lst_node:
        print_node(node)
        node.append(appendNode)
        #node.append(Element('D', {'name': 'error'}))

    ElementTree(destRoot).write(sys.stdout, encoding='utf-8')    
    ElementTree(destRoot).write(destXmlFileName, encoding='utf-8')    

  	


def read_xml(text):
    '''read xml file'''
    # 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）   

    # root = ElementTree.fromstring(text)
     

    # 获取element的方法
    # 1 通过getiterator
    # lst_node = root.getiterator("method")
    # for node in lst_node:
    # 	if node.attrib.has_key("select") > 0 and node.attrib['select'] == "yes":
    # 		ComposeMethod(node)
        
         
    # 2通过 getchildren
    #lst_node_child = lst_node[0].getchildren()[0]
    #print_node(lst_node_child)
         
    # 3 .find方法
    #node_find = root.find('person')
    #print_node(node_find)
     
    #4. findall方法
    #node_findall = root.findall("person/name")[1]
    #print_node(node_findall)
     
if __name__ == '__main__':
    #read_xml(open("BiaoZhunZhi_JiHuaZhiFa.xml").read())
    #ComposeMethod(open("BiaoZhunZhi_JiHuaZhiFa.xml").read())

    AppendNodeIntoPattern("BiaoZhunZhi_JiZhiHuaFa.xml", "configurePattern.xml")