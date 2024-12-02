# Base class
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  # in mAh
        self.battery_level = 100  # Battery starts at 100%
    
    def charge(self, amount):
        self.battery_level = min(self.battery_level + amount, 100)
        print(f"{self.model} charged to {self.battery_level}%.")
    
    def use(self, hours):
        battery_drain = hours * 10  # Example: 10% battery drain per hour
        if battery_drain > self.battery_level:
            print(f"Not enough battery to use {self.model} for {hours} hours.")
        else:
            self.battery_level -= battery_drain
            print(f"Used {self.model} for {hours} hours. Battery now at {self.battery_level}%.")
    
    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Battery: {self.battery_capacity}mAh")

# Derived class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_capacity, has_health_monitor):
        super().__init__(brand, model, battery_capacity)
        self.has_health_monitor = has_health_monitor

    def display_info(self):
        health_feature = "Yes" if self.has_health_monitor else "No"
        print(f"Smartwatch: {self.brand} {self.model}, Battery: {self.battery_capacity}mAh, Health Monitor: {health_feature}")

# Test the classes
phone = Smartphone("Samsung", "Galaxy S21", 4000)
phone.display_info()
phone.use(3)
phone.charge(20)

watch = Smartwatch("Apple", "Watch Series 7", 300, True)
watch.display_info()
watch.use(2)
watch.charge(10)
