
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listijk = [] #an empty list to be filled as following
    for i in range(x + 1): #it will output 0, and will only output 1 after the next conditions ('for j' and 'for k') are met.
        for j in range (y + 1): #it will output 0, and will only output 1 after the next condition ('for k') is met.
            for k in range (z + 1): #it will output 0 and then 1.
                listijk.append([i,j,k]) #it will add i, j and k values to the list
    print(listijk) #print the list properly filled
    #print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n ])