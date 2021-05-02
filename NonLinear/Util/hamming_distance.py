def hammingDistance(n1, n2) : 
    
    #Calculate the XOR of two numbers
    x = n1 ^ n2  
    setBits = 0
    # count the number of 1s 
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits  
