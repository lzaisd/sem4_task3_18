def read_from_file(file):
    data = []
    with open(file) as f:
        for line in f:
            line_list = line.split()
            tablet = Tablet(line_list[0], int(line_list[1]), int(line_list[2]), int(line_list[3]))
            data.append(tablet)
    return data


def write_to_file(arr):
    f = open('output.txt', 'w')
    for elem in arr:
        f.write(str(elem) + " ")


class Tablet:
    def __init__(self, name, storage, rating, price):
        self.name = name
        self.storage = storage
        self.rating = rating
        self.price = price

    def __repr__(self):
        return '{' + self.name + ', ' + str(self.storage) + ', ' + str(self.rating) + ', ' + str(self.price) + '}'


def get_new_list(tablets, m, r):
    new_data = []
    for t in tablets:
        if t.storage >= m and t.rating >= r:
            new_data.append(t)
    return new_data


def choose_tablets(tablets, k):
    data = []
    total_price = 0
    for i, t in enumerate(tablets):
        if i >= k:
            return [data, total_price]
        data.append(t)
        total_price += t.price
    return [data, total_price]


tablets_list = read_from_file('input1.txt')

m = 64
r = 2
k = 2
new_tablets_list = get_new_list(tablets_list, m, r)
new_tablets_list.sort(key=lambda x: x.price)
result = choose_tablets(new_tablets_list, k)
write_to_file(result)

# k - кол-во планшетов
# объем памяти не ниже M и рейтинг не ниже R
