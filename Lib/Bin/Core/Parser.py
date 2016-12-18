#Created by Coconut
#Written in Python

from .Modules.Standard import *

#Parser
def parse(toks):
    #print(toks)
    i = 0
    while(i < len(toks)):
        if toks[i] == "ENDIF":
            #print("Found an endif")
            i += 1
        #print(i)
        elif toks[i] + " " + toks[i + 1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i + 1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i + 1][0:4] == "PRINT EXPR" or toks[i] + " " + toks[i + 1][0:3] == "PRINT VAR":
        #i += i
            if toks[i + 1][0:6] == "STRING":
                doPRINT(toks[i + 1])
            elif toks[i + 1][0:3] == "NUM":
                doPRINT(toks[i + 1])
            elif toks[i + 1][0:4] == "EXPR":
                doPRINT(toks[i + 1])
            elif toks[i + 1][0:3] == "VAR":
                doPRINT(getVARIBLE(toks[i + 1]))
            i += 2

        #print(i/value)
        elif toks[i][0:3] + " " + toks[i + 1] + " " + toks[i + 2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i + 1] + " " + toks[i + 2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i + 1] + " " + toks[i + 2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i + 1] + " " + toks[i + 2][0:3] == "VAR EQUALS VAR":
            #print(toks[i + 2])
            if toks[i + 2][0:6] == "STRING":
                doASSIGN(toks[i],toks[i + 2])
            elif toks[i + 2][0:3] == "NUM":
                doASSIGN(toks[i],toks[i + 2])
            elif toks[i + 2][0:4] == "EXPR":
                doASSIGN(toks[i],"NUM:" + str(evalExpression(toks[i + 2][5:])))
            elif toks[i + 2][0:3] == "VAR":
                doASSIGN(toks[i],getVARIBLE(toks[i + 2]))
            i += 3

        # Input(i)
        elif toks[i] + " " + toks[i + 1][0:6] + " " + toks[i + 2][0:3] == "INPUT STRING VAR":
            getINPUT(toks[i + 1][7:],toks[i + 2][4:])
            i += 3

        elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF NUM EQEQ NUM THEN":
            #getINPUT(toks[i + 1][7:],toks[i + 2][4:])
            #print("Found an if statement")
            if toks[i + 1][4:] == toks[i + 3][4:]:
                print(Error_List[3])
            else:
                print(Error_List[4])
            i += 5

    #Useful for checking if var == stored
    #print(symbols)