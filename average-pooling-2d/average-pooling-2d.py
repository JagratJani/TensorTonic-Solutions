def average_pooling_2d(X, pool_size):
    rows=len(X)
    cols=len(X[0])
    result=[]

    for i in range(0,rows-pool_size+1,pool_size):
        pooled_row=[]

        for j in range(0,cols-pool_size+1,pool_size):
            total=0

            for r in range(i,i+pool_size):
                for c in range(j,j+pool_size):
                    total+=X[r][c]

            pooled_row.append(total/(pool_size*pool_size))
        result.append(pooled_row)
    return result
            