#Written by Sanjay(Coconut)
#Nutty Runtime - Executes .nut
#Written in Python

#Imports Standard Library
from Core.Modules.Standard import *

#Imports Core File(s)
from Core.Lexer import *
from Core.Parser import *

#Runs File(s)
def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()