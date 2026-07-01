class SmartLamp:
    def __init__(self,name,brightness):
        self.name = name
        self.brightness = brightness
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} включена")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} выключена")
    
    def set_brightness(self,value):
        self.brightness = value
        print(f"Яркость установлена на {self.brightness}%")
    
    def show_info(self):
        status = "включена" if self.is_on else "выключена"
        print(f"Лампа: {self.name}")
        print(f"Статус: {status}")
        print(f"Яркость: {self.brightness}%")

lamp1 = SmartLamp("Лампа в спальне", 50)
lamp1.show_info()
lamp1.turn_on()
lamp1.set_brightness(90)
lamp1.show_info()
