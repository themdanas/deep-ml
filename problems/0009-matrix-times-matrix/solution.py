def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    c=[]
    a_row=len(a)
    a_col=len(a[0])
    b_row=len(b)
    b_col=len(b[0])

    

    if(a_col==b_row):
        for i in range(a_row):
            curr_row=[]
            for j in range(b_col):
                prod=0
                for k in range(a_col):
                    prod+=a[i][k]*b[k][j]
                curr_row.append(prod)
            c.append(curr_row)
    
    else:

        return -1
        
            
	
    return c