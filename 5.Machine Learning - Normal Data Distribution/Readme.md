
# Normal Data Distribution

## Discription

In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.

In this chapter we will learn how to create an array where the values are concentrated around a given value.

In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.

```javascript

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

```

## Histogram Explained

* We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.

* We specify that the mean value is 5.0, and the standard deviation is 1.0.

* Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.

* And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.