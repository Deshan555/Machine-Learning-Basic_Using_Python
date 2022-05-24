import numpy

ages: list = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# lets calculate What is the 75% percentile?

calculate = numpy.percentile(ages, 75)

print("What is the 75% percentile? Answer Is : ",calculate)

# lets calculate What is the 90% percentile?

calculate = numpy.percentile(ages, 90)

print("What is the 90% percentile? Answer Is : ",calculate)