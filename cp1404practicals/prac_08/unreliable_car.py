from cp1404practicals.prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        possibility = random.randint(0, 100)
        if self.reliability <= possibility:
            distance = 0
        elif self.reliability > possibility:
            distance = distance
            super().drive(distance)
        return distance

    def __str__(self):
        return "{}, current reliability is {}".format(super().__str__(), self.reliability)

