import pandas


def estimate_price(mileage):
    try:
        theta = pandas.read_csv("theta.csv")
        theta0 = theta.iloc[0, 0]
        theta1 = theta.iloc[0, 1]
        return theta0 + theta1 * mileage
    except Exception as err:
        print(f"Error: {err}")


def main():
    mileage = input("Enter a mileage: ")
    print(estimate_price(int(mileage)))


if __name__ == "__main__":
    main()
