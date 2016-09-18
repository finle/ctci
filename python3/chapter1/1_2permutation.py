#!/usr/bin/python3

def permutation(str1,str2):
    
    strDict = {}
    
    if len(str1) != len(str2):
        return False
    
    
    for i in str1:
        if i not in strDict:
            strDict[i] = 1
        else:
            strDict[i] += 1
    
    for i in str2:
        if i not in strDict:
            return False
        else:
            if strDict[i] == 0:
                return False
            
    return True
