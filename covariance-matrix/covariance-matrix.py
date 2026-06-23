import numpy as np

def covariance_matrix(X):
    X=np.asarray(X, dtype=float)

    if X.ndim !=2: return None

    N=X.shape[0]
    if N<2 : return None

    mean=np.mean(X,axis=0)
    X_centered=X-mean
    covariance= (X_centered.T @ X_centered)/(N-1)

    return covariance