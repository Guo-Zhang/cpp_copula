#! usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals


# ========== import packages ==========

# import third-party packages
import numpy as np


# ========== class definition ==========

# ----- Base Classes of Coupla ------
class Copula(object):
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

    def tau(self):
        """
        Calculate Kendall's tau for the copula given a specified parameter theta.
        """
        pass


# ---- ARCM Coupla -----
class JoeCopula(Copula):

    def pdf(self, u, v, theta):
        """
        c(u,v;\theta)=
        :param u:
        :param v:
        :param theta:
        :return:
        """
        return None

    def cdf(self, u, v, theta):
        """
        $$C(u,v;\theta) = 1-[(1-u)^\theta+(1-v)^\theta-(1-u)^\theta(1-v)^\theta]^{\frac{1}{\theta}}$$
        where $\theta \leq 1$
        :param u:
        :param v:
        :param theta:
        :return:
        """
        assert theta>=1, 'Parameter theta cannot be less than 1. Please check. '
        return 1-((1-u)**theta+(1-v)**theta-(1-u)**theta*(1-v)**theta)**(1/float(theta))

    def rvs(self):
        pass

    def rho(self):
        pass

    def tau(self):
        pass