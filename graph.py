import numpy
import matplotlib.pyplot as plt
import pandas
import numbers


def draw_graph(data: pandas.DataFrame, theta0: float, theta1: float) -> None:
    """This function draws the graph which represents the data with a scatter \
plot and draws the linear regression line of the data."""
    if not isinstance(data, pandas.DataFrame):
        raise ValueError("data must be a pandas' DataFrame.")
    if "km" not in data.columns or "price" not in data.columns:
        raise ValueError("data must contains 'km' and 'price' columns.")
    if not isinstance(theta0, numbers.Number):
        raise ValueError("theta0 must be a number.")
    if not isinstance(theta1, numbers.Number):
        raise ValueError("theta1 must be a number.")
    x = numpy.array(range(0, data["km"].max() + 1, 1000))
    y = theta0 + theta1 * x
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {theta1:.2f}x + {theta0:.2f}", color="red")
    data.plot(kind="scatter", x="km", y="price", ax=ax, label="data")
    plt.legend()
    plt.show()


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
        draw_graph(data, theta0, theta1)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
