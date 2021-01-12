from cp1404practicals.prac_08.taxi import Taxi


def main():
    new_taxi = Taxi(100, "Prius 1")
    new_taxi.drive(40)
    print(new_taxi)
    print("Current fare is {}".format(new_taxi.get_fare()))
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print("Current fare is {}".format(new_taxi.get_fare()))


main()
