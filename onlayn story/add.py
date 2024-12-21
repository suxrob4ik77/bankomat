import json


def add_kart():
    a = input("Moshina qoshing==")
    if  a=="1":
         cars = {}
         with open("python/de.txt", "r") as file:

             try:
                cars = json.load(file)
             except Exception as file:
                cars = {}
         car_number = input("Moshina raqamini qoshing")

         tex_pass = input("Tex raqam qoshing")
         egasi = input("Egasini ismi")
         time_cars = input("Vaqtini qashing")
         cars[car_number] = {
            "Tex raqam qoshing" : tex_pass,
            "Egasini ismi" :egasi,
            "Vaqtini qashing": time_cars
         }
         with open("python/de.txt", "w") as file:
            json.dump(cars, file, indent = 4)
    else:
         print("XATOOOOOOO")
# add_kart()
