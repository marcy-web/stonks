import numpy
import matplotlib.pyplot as matplotlib

numpy.set_printoptions(suppress=True, precision=1, floatmode='fixed')
matplotlib.style.use('rose-pine-moon.mplstyle')

test_array = numpy.array([1, 4, 6, 9, 5])

def calculate_quadratic_variation(brownian_path):
    price_change = numpy.diff(brownian_path, axis = 0, prepend = 0.0)
    squared_change = numpy.power(price_change, 2)
    cumulative_square_change = numpy.cumsum(squared_change, axis = 0)
    return cumulative_square_change

def main():
    # variable declarations
    time_steps = 10000
    number_of_paths = 1
    time_horizon = 1.0

    # variable declarations but with calculations
    time_points = numpy.linspace(0.0, time_horizon, time_steps)
    time_differential = time_points[1] - time_points[0]
    brownian_differential = numpy.sqrt(time_differential) * numpy.random.normal(size = (time_steps - 1, number_of_paths))
    brownian_start = numpy.zeros(shape = (1, number_of_paths))
    brownian_paths = numpy.concatenate((brownian_start, numpy.cumsum(brownian_differential, axis = 0)), axis = 0)

    #data visualisation
    matplotlib.plot(time_points, brownian_paths)
    matplotlib.show()

main()