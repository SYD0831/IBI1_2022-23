class Triathlon(object):
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time
    
    def print_details(self):
        print(f"{self.first_name} {self.last_name} competed at {self.location} with times: swim - {self.swim_time}s, cycle - {self.cycle_time}s, run - {self.run_time}s, total - {self.total_time}s")

# Example usage
athlete = Triathlon("John", "Doe", "New York", 600, 1800, 1200)
athlete.print_details()