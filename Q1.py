class flight:
    def __init__(self, flight_no, source , destination, base_fare):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.base_fare = base_fare

    def display_details(self):
        print(f"Flight Number: {self.flight_no}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Base Fare: {self.base_fare}")
    
    def get_flight_info(self):
        return f"{self.flight_no} from {self.source} to {self.destination}"
    
    def calculate_final_fare(self, passenger_count):
        final_fare = self.base_fare * passenger_count
        return final_fare
    def calculate_final_discounted_fare(self, passenger_count, discount_percent):
        final_fare = self.base_fare * passenger_count
        total_fare = final_fare - (final_fare * discount_percent / 100)
        return total_fare
    
    def updated_route(self, updated_source):
        self.source = updated_source

    def updated_route(self, updated_source, updated_destination):
        self.source = updated_source
        self.destination = updated_destination

F1 = flight("Indigo - 777", "Kashmir", "Kanyakumari", 25000)
F1.display_details()
print(F1.get_flight_info())


F1.updated_route("Mumbai")
print("updated_route",  "From" ,F1.source, "To", F1.destination)

F1.updated_route("Delhi", "Chennai")
print("updated_route",  "From" ,F1.source, "To", F1.destination)
