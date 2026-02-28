#Question - A
base_fare = "4500.75"
tax_percent = "5"

base_fare = float(base_fare)
tax_percent = float(tax_percent)

final_fare = base_fare + (base_fare * tax_percent / 100)
print(f"Final fare after tax: {final_fare}")

print("=======================")

#Question - B
seat_numbers = "12A,12B,14C,15D"

seat_list = list(seat_numbers.split(","))
print("seat list:", seat_list)  

print("=======================")

#Question - C
seat_list = set(seat_list)
print("seat list:", seat_list)

print("=======================")


#Question - D

is_international = "True"
is_international = is_international == "True"
print(f"Is the flight international? {is_international}")

print("=======================")

#question - E

flight_details ={
"flight_number" : "AI-202",
"final_fare" : int(final_fare),
"seat numbers" : tuple(seat_list)
}