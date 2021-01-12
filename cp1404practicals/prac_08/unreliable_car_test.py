from cp1404practicals.prac_08.unreliable_car import UnreliableCar
import random


def main():
    new_car = UnreliableCar(100, "New Car", 50)
    while new_car.fuel != 0:
        new_car.drive(random.randint(0, 50))
        print(new_car)



main()
