from abc import ABC
import numpy as np

from Estimation import Var

class Modelling(ABC):
    def __init__(self, gen, estimations, M, truth_value):
        self.gen = gen
        self.estimations = estimations
        self.M = M
        self.truth_value = truth_value
        self.estimations_sample = np.zeros((M, len(estimations)))  # Добавленная строка

    def estimate_bias_sqr(self):
        return np.array([(estimation.estimate(self.estimations_sample[i, :]) - self.truth_value) ** 2 for i, estimation in enumerate(self.estimations)])

    def estimate_var(self):
        return np.array([Var().estimate(self.estimations_sample[:, i]) for i in range(len(self.estimations))])

    def estimate_mse(self):
        return np.array([e.estimate(self.estimations_sample[:, i]) for i, e in enumerate(self.estimations)])

    def get_samples(self):
        return self.estimations_sample

    def get_sample(self):
        return self.gen.get(50)

    def run(self, additional_argument):
        for i in range(self.M):
            sample = self.get_sample()
            self.estimations_sample[i, :] = [e.estimate(sample) for e in self.estimations]

