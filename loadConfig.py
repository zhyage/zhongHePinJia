# -*- coding:utf-8 -*-


import os
import os.path

import sys
from xml.etree.ElementTree import fromstring, ElementTree, Element
from xml.etree import ElementTree as ET

sys.path.append("")

from commonUtils import RadioSelect
from importSheetData import ImportSheet
from generateMethodPattern import generateMethodPattern
from generateMethodPattern import LoadExistMethodPattern


def LoadConfigFile(sheetInstance):

    tipList = ["Generate new configure file or Load exist configure file ?:\n",
               "0: ogenerate new configure file\n"
               "1: load exist configure file\n"
               "please input your select :"]

    maxOptions = 2
    select = RadioSelect(tipList, maxOptions)

    if 0 == select:
        configFile = generateMethodPattern(sheetInstance)
    else:
        configFile = LoadExistMethodPattern(sheetInstance)

    return configFile
