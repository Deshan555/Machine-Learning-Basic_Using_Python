import numpy

import matplotlib.pyplot as plot

def create_dataSet(mean: float, standard__deviation: float, range: float):

    number_list: list = numpy.random.normal(mean, standard__deviation, range)

    return number_list


def draw_plot(data_set: list, number_ofBars: int):

    plot.hist(data_set, number_ofBars)

    plot.show()


## Call functions

set_data : list = create_dataSet(5.0, 1.0, 10000)

draw_plot(set_data, 100)