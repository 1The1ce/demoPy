class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def display_time(self):
        print(f"Time: {self.hour:02}:{self.minute:02}:{self.second:02}")

class Hour:
    def __init__(self, time_obj):
        self.time_obj = time_obj

    def add_five(self):
        self.time_obj.hour = (self.time_obj.hour + 5) % 24  # Keeps the hour in 24-hour format

class Minute:
    def __init__(self, time_obj):
        self.time_obj = time_obj

    def add_five(self):
        self.time_obj.minute = (self.time_obj.minute + 5) % 60  # Keeps the minute in 60-minute format

class Second:
    def __init__(self, time_obj):
        self.time_obj = time_obj

    def add_five(self):
        self.time_obj.second = (self.time_obj.second + 5) % 60  # Keeps the second in 60-second format

# Initial time
time = Time(10, 30, 45)
print("Initial time:")
time.display_time()

# Modifying the time through each class
hour = Hour(time)
minute = Minute(time)
second = Second(time)

hour.add_five()
minute.add_five()
second.add_five()

# Displaying the modified time
print("Modified time:")
time.display_time()
