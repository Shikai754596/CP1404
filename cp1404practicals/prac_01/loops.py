def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for t in range(0, 101, 10):
        print(t, end=' ')
    print()

    for y in range(20, 0, -1):
        print(y, end=' ')
    print()

    stars_num = int(input("Number of stars: "))
    for s in range(stars_num):
        print("*", end='')
    print()

    incr_stars = int(input("Number of stars: "))
    for w in range(incr_stars):
        for k in range(w + 1):
            print("*", end='')
        print()
    print()


main()
