def main():
    num_item = int(input("Number of items: "))
    while num_item < 0:
        print("Invalid number of items!")
    total_price = 0
    for i in range(num_item):
        total_price += float(input("Price of item: "))
    if total_price > 100:
        total_price = total_price * 0.9
    print("Total price for {} items is ${}".format(num_item, total_price))

main()