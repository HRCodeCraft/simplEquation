import numpy as np

class Fuzzification:
    def __init__(self, universe_of_discourse):
        self.universe_of_discourse = universe_of_discourse

    def triangular(self, x, a, b, c):
        less_than_a = np.less_equal(x, a)
        greater_than_c = np.greater_equal(x, c)
        return np.where(less_than_a | greater_than_c, 0, np.where(np.less(a, x) & np.less_equal(x, b), (x - a) / (b - a), (c - x) / (c - b)))

    def trapezoidal(self, x, a, b, c, d):
        less_than_a = np.less_equal(x, a)
        greater_than_d = np.greater_equal(x, d)
        return np.where(less_than_a | greater_than_d, 0, np.where(np.less(a, x) & np.less_equal(x, b), (x - a) / (b - a), (d - x) / (d - c)))

    def gaussian(self, x, mean, variance):
        return np.exp(-((x - mean)**2) / (2 * variance**2))

    def sigmoidal(self, x, a, c):
        return 1 / (1 + np.exp(-a * (x - c)))

# Example usage
if __name__ == "__main__":
    universe = np.arange(0, 11, 1)

    fuzz = Fuzzification(universe)

    # Triangular fuzzification
    a = fuzz.triangular(universe, 2, 4, 6)

    # Trapezoidal fuzzification
    b = fuzz.trapezoidal(universe, 3, 4, 6, 7)

    # Gaussian fuzzification
    c = fuzz.gaussian(universe, 5, 1)

    # Sigmoidal fuzzification
    d = fuzz.sigmoidal(universe, 1, 5)

    print("Triangular fuzzification:", a)
    print("Trapezoidal fuzzification:", b)
    print("Gaussian fuzzification:", c)
    print("Sigmoidal fuzzification:", d)
