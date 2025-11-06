import pandas
import numbers


def precision(data: pandas.DataFrame, theta0: float, theta1: float) -> float:
    """This function calculate the precision of the algorithm trained. It \
gives the average of the errors."""
    if not isinstance(data, pandas.DataFrame):
        raise ValueError("data must be a pandas' DataFrame.")
    if "km" not in data.columns or "price" not in data.columns:
        raise ValueError("data must contains 'km' and 'price' columns.")
    if not isinstance(theta0, numbers.Number):
        raise ValueError("theta0 must be a number.")
    if not isinstance(theta1, numbers.Number):
        raise ValueError("theta1 must be a number.")
    return abs(theta0 + theta1 * data["km"] - data["price"]).mean()


def main():
    try:
        data = pandas.read_csv("data.csv")
        if "km" not in data.columns or "price" not in data.columns:
            raise ValueError("data must contains 'km' and 'price' columns.")
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
        print(f"Precision = {precision(data, theta0, theta1):.2f}")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
