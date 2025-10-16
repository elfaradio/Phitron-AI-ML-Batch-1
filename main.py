class Phone:
    category = "Electronics"

    def __init__(self, model, battery, camera):
        self.model = model
        self.battery = battery
        self.camera = camera


apple = Phone()

print(apple.category)
