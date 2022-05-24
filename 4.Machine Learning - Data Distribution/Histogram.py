import numpy

import matplotlib.pyplot as plot 

data_list: list = numpy.random.uniform(0.0, 5.0, 250)

plot.hist(data_list, 20)

plot.show()
