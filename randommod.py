import random

from random import sample

random_variable=random.random()
random_int_variable=random.randint(111111,999999)
random_range_variable=random.uniform(3,5)
sample_list=[1,2,3,45,6]

choice_variable=random.choice(sample_list)
random.shuffle(sample_list)

print(sample_list)