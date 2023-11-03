# TASK 1

# import random
#
# class MusicAlbum:
#     def __init__(self, title, artist, releaseYear, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.releaseYear = releaseYear
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.releaseYear}
# Жанр: {self.genre}
# Список треков: {self.tracklist}
#         ''')
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
#
# album4.get_info()
# print(album4.play_random_track())







# TASK 2

# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def average_score(self):
#         self.averageScore = 0
#         for i in range(len(self.scores)):
#             self.averageScore += self.scores[i]
#         self.averageScore = self.averageScore / len(self.scores)
#         return self.averageScore
#
# student2 = Student("Badili Rammov", 23, "952-I", [5,4,5,5,4,4])
# print(f'''
# Name: {student2.name}
# Age: {student2.age}
# Grade: {student2.grade}
# Scores: {student2.scores}
# AverageScore: {student2.average_score()}
# ''')






# TASK 3

# class Recipe:
#     def __init__(self, productName, ingredients):
#         self.productName = productName
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         resultList = f"Ingredients for {self.productName}:\n"
#         for i in range(len(self.ingredients)):
#             resultList += (self.ingredients[i] + "\n")
#         print (resultList)
#
#     def cook(self):
#         print (f'''
# Start cooking {self.productName}
# Processing...
# Success! {self.productName} is ready!
# ''')
#
# cake = Recipe("Cake", ["ing1", "ing2", "ing3", "ing4", "ing5", "ing6"])
# cake.print_ingredients()
# cake.cook()






# TASK 4

# class Publisher:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         print(f'Publisher name: {self.name}\nPublisher location: {self.location}')
#
#     def publish(self, message):
#         self.message = message
#         print(f'Готовим "{self.message}" к публикации в {self.name} ({self.location})')
#
#
# class BookPublisher(Publisher):
#     def __init__(self, name,location, num_authors):
#         super().__init__(name,location)
#         self.num_authors = num_authors
#
#     def publish(self, book, authorName):
#         self.book = book
#         self.authorName = authorName
#         print(f'Передаем рукопись "{self.book}", написанную автором {self.authorName} в издательство {self.name} ({self.location})')
#
#
#
# class NewspaperPublisher(Publisher):
#     def __init__(self, name, location, num_pages):
#         super().__init__(name, location)
#         self.num_pages = num_pages
#
#
#     def publish(self, title):
#         self.title = title
#         print(f'Печатаем свежий номер со статьей "{self.title}" на главной странице в издательстве {self.name} ({self.location})')
#
#
#
#
# publisher = Publisher("ABCD Publish", "Moscow")
# publisher.publish("Author list")
#
# book_publisher = BookPublisher("Great Books", "Samara", 52)
# book_publisher.publish("Rammov's Earth", "M.B. Rammov")
#
# newspaper_publisher = NewspaperPublisher("Moscow news", "Moscow", 12)
# newspaper_publisher.publish("New version Midjourney")







# TASK 5

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.amount = amount
#         self.__balance += self.amount
#         self.__transactions.append(f"Начисление на счёт {self.amount}")
#
#     def withdraw(self, amount):
#         self.amount = amount
#         self.__balance -= self.amount
#         self.__transactions.append(f"Снятие со счёта {self.amount}")
#
#     def add_interest(self):
#         self.percent = self.__balance * self.__interest_rate
#         self.__balance += self.percent
#         self.__transactions.append(f"Начисление процентов по вкладу: {self.percent}")
#
#     def history(self):
#         resultStr = ""
#         for i in range(len(self.__transactions)):
#             resultStr += self.__transactions[i] + "\n"
#         print(resultStr)
#
#
# account = BankAccount(100000, 0.05)
# account.deposit(15000)
# account.withdraw(7500)
# account.add_interest()
# account.history()











# TASK 6

# class Employee:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#         self.__bonus = 0
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return (self.__salary + self.__bonus)
#
#
# employee = Employee("Badili Rammov", 30, 120000)
# employee.set_bonus(15000)
#
# print(f"Name: {employee.get_name()}")
# print(f"Age: {employee.get_age()}")
# print(f"Salary: {employee.get_salary()}")
# print(f"Bonus: {employee.get_bonus()}")
# print(f"Result Salary: {employee.get_total_salary()}")








# TASK 7

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f'{self.name} подаёт голос')
#
#     def move(self):
#         print(f'{self.name} дергает хвостом')
#
#
# class Dog(Animal):
#     def __init__(self, name, species, legs, breed):
#         super().__init__(name,species,legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f'{self.breed} {self.name} лает')
#
#
# class Bird(Animal):
#     def __init__(self, name,species,legs,wingspan):
#         super().__init__(name,species,legs)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f'{self.species} {self.name} летает')
#
#
#
# dog = Dog("Geralt", "Dog", 4, "Doberman")
# bird = Bird("Vasiliy", "Bird", 2, 10)
#
# dog.voice()
# bird.voice()
#
# dog.move()
# bird.move()
#
# dog.bark()
# bird.fly()





# TASK 8
# Непонятное какое-то задание. В условиях не всё рассказывает что хочет от меня
# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def describe(self):
#         return(f'Это {self.name}. Цвет - {self.color}')
#
#
# class Circle(Shape):
#     def __init__(self, name, color, radius):
#         super().__init__(name,color)
#         self.radius = radius
#
#     def describe(self):
#         print(f'{super().describe()}. Радиус - {self.radius}')
#
#     def area(self):
#         return self.radius**2 * 3.14
#
#
# class Rectangle(Shape):
#     def __init__(self, name, color, length, width):
#         super().__init__(name,color)
#         self.length = length
#         self.width = width
#
#     def describe(self):
#         print(f'{super().describe()}. Длина - {self.length}, ширина - {self.width}')
#
#     def area(self):
#         return (self.length * self.width)
#
#
#
#
# class Triangle(Shape):
#     def __init__(self, name, color, base, height):
#         super().__init__(name,color)
#         self.base = base
#         self.height = height
#
#     def describe(self):
#         print(f'{super().describe()}. Основание - {self.base}, высота - {self.height}')
#
#     def area(self):
#         return (self.base * self.height / 2)
#
#
# shape = Shape("геометрическая фигура", "красный")
# print(shape.describe())
#
# circle = Circle("окружность", "белый", 5)
# circle.describe()
#
# rectangle = Rectangle("прямоугольник", "синий", 3, 4)
# rectangle.describe()
#
# triangle = Triangle("треугольник", "розовый", 6, 8)
# triangle.describe()
#
# print(f'Площадь треугольника: {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()}')









# TASK 9

# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#
#
# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(name,price,weight)
#         self.cocoa_percentage = cocoa_percentage
#         self.chocolate_type = chocolate_type
#
#
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(name,price,weight)
#         self.flavor = flavor
#         self.shape = shape
#
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(name,price,weight)
#         self.flavor = flavor
#         self.filled = filled
#
#
# chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
# gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
# hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)
#
# print("Шоколадные конфеты:")
# print(f"Название конфет: {chocolate.name}")
# print(f"Стоимость: {chocolate.price} руб")
# print(f"Вес брутто: {chocolate.weight} г")
# print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
# print(f"Тип шоколада: {chocolate.chocolate_type}")
# print("\nМармелад жевательный:")
# print(f"Название конфет: {gummy.name}")
# print(f"Стоимость: {gummy.price} руб")
# print(f"Вес брутто: {gummy.weight} г")
# print(f"Вкус: {gummy.flavor}")
# print(f"Форма: {gummy.shape}")
# print("\nФруктовые леденцы:")
# print(f"Название конфет: {hard_candy.name}")
# print(f"Стоимость: {hard_candy.price} руб")
# print(f"Вес брутто: {hard_candy.weight} г")
# print(f"Вкус: {hard_candy.flavor}")
# print(f"Начинка: {hard_candy.filled}")





