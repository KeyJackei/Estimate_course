from Estimation import Cauchy_Estimate
from RandomVariable import RandomVariable
from scipy.stats import cauchy
import numpy as np

class SmoothedRandomVariable(RandomVariable, Cauchy_Estimate):
    def _k(x):
        if abs(x) <= 1:
            return 0.75 * (1 - x * x)
        else:
            return 0

    def _K(x):
        if x < -1:
            return 0
        elif -1 <= x < 1:
            return 0.5 + 0.75 * (x - x ** 3 / 3)
        else:
            return 1

    def __init__(self, sample, h, mu_optimal=None):
        self.sample = sample
        self.h = h
        self.mu_optimal = mu_optimal  # Оптимальное значение mu

    def pdf_cauchy(self, x):
        if self.mu_optimal is None:
            raise ValueError("Оптимальное значение mu не определено")
        return cauchy.pdf((x - self.mu_optimal) / self.h) / self.h

    def cdf_cauchy(self, x):
        if self.mu_optimal is None:
            raise ValueError("Оптимальное значение mu не определено")
        return cauchy.cdf((x - self.mu_optimal) / self.h)

    def pdf_median(self, x):
        return np.mean([SmoothedRandomVariable._k((x - y) / self.h) for y in self.sample]) / self.h


    def cdf_median(self, x):
        return np.mean([SmoothedRandomVariable._K((x - y) / self.h) for y in self.sample])


    def quantile(self, alpha):
        # Реализуйте ваш метод для вычисления квантили
        raise NotImplementedError