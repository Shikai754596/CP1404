from cp1404practicals.prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi(100, "Hummer", 2)
    silver_taxi.drive(18)
    print(silver_taxi)
    print("The fare is ${}".format(silver_taxi.get_fare()))


main()
