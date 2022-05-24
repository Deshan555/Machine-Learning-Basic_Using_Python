import numpy

import matplotlib.pyplot as plt

def create_BigData(start_value: float, end_value: float, range: float):

    data_list: list = numpy.random.uniform(start_value, end_value, range)

    return data_list


number_list: list = create_BigData(0.0, 5.0, 25000)

plt.hist(number_list, 1000)

plt.show()