#Created by Sanjay(Coconut)
#Standard Library - an API for the Nutty Runtime
#Written in Python

#System Imports
from sys import *
import time 

#Dependent Semi-APIs
from .Error import * 

tokens = []
num_stack = []
symbols = {}

#Read File(s)
def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

#Lines 145 - 183 are base-operation functions
def evalExpression(expr):

    #Eval's Numeric Expressions
    return eval(expr)


def doPRINT(toPRINT):
    if(toPRINT[0:6] == "STRING"):
        toPRINT = toPRINT[8:]
        toPRINT = toPRINT[:-1]
    elif(toPRINT[0:3] == "NUM"):
        toPRINT = toPRINT[4:]
    elif(toPRINT[0:4] == "EXPR"):
        toPRINT = evalExpression(toPRINT[5:])
    print(toPRINT )


def doASSIGN(varname, varvalue):
    symbols[varname[7:]] = varvalue



def getVARIBLE(varname):
    varname = varname[7:]
    if varname in symbols:
        #print("TRUE")
        return symbols[varname]
    else:
        return Error_List[9]
        time.sleep(1)
        exit() #Stop current process



def getINPUT(string, varname):
    i = input(string[1: - 1] + " ")
    symbols[varname] = "STRING:\"" + i + "\""