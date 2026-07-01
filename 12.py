# class SmartLamp:
#     def __init__(self,name,brightness):
#         self.name = name
#         self.brightness = brightness
#         self.is_on = False
    
#     def turn_on(self):
#         self.is_on = True
#         print(f"{self.name} включена")
    
#     def turn_off(self):
#         self.is_on = False
#         print(f"{self.name} выключена")
    
#     def set_brightness(self,value):
#         self.brightness = value
#         print(f"Яркость установлена на {self.brightness}%")
    
#     def show_info(self):
#         status = "включена" if self.is_on else "выключена"
#         print(f"Лампа: {self.name}")
#         print(f"Статус: {status}")
#         print(f"Яркость: {self.brightness}%")

# lamp1 = SmartLamp("Лампа в спальне", 50)
# lamp1.show_info()
# lamp1.turn_on()
# lamp1.set_brightness(90)
# lamp1.show_info()


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance

# account = BankAccount("Alya", 10000)
# account.balance = -500000000
# print(account.balance)


class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Сумма пополнения должна быть больше 0")
            return
        self.__balance += amount
        print(f"Баланс пополнен на {amount}")
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше 0")
            return
        
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount
        print(f"Снято {amount}")

    def get_balance(self):
        print(f"Баланс: {self.__balance}")
    
# account = BankAccount("Alya", 10000)
# account.show_balance()
# print()
# account.deposit(5000)
# print()
# account.show_balance()
# account.__balance = -9999999999
# account.show_balance()


# class Player:
#     def __init__(self,username,health):
#         self.username = username
#         self.__health = health

#     def get_health(self):
#         return self.__health
    
#     def set_health(self,value):
#         if value < 0:
#             self.__health = 0
#         elif value > 100:
#             self.__health = 100
#         else:
#             self.__health = value

# player = Player("Shadow", 80)

# print(player.get_health())
# player.set_health(120)
# print(player.get_health())

# player.set_health(-50)
# print(player.get_health())

class Wallet:
    def __init__(self,owner, money):
        self.owner = owner
        self.__money = money

    def add_money(self,amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        self.__money += amount
        print("Все окей")
    
    def spend_money(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        if amount > self.__money:
            print("Недостаточно денег")
            return
        self.__money -= amount
        print("Все окей")
    
    def get_money(self):
        print(self.owner)
        print(self.__money)

# Наследование

class Transport:
    def __init__(self,type,speed):
        self.type = type
        self.speed = speed
    
    def move(self):
        print(f"{self.type} движется со скоростью {self.speed} км/ч")
    
    def stop(self):
        print(f"{self.type} остановился")

class Car(Transport):
    def open_trunk(self):
        print(f"{self.type}: багажник открыт")

class ElectricCar(Transport):
    def __init__(self,type,speed,battery):
        super().__init__(type,speed)
        self.battery = battery
    
    def charge(self):
        print(f"{self.type} заряжается, Батеерея {self.battery}%")

tesla = ElectricCar("Tesla", 150, 75)
tesla.move()
tesla.charge()


class GameCharacter:
    def __init__(self,name,health,damage):
        self.name = name
        self._health = health
        self._damage = damage

    def attack(self):
        print(f"{self.name} атакует и наносит {self._damage} урона")

    def take_damage(self,amount):
        if amount >= 100:
            print("Слишком большой урон")
            return
        if amount < 0:
            print("Урон не может быть отрицательным")
            return
        self._health -= amount
        if self._health < 0:
            self._health = 0
        
        print(f"{self.name} получил {amount} урона")
        print(f"Здоровье: {self._health}")

    def is_alive(self):
        return self._health > 0
    
class Warrior(GameCharacter):
    def __init__(self,name,health,damage,armor):
        super().__init__(name,health,damage)
        self._armor = armor

    def defend(self):
        print(f"{self.name} защищается щитом. Броня: {self._armor}")

class Mage(GameCharacter):
    def __init__(self,name,health,damage,mana):
        super().__init__(name,health,damage)
        self._mana = mana
    
    def cast_spell(self):
        if self._mana < 10:
            print("Недотаточно маны")
            return
        
        self._mana -= 10
        print(f"{self.name} использует заклинание")
        print(f"Осталось маны: {self._mana}")

warrior = Warrior("Ragnar", 120, 25,50)
mage = Mage("Rilay", 80, 40, 100)

warrior.attack()
warrior.defend()

mage.attack()
mage.cast_spell()


    