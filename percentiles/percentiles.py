import numpy as np

def percentiles(x, q):
    x= np.sort(np.asarray(x,dtype=float))
    q= np.asarray(q,dtype=float)
    n= len(x)
    ans=[]
    for p in q:
        pos = (p/100)*(n-1)

        upper= int(np.ceil(pos))
        lower= int(np.floor(pos))

        if upper==lower:
            ans.append(x[lower])
        else:
            weight= pos-lower
            value= x[lower]+(x[upper]-x[lower])*weight
            ans.append(value)
    return np.array(ans)