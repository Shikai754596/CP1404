from cp1404practicals.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        fare = super().get_fare() + self.flagfall
        return fare

    def __str__(self):
        return "{} plus flagfall of {}".format (super().__str__(), self.flagfall)
