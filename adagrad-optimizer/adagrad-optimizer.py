import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    for i in range(len(g)):
        G[i]=G[i]+(g[i]*g[i])
    for i in range(len(g)):
        w[i]= w[i]-(lr/np.sqrt(G[i]+eps))*g[i]
    return (w,G)