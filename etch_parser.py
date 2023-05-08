import sys                  
from etch_lexer import *         

userVars = []               



def parseExpr(val, tok, userVars):
    
    
    

    if (tok[0][0] == 24 or tok[0][0] == 26 or tok[0][0] == 14 or tok[0][0] == 31 or 
        tok[0][0] == 32 or tok[0][0] == 33 or tok[0][0] == 34 or tok[0][0] == 15 or 
        tok[0][0] == 16 or tok[0][0] == 17 or tok[0][0] == 13 or tok[0][0] == 14):
        ret = parseExpr_N(val,tok, userVars)

    
    elif tok[0][0] == 11:
        ret = parseExpr_B(val, tok, userVars)
    elif tok[0][0] == 12:
        ret = parseExpr_B(val, tok, userVars)
    else:
        return val

    return parseExpr(ret[0], ret[1], userVars)     


def parseExpr_N(val, tok, userVars):    
    if tok[0][0] == 24:                 
        ret = parseTerm(val, tok[1:], userVars)

    elif (tok[0][0] == 26 or tok[0][0] == 31 or 
        tok[0][0] == 32 or tok[0][0] == 33 or tok[0][0] == 34 or tok[0][0] == 15 or 
        tok[0][0] == 16 or tok[0][0] == 17 or tok[0][0] == 18 or tok[0][0] == 19 or
        tok[0][0] == 20 or tok[0][0] == 21 or tok[0][0] == 22 or tok[0][0] == 23):
        ret = parseTerm(val, tok, userVars)

    
    elif tok[0][0] == 13:               
        ret = parseExpr_T(val, tok, userVars)
    elif tok[0][0] == 14:               
        ret = parseExpr_T(val, tok, userVars)
    else:
        return val, tok

    return parseExpr_N(ret[0], ret[1], userVars)


def parseExpr_B(val, tok, userVars):
    if tok[0][0] == 11:                 
        if (val and parseExpr_N(val, tok[1:], userVars)):
            return 1, tok[1:]
        else:
            return 0, tok[1:]
    elif tok[0][0] == 12:               
        if (val or parseExpr_N(val, tok[1:], userVars)):
            return 1, tok[1:]
        else:
            return 0, tok[1:]
    else:                               
        return


def parseExpr_T(val, tok, userVars):
    if tok[0][0] == 13:                  
        return val + (parseExpr_N(val, tok[1:], userVars))[0], tok[2:]
    elif tok[0][0] == 14:                
        return val - (parseExpr_N(val, tok[1:], userVars))[0], tok[2:]
    else:                           
        return



def parseTerm(val, tok, userVars):
    if tok[0][0] == 24:
        ret = parseExpr(val, tok, userVars)

    
    elif (tok[0][0] == 26 or tok[0][0] == 31 or tok[0][0] == 32 or
        tok[0][0] == 33 or tok[0][0] == 34 or tok[0][0] == 18 or tok[0][0] == 19 or
        tok[0][0] == 20 or tok[0][0] == 21 or tok[0][0] == 22 or tok[0][0] == 23):
        ret = parseFactor(val, tok, userVars)

    
    elif(tok[0][0] == 15 or tok[0][0] == 16 or tok[0][0] == 17):
        ret = parseExpr_F(val, tok, userVars)
    else:
        return val, tok

    return parseTerm(ret[0], ret[1], userVars)


def parseExpr_F(val, tok, userVars):
    if tok[0][0] == 15:         
        return val * (parseTerm(val, tok[1:], userVars))[0], tok[2:]               
    elif tok[0][0] == 16:       
        return val / (parseTerm(val, tok[1:], userVars))[0], tok[2:]
    elif tok[0][0] == 17:       
        return val % (parseTerm(val, tok[1:], userVars))[0], tok[2:]
    else:
        return


def parseFactor(val, tok, userVars):
    
    if(tok[0][0] == 26 or tok[0][0] == 31 or tok[0][0] == 32 or
        tok[0][0] == 33 or tok[0][0] == 34):
        ret = parseValue(tok, userVars)

    
    elif(tok[0][0] == 18 or tok[0][0] == 19 or tok[0][0] == 20 or tok[0][0] == 21 or
        tok[0][0] == 22 or tok[0][0] == 23):
        ret = parseExpr_V(val, tok, userVars)
    else:
        return val, tok
    return parseFactor(ret[0], ret[1], userVars)
    

def parseValue(tok, userVars):
    if tok[0][0] ==  24:                        
        return parseExpr(val, tok[1:], userVars)

    elif tok[0][0] == 26:                       
        val = parseValue(tok[1:], userVars)
        if val == 1:
            return 0, tok[1:]
        elif val == 0:
            return 1, tok[1:]

    elif tok[0][0] == 31:                       
        
        
        for i in userVars:
            if i[0] == tok[0][1]:       
                var = i[1]
        return var, tok[1:]

    elif tok[0][0] == 32:               
        return int(tok[0][1]), tok[1:]

    elif tok[0][0] == 34:               
        return tok[0][1], tok[1:]


def parseExpr_V(val, tok, userVars):
    ret = parseValue(tok[1:], userVars) 
    compVal = ret[0]                    

    if tok[0][0] == 18:                 
        if val > compVal:               
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]
    elif tok[0][0] == 19:               
        if val >= compVal:              
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]
    elif tok[0][0] == 20:               
        if val < compVal:               
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]
    elif tok[0][0] == 21:               
        if val <= compVal:              
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]
    elif tok[0][0] == 22:               
        if val == compVal:              
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]
    elif tok[0][0] == 23:               
        if val != compVal:              
            return 1, tok[2:]
        else:                           
            return 0, tok[2:]




def parsePrint(tok, userVars):
    
    if tok[0][0] == 1 and tok[1][0] == 30 and tok[2][0] == 0:
        string = tok[1][1]
        string = string[1:-1]                                   
        i = 0
        while i < len(string):                                  
            if string[i] == "\\" and string[i + 1] == "n":      
                print()
                i += 1
            elif string[i] == "\\" and string[i + 1] == "t":    
                print('\t', end="")
                i += 1
            else:
                print(string[i], end="")                        
            i += 1

    
    if tok[0][0] == 1 and tok[1][0] == 31 and tok[2][0] == 0:
        prt = ""
        for i in userVars:
            if i[0] == tok[1][1]:                               
                prt = i[1]                                      
        print(prt)                                              
    else:
        return tok[3:]
    return tok[3:]


def parseInput(tok, userVars):
    if tok[0][0] == 2 and tok[1][0] == 31 and tok[2][0] == 0:
        val = input(' ')                            
        if val[0] == "-":                           
            userVars.append([tok[1][1], int(val)])  
        if val.isdigit():                           
            userVars.append([tok[1][1], int(val)])  
        if val.isalpha():                           
            userVars.append([tok[1][1], val])       

    return tok[3:]


def parseAssign(tok, userVars):
    
    
    

    var = tok[0][1]                         
    val = parseExpr(0, tok[2:], userVars)   
    userVars.append([var, val])             

    count = 0
    for i in tok:
        if i[0] == 0:
            indexSemi = count               
            break
        count = count + 1

    return tok[indexSemi + 1:]              


def parseIf(tok, userVars):
    expr = parseExpr(0,tok[1:], userVars)   
    tok = tok[2:]                           

    
    count = 0
    for i in tok:
        if i[0] == 6:
            indexElse = count
            break
        count = count + 1

    
    count = 0
    for i in tok:
        if i[0] == 7:
            indexEnd = count
            break
        count = count + 1

    
    if expr == 1:
        del tok[indexElse: indexEnd + 1]        

        count = 0
        for i in tok:
            if i[0] == 5:
                indexThen = count               
                break
            count = count + 1
        
        tok = tok[indexThen+1:]                 
        return tok                              
    
    
    elif expr == 0:
        del tok[indexEnd]                       
        del tok[0:indexElse+1]                  
        return tok 

def parseElseIf(tok, userVars):
    expr = parseExpr(0,tok[1:], userVars)   
    tok = tok[2:]                           

    
    count = 0
    for i in tok:
        if i[0] == 6:
            indexElse = count
            break
        count = count + 1

    
    count = 0
    for i in tok:
        if i[0] == 7:
            indexEnd = count
            break
        count = count + 1

    
    if expr == 1:
        del tok[indexElse: indexEnd + 1]        

        count = 0
        for i in tok:
            if i[0] == 5:
                indexThen = count               
                break
            count = count + 1
        
        tok = tok[indexThen+1:]                 
        return tok                              
    
    
    elif expr == 0:
        del tok[indexEnd]                       
        del tok[0:indexElse+1]                  
        return tok                             


def parseStmt(tok, userVars):
    if tok[0][0] == 1:                          
        ret = parsePrint(tok, userVars)
    elif tok[0][0] == 2:                        
        ret = parseInput(tok, userVars)
    elif tok[0][0] == 31 and tok[1][0] == 3:    
        ret = parseAssign(tok, userVars)
    elif tok[0][0] == 4:                        
        ret = parseIf(tok, userVars)
    elif tok[0][0] == 69:
        ret = parseElseIf(tok, userVars)
    elif tok[0][0] == 29:                       
        return 0, tok
    else:                                       
        return 1, tok
    return parseStmt(ret, userVars)             


def parseStmtList(tok):
    ret = (parseStmt(tok, userVars))[0]         
    if ret == 1:
        return 1
    else:
        return 0


def main():
    with open(str(sys.argv[1]), 'r') as file:   
        tok = file.read().replace('\n', '')     

    tokens = []                                 
    temp = nextToken(tok)                       

    while temp[0][0] != ENDSTREAM and temp[0][0] != ERROR:
        tokens.append(temp[0])                  
        temp = nextToken(temp[1])               

        if temp[0][0] == ERROR:                 
            tokens.append(temp[0])              
            print("Lexical Analysis err: " + temp[0][1]) 

    if temp[0][0] != ERROR:
        tokens.append(temp[0])
        ret = parseStmtList(tokens)             

if __name__ == "__main__":
    main()

#End of EtchScript parsing