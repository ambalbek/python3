#!/usr/bin/env python3
"""                                                                                
 A digital root is the single digit value obtained by iteratively summing          
 the digits of a number, where each iteration uses the result from the             
 previous iteration to compute a sum. The process continues until a single         
 digit number is reached.                                                          
                                                                                   
 For example:                                                                      
 digital_root(65) = 2                                                              
 6 + 5 = 11, 1 + 1 = 2                                                             
 digital_root(65536) = 7                                                           
 6 + 5 + 5 + 3 + 6 = 25, 2 + 5 = 7                                                 
 digital_root(8) = 8                                                               
                                                                                   
Implement a function digital_root(n) that returns the digital root of n, given  
0 <= n <= 1000000.                                                                 
"""
def digital_root(n):
    answer=sum([int(i) for i in str(n)])  
    final= sum([int(i) for i in str(answer)])
    print(final) 
if __name__=='__main__':
    digital_root(65)
    digital_root(65536)