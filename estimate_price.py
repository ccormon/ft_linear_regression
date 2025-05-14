import pandas
import theta


def estimate_price(mileage: int, theta0: float, theta1: float) -> float | None:
    try:
        return theta.theta0 + theta.theta1 * mileage
    except Exception as err:
        print(f"Error: {err}")


def main():
    mileage = input("Enter a mileage: ")
    print(estimate_price(int(mileage), theta.theta0, theta.theta1))


if __name__ == "__main__":
    main()
