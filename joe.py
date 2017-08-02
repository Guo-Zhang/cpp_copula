#! usr/bin/python


class Copula:
    """
    Note to reader: Each bivariate copula should be its own subclass that implements the following methods.
    """

    def __init__():
        pass

    def pdf():
        """
        Evaluate the probability distribution function (pdf) at a point (u,v) for a parameter theta
        """
        pass

    def cdf():
        """
        Evaluate the cumulative distribution function (cdf) at a point (u,v) for a parameter theta
        """
        pass

    def rvs():
        """
        Generate a simulation for the copula given a specified parameter theta.
        """
        pass

    def rho():
        """
        Calculate Spearman's rho for the copula given a specified parameter theta.
        """
        pass

    def tau():
        """
        Calculate Kendall's tau for the copula given a specified parameter theta.
        """
        pass


class Joe(Copula):

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
        C(u,v;\theta) = 1-[(1-u)^\theta+(1-v)^\theta-(1-u)^\theta(1-v)^\theta]^{\frac{1}{\theta}}
        :param u:
        :param v:
        :param theta:
        :return:
        """
        assert theta!=0, 'Parameter theta cannot be zero. Please check. '
        return 1-((1-u)**theta+(1-v)**theta-(1-u)**theta*(1-v)**theta)**(1/float(theta))

    def rvs(self):
        pass

    def rho(self):
        pass

    def tau(self):
        pass