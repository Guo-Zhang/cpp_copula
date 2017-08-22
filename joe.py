# !/usr/bin/env python
# -*- coding: utf-8 -*-

# ========== module document ==========

__pyVersion__ = '3.5.2'

__author__ = 'Yilin Zhang'

__date__ = '2017-8-18'

__moduleVersion__ = '1.0'



# ========== import packages ==========

# import third-party packages
import numpy as np
import sympy as sp
from scipy import integrate

# ========== class definition ==========

## Archimedean Copula(distributed with theta)
class ArcmCopula(object):
    """
    Note to reader: Each bivariate copula should be its own subclass that implements the following methods.
    """

    def __init__(self):
        pass

    def pdf(self):
        """
        Evaluate the probability distribution function (pdf) at a point (u,v) for a parameter theta
        """
        pass

    def cdf(self):
        """
        Evaluate the cumulative distribution function (cdf) at a point (u,v) for a parameter theta
        """
        pass

    def rvs(self):
        """
        Generate a simulation for the copula given a specified parameter theta.
        """
        pass

    def rho(self):
        """
        Calculate Spearman's rho for the copula given a specified parameter theta.
        """
        pass


## Joe Copula (distributed with theta)
class JoeCopula(object): # object waiting to change 
    """
    An joe_copula with one parameter theta.
    Get pdf, cdf, logpdf, sf, logsf given 2D-ndarray,
    seeing each row as a point in distribution.
    
    Parameters
    ----------
        x: 2D-ndarray;
           number in x should be between (0,1);
    theta: float;
           number should larger than one
    
    Examples
    -----------
    x = np.array([[0.1,0.2,0.3],[0.2,0.3,0.4]])
    myjoe = JoeCopula()
    myjoe.pdf(x,1.2)
    """
    def __init__(self):
        pass
    
    def cdf(self, x, theta):
        """
        genarator function : f(x)
        inverse genarator function : g(x)
        X = (x1, x2, ... ,xn)
        cdf(X) = g(f(x1)+f(x2)+...+f(xn))
        """
        term = np.sum(-np.log(1.0-(1.0-x)**theta),axis=-1)
        return 1.0-(1.0-np.exp(-term))**(1.0/theta)
    
    def pdf(self, x, theta):
        """
        genarator function : f(x)
        inverse genarator function : g(x)
        X = (x1, x2, ... ,xn)
        pdf(X) = g^{(-n)}(f(x1)+f(x2)+...+f(xn))f'(x1)f'(x2)...f'(xn)
        """
        dim = x.shape[-1]
        term = np.sum(-np.log(1.0-(1.0-x)**theta),axis=-1)
        
        # get the differentiation of the genarator function and inverse genarator function
        t = sp.Symbol('t')
        f1 = 1.0-(1.0-sp.exp(-t))**(1.0/theta)
        for i in range(dim):
            f1 = sp.diff(f1,t)
        f2 = -sp.log(1.0-(1.0-t)**theta)                       
        f2 = sp.diff(f2,t)
        
        # get ufunc of the differentiation equation
        u1 = lambda z: f1.subs(t,z)
        u1 = np.frompyfunc(u1,1,1)
        u2 = lambda z: f2.subs(t,z)
        u2 = np.frompyfunc(u2,1,1)
        return u1(term)*np.prod(u2(x),axis=-1)
    
    def rvs(self, n, dim, theta):
        """
        Monte Carlo simulation using JoeCopula.pdf(self, k, theta)
        """
        i = 0
        while(i<n):
            k = np.random.random_sample(dim)
            if theta*np.random.random_sample(1)< JoeCopula.pdf(self, k, theta):
                if i == 0:
                    sample = k
                else:
                    sample = np.vstack((sample,k))
                i = i+1
        return sample

    def tau(self, x, theta):
        """
        genarator function : f(t)
        $$tau(x)=1+\int^1_0 \frac{f(t)}{f'(t)}dt$$
        """
        f = lambda t: np.log(1.0-(1.0-t)**theta)/(theta*(1.0-t)**(theta-1.0)/(1.0-(1.0-t)**theta))# f = (-log(1-(1-t)^theta)) / (theta*(1-t)^theta/(1-(1-t)^theta))
        return 1.0+4.0*integrate.quad(f, 0, 1.0)[0]
    
#----------class definition----------
        
        

#----------main function----------

if __name__ == '__main__':
    x = np.array([[0.1,0.2],[0.8,0.9]])
    myjoe = JoeCopula()
    print(myjoe.rvs(n=5,dim=7,theta=1.2))
    
#----------main function----------

