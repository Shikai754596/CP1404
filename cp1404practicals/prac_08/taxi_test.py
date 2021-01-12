from cp1404practicals.prac_08.taxi import Taxi

def main():
    new_taxi = Taxi("Prius 1", 100, 1.23)
    new_taxi.drive(40)
    print(new_taxi)

main()