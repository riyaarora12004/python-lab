import statistics

my_list = [3, 5, 2, 7, 1, 8, 4]

mean = statistics.mean(my_list)
print("Mean:", mean)

variance = statistics.variance(my_list)
print("Variance:", variance)

std_dev = statistics.stdev(my_list)
print("Standard Deviation:", std_dev)
