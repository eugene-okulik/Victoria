import json


class Flower:
    def __init__(self, name, lifetime, freshness, color, length, price):
        self.name = name
        self.lifetime = lifetime
        self.freshness = freshness
        self.color = color
        self.length = length
        self.price = price


class Rose(Flower):
    def __init__(self, name, lifetime, freshness, color, length, price):
        super().__init__(name, lifetime, freshness, color, length, price)

    def __repr__(self):
        r = {
            'name': self.name,
            'lifetime': self.lifetime,
            'freshness': self.freshness,
            'color': self.color,
            'length': self.length,
            'price': self.price
        }
        return json.dumps(r)


class Lily(Flower):
    def __init__(self, name, lifetime, freshness, color, length, price):
        super().__init__(name, lifetime, freshness, color, length, price)

    def __repr__(self):
        r = {
            'name': self.name,
            'lifetime': self.lifetime,
            'freshness': self.freshness,
            'color': self.color,
            'length': self.length,
            'price': self.price
        }
        return json.dumps(r)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def duration(self):
        total_flowers = len(self.flowers)
        total_duration = sum([flower.lifetime - flower.freshness for flower in self.flowers])
        # for flower in self.flowers:
        #     total_duration += flower.lifetime - flower.freshness
        return total_duration / total_flowers

    def price(self):
        total_price = sum([flower.price for flower in self.flowers])
        return total_price

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda x: x.price)

    def sort_by_length(self):
        return sorted(self.flowers, key=lambda x: x.length)

    def search_by_color(self, color):
        colored_flowers = []
        for flower in self.flowers:
            if flower.color.lower() == color.lower():
                colored_flowers.append(flower)
        return colored_flowers


rose1 = Rose('Rose', 3, 1, 'red', 20, 120)
rose2 = Rose('Rose', 3, 2, 'white', 80, 350)
rose3 = Rose('Rose', 4, 3, 'yellow', 39, 30)

lily1 = Lily('Lily', 7, 5, 'white', 50, 150)
lily2 = Lily('Lily', 10, 8, 'orange', 70, 140)


my_bouquet = Bouquet()
my_bouquet.add_flower(rose1)
my_bouquet.add_flower(rose2)
my_bouquet.add_flower(lily1)

print(my_bouquet.duration())
print(my_bouquet.price())
print(my_bouquet.sort_by_price())
print(my_bouquet.sort_by_length())
print(my_bouquet.search_by_color('RED'))
