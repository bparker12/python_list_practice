import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

for number in range(1, 6):
        # print(number)
        # print(my_randoms)
        if  my_randoms.count(number) > 0:
            print(f'my_randoms list contains {number}')
        else:
            print(f'my_randoms list does not contain {number}')