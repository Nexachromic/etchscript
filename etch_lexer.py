
import sys

ERROR = -1          
SEMICOLON = 0       
ETCH = 1           
FEED = 2             
EQUAL = 3           
IF = 4              
THEN = 5
ELIF = 69            
ELSE = 6            
END = 7             
WHILE = 8           
DO = 9              
FOR = 10            
AND = 11            
OR = 12             
PLUS = 13           
MINUS = 14          
MULT = 15           
DIV = 16            
MOD = 17            
GREATERTHAN = 18    
GREATERTHANEQL = 19 
LESSTHAN = 20       
LESSTHANEQL = 21    
EQUALEQUAL = 22     
NOTEQUAL = 23       
PARENOPEN = 24      
PARENCLOSE = 25     
NOT = 26            
TRUE = 27           
FALSE = 28          
ENDSTREAM = 29      
STRING_TOKEN = 30   
ID_TOKEN = 31       
INT_TOKEN = 32      
BOOL_TOKEN = 33     
CHAR_TOKEN = 34     

NAMES = ["SEMICOLON", "ETCH", "FEED", "EQUAL", "IF", "THEN", "ELIF" "ELSE", "END", "WHILE", "DO", "FOR", "AND", "OR", "PLUS", 
        "MINUS", "MULT", "DIV", "MOD", "GREATERTHAN", "GREATERTHANEQL", "LESSTHAN", "LESSTHANEQL", "EQUALEQUAL", 
        "NOTEQUAL", "PARNOPEN", "PARENCLOSE", "NOT", "TRUE", "FALSE", "ENDSTREAM", "STRING_TOKEN", "ID_TOKEN",
        "INT_TOKEN", "BOOL_TOKEN", "CHAR_TOKEN"]





def startID(c):
    return c == "_" or c.isalpha()



def isIdChar(c):
    return c == "_" or c.isalpha() or c.isdigit()



def startString(c):
    return c == '"'



def startChar(c):
    return c == "'"



def tokenKeyWord(input, name):
    
    token = input[0]
    i = 1
    while i < len(input) and isIdChar(input[i]):    
        token = token + input[i]                    
        i = i + 1                                   
    if name == "etch":                     
        return [[ETCH, token], input[i:]]
    elif name == "feed":                     
        return [[FEED, token], input[i:]]
    elif name == "if":                      
        return [[IF, token], input[i:]]        
    elif name == "then":                    
        return [[THEN, token], input[i:]]
    elif name == "elif":
        return [[ELIF, token], input[i:]]
    elif name == "else":                    
        return [[ELSE, token], input[i:]]
    elif name == "end":                     
        return [[END, token], input[i:]]
    elif name == "while":                   
        return [[WHILE, token], input[i:]]
    elif name == "do":                      
        return [[DO, token], input[i:]]
    elif name == "for":                     
        return [[FOR, token], input[i:]]
    elif name == "and":                     
        return [[AND, token], input[i:]]
    elif name == "or":                      
        return [[OR, token], input[i:]]
    elif name == "True":                    
        return [[TRUE, token], input[i:]]
    elif name == "False":                   
        return [[FALSE, token], input[i:]]     
    elif name == ">=":                      
        return [[GREATERTHANEQL, token], input[i:]]   
    elif name == "<=":                      
        return [[LESSTHANEQL, token], input[i:]]
    elif name == "==":                      
        return [[EQUALEQUAL, token], input[i:]]
    elif name == "!=":                      
        return [[NOTEQUAL, token], input[i:]]


def tokenID(input):

    token = input[0]    
    i = 1
    while i < len(input) and isIdChar(input[i]):
        token = token + input[i]
        i = i + 1
    if(token == "end"):         
        return [[END, token], input[i:]]
    elif(token == "True"):      
        return [[TRUE, token], input[i:]]
    elif(token == "False"):     
        return [[FALSE, token], input[i:]]
    else:                       
        return [[ID_TOKEN, token], input[i:]]


def tokenInteger(input):

    token = input[0]    
    i = 1
    while i < len(input) and input[i].isdigit():    
        token = token + input[i]                    
        i = i + 1
    return [[INT_TOKEN, int(token)], input[i:]]     


def tokenString(input):

    endQuote = input.find('\"', 1)                                          
    if endQuote == -1:
        return [[ERROR, "Symbol not recognized."], input[0:]]           

    token = input[0:endQuote+1]                                             
    if len(token) >= 2 and token.startswith('"') and token.endswith('"'):   
        return [[STRING_TOKEN, token], input[len(token):]]


def tokenChar(input):

    if input[2] != "'":
        return [[ERROR, "Symbol not recognized."], input[0:]]           

    if len(input[0:3]) != 3:                                                
        return [[ERROR, "Symbol not recognized."], input[0:]]           

    token = input[0:3]                                                      
    if len(token) == 3 and token.startswith("'") and token.endswith("'"):   
        return [[CHAR_TOKEN, token], input[3:]]






def nextToken(input):

    i = 0
    while i < len(input) and input[i].isspace():    
        i = i + 1
    if i >= len(input):                             
        return [[ENDSTREAM, None], []]              

    
    
    elif input.split()[0] == "etch":
        return tokenKeyWord(input[i:], "etch")
    elif input.split()[0] == "feed":
        return tokenKeyWord(input[i:], "feed")
    elif input.split()[0] == "if":
        return tokenKeyWord(input[i:], "if") 
    elif input.split()[0] == "then":
        return tokenKeyWord(input[i:], "then")
    elif input.split()[0] == "elif":
        return tokenKeyWord(input[i:], "elif")    
    elif input.split()[0] == "else":
        return tokenKeyWord(input[i:], "else")
    elif input.split()[0] == "end":
        return tokenKeyWord(input[i:], "end")
    elif input.split()[0] == "while":
        return tokenKeyWord(input[i:], "while")
    elif input.split()[0] == "do":
        return tokenKeyWord(input[i:], "do")
    elif input.split()[0] == "for":
        return tokenKeyWord(input[i:], "for")
    elif input.split()[0] == "and":
        return tokenKeyWord(input[i:], "and")
    elif input.split()[0] == "or":
        return tokenKeyWord(input[i:], "or")
    elif input.split()[0] == "True":
        return tokenKeyWord(input[i:], "True")
    elif input.split()[0] == "False":
        return tokenKeyWord(input[i:], "False")
    elif input.split()[0] == ">=":
        return tokenKeyWord(input[i + 1:], ">=")    
    elif input.split()[0] == "<=":
        return tokenKeyWord(input[i + 1:], "<=")    
    elif input.split()[0] == "==":
        return tokenKeyWord(input[i + 1:], "==")    
    elif input.split()[0] == "!=":
        return tokenKeyWord(input[i + 1:], "!=")    

    
    
    elif input[i] == ";":
        return [[SEMICOLON], input[i + 1:]]
    elif input[i] == "=":
        return [[EQUAL], input[i + 1:]]
    elif input[i] == "+":
        return [[PLUS], input[i + 1:]]
    elif input[i] == "-":
        return [[MINUS], input[i + 1:]]
    elif input[i] == "*":
        return [[MULT], input[i + 1:]]
    elif input[i] == "/":
        return [[DIV], input[i + 1:]]
    elif input[i] == "%":
        return [[MOD], input[i + 1:]]
    elif input[i] == ">":
        return [[GREATERTHAN], input[i + 1:]]
    elif input[i] == "<":
        return [[LESSTHAN], input[i + 1:]]
    elif input[i] == "(":
        return [[PARENOPEN], input[i + 1:]]
    elif input[i] == ")":
        return [[PARENCLOSE], input[i + 1:]]
    elif input[i] == "!":
        return [[NOT], input[i + 1:]]

    
    
    elif startChar(input[i]):         
        return tokenChar(input[i:])     
    elif startString(input[i]):       
        return tokenString(input[i:])   
    elif startID(input[i]):           
        return tokenID(input[i:])       
    elif input[i].isdigit():            
        return tokenInteger(input[i:])  
    else:                               
        return [[ERROR, "Symbol not recognized."], input[i:]]   






def printLex(t):
    if t[0] >= 29:
        print(NAMES[t[0]] + "(" + str(t[1]) + ")")          
    else:
        print(NAMES[t[0]])                                  



def main():

    
    with open(str(sys.argv[1]), 'r') as file:                   
        input = file.read().replace('\n', '')                   

    temp = nextToken(input)                                     

    
    while temp[0][0] != ENDSTREAM and temp[0][0] != ERROR:      
        printLex(temp[0])                                       
        temp = nextToken(temp[1])                               

    if temp[0][0] == ERROR:                                     
        print("Lexical Analysis err: " + temp[0][1])                     

if __name__ == "__main__":
    main()

#End of EtchScript Lexical Analysis