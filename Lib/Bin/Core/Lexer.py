from .Modules.Standard import *

#Lexerish Lexer
def lex(filecontents):
    tok = ""
    state = 0
    isexpr = 0
    varstarted = 0
    var = ""
    string = ""
    expr = ""
    n = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                #print(expr + "EXPR")
                tokens.append("EXPR:" + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                #print(expr + "NUM")
                tokens.append("NUM:" + expr)
                expr = ""
            elif var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            tok = ""
        elif tok == "=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            if tokens[-1] == "EQUALS":
                tokens[-1] = "EQEQ"
            else:
                tokens.append("EQUALS")
            tok = ""

        #Var Assigning syntax
        elif tok == "set:" and state == 0:
            varstarted = 1
            var += tok
            tok = ""
        elif varstarted == 1:
            if tok == "<" or tok == ">":
                if var != "":
                    tokens.append("VAR:" + var)
                    var = ""
                    varstarted = 0
            var += tok
            tok = ""

        #Print Keyword
        elif tok == "PRINT" or tok == "print":
            #print("[Coconut.nut] Found a print")
            tokens.append("PRINT")
            tok = ""

        #Endif Statement Keyword
        elif tok == "ENDIF" or tok == "endif":
            #print("[Coconut.nut] Found a print")
            tokens.append("ENDIF")
            tok = ""

         #If Statement Keyword
        elif tok == "IF" or tok == "if":
            #print("[Coconut.nut] Found a print")
            tokens.append("IF")
            tok = ""

         #Then Keyword
        elif tok == "THEN" or tok == "then":
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            #print("[Coconut.nut] Found a print")
            tokens.append("THEN")
            tok = ""

        #Input Keyword
        elif tok == "INPUT" or tok == "input":
            #print("[Coconut.nut] Found a print")
            tokens.append("INPUT")
            tok = ""
        elif tok == "0" or  tok == "1" or  tok == "2" or  tok == "3" or  tok == "4" or  tok == "5" or  tok == "6" or  tok == "7" or  tok == "8" or  tok == "9":
            #print("NUMBER")
            expr += tok
            tok = ""
        elif tok == "+" or tok == "-" or tok == "*" or tok == "/" or tok == "(" or tok == ")":
            isexpr = 1
            expr += tok
            tok = ""

        #Ignores Tabs
        elif tok == "\t":
            tok = ""
        elif tok == "\"" or tok == " \"":
            if state == 0:
                state = 1
            elif state == 1:
                #print("[Coconut] Found a string")
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    #print(expr)
    #print(tokens)
    #symbols["varible"] = "Hello"
    #print(symbols)
    #return ''
    return tokens