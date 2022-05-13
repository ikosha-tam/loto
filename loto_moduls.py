import random

# Мешок
bag = []
# Число боченков
number_barrels = 90

def init_bag():
    '''

    :return: 
    '''


# Инициализация мешка
for item in range(1, number_barrels + 1):
    bag.append(item)
print(bag)
for i in range(80):
    random_number = random.choice(bag)
    print(random_number, len(bag))
    bag.remove(random_number)
    input()
print(bag)
