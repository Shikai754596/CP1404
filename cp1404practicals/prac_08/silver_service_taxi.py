from cp1404practicals.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        fare = self.price_per_km * self.current_fare_distance * self.fanciness + self.flagfall
        return fare

    def __str__(self):
        return "{}, fuel={}, odometer={}, {} on current fare, {:.2f}/km plus flagfall of {}".format(self.name, self.fuel, self.odometer, self.current_fare_distance , (self.price_per_km * self.fanciness), self.flagfall)
