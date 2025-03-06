import numpy
import matplotlib.pyplot as matplotlib

numpy.set_printoptions(suppress=True, precision=1, floatmode='fixed')
matplotlib.style.use('rose-pine-moon.mplstyle')


def main():
    # variable declarations
    drift_coefficient = 0.1
    number_of_steps = 1000
    time_in_years = 1
    number_of_paths = 100
    initial_stock_price = 100
    volatility = 0.3

    #simulating geometric brownian motion paths
    time_steps = time_in_years / number_of_steps
    deterministic_drift = (drift_coefficient - volatility ** 2 / 2) * time_steps
    random_shocks = numpy.random.normal(0, numpy.sqrt(time_steps), size = (number_of_paths, number_of_steps))
    random_shocks = random_shocks.T
    stochastic_component = volatility * random_shocks
    drift_factor_per_step = numpy.exp(deterministic_drift + stochastic_component)

    drift_factor_per_step = numpy.vstack([numpy.ones(number_of_paths), drift_factor_per_step])
    drift_factor_per_step = initial_stock_price * drift_factor_per_step.cumprod(axis = 0)
    
    #consider time interval in years
    time_interval = numpy.linspace(0, time_in_years, number_of_steps + 1)
    time_point_matrix = numpy.full(shape = (number_of_paths, number_of_steps + 1), fill_value = time_interval).T

    #data visualisation
    matplotlib.figure(figsize=(28.8, 21.6), dpi=100)
    matplotlib.rcParams.update({'font.size': 22})
    matplotlib.grid(True)
    matplotlib.plot(time_point_matrix, drift_factor_per_step)
    matplotlib.title("Realisations of Geometric Brownian Motion")
    matplotlib.xlabel("Years (t)")
    matplotlib.ylabel("Stock Price ($)")
    matplotlib.savefig("geometric_brownian_motion.png")
    matplotlib.show()

main()