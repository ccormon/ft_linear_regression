import pandas
import numbers


def estimate_price(mileage: int, theta0: float, theta1: float) -> float | None:
    """This function estimate the price of a car according to the mileage and \
the thetas give in parameter parameter."""
    if not isinstance(mileage, numbers.Number):
        raise ValueError("mileage must be a number.")
    if not isinstance(theta0, numbers.Number):
        raise ValueError("theta0 must be a number.")
    if not isinstance(theta1, numbers.Number):
        raise ValueError("theta1 must be a number.")
    try:
        return theta0 + theta1 * mileage
    except Exception as err:
        print(f"Error: {err}")


def main():
    try:
        mileage = input("Enter a mileage: ")
        try:
            theta = pandas.read_csv("theta.csv")
            if "theta0" not in theta.columns or "theta1" not in theta.columns:
                raise ValueError("theta must contains 'theta0' and 'theta1' \
columns.")
            theta0 = theta["theta0"].values[0]
            theta1 = theta["theta1"].values[0]
        except Exception:
            theta0 = 0
            theta1 = 0
        print(estimate_price(int(mileage), theta0, theta1))
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
