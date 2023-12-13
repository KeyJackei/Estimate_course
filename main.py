from Modelling import Modelling
from NonParametricRandomVariable import NonParametricRandomVariable
from  RandomNumberGenerator import RandomNumberGenerator
from RandomVariable import RandomVariable
from SimpleRandomNumberGenerator import SimpleRandomNumberGenerator
from NormalRandomVariable import NormalRandomVariable

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

from Estimation import Choose_Mean, Cauchy_Estimate


# Коши: -0.018268944270937393 Медиана -0.01606540533879085
def iterative_mu_2(sample, eps=0.01):
    mu_2_prev = Choose_Mean().estimate(sample)  # начальная оценка mu_2
    iteration = 0

    while True:
        numerator_sum = np.sum(sample * cauchy.pdf(sample, mu_2_prev))
        denominator_sum = np.sum(cauchy.pdf(sample, mu_2_prev))

        mu_2_current = numerator_sum / denominator_sum

        if abs(mu_2_current - mu_2_prev) < eps:
            break  # условие завершения цикла

        mu_2_prev = mu_2_current
        iteration += 1
    print(mu_2_current, mu_2_prev)

    return mu_2_current, iteration

def main():
    location = 0
    scale = 1
    N = 500

    rv = NormalRandomVariable(location, scale)
    generator = SimpleRandomNumberGenerator(rv)

    sample = generator.get(N)
    rv1 = NonParametricRandomVariable(sample)
    generator1 = SimpleRandomNumberGenerator(rv1)

    estimations = [Choose_Mean(), Cauchy_Estimate()]  # Создаем объекты оценок
    estimations_sample = np.zeros((2 * N, len(estimations)))

    modelling = Modelling(generator1, estimations, 2 * N, location)
    modelling.run(estimations_sample)

    bootstrap_samples = estimations_sample
    mses = modelling.estimate_mse()

    print("СКО: ", mses)
    print("Во сколько раз вторая оценка хуже первой:", mses[1] / mses[0])

if __name__ == "__main__":
    main()






    # choose_mean = Choose_Mean()
    #
    # eps = 0.01
    # mu_2 = choose_mean.estimate(sample)
    # for x_i in sample:
    #     mu_cauhy = (sum((x_i * cauchy.pdf(x_i, 0, mu_2))))/ sum(cauchy.pdf(x_i, 0, mu_2))
    #     if abs(mu_cauhy - mu_2) < eps:
    #         mu_2 = mu_cauhy
    #         print(mu_2)
    #         break
    #     else:
    #         mu_2 = mu_cauhy
    #         mu_cauhy = mu_2







