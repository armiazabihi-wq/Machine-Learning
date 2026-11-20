import diagram
from data import create_data
from data import some_values

data_list = some_values()

print("Hur många värden som finns i res" , len(data_list))
print("Första tio värdena:", data_list[:10]) 

diagram.shows_histogram(data_list)
