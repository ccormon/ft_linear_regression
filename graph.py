import numpy
import matplotlib.pyplot as plt
import pandas
import theta


def main():
    data = pandas.read_csv("data.csv")
    x = numpy.array(range(0, 240001, 1000))
    y = theta.theta0 + theta.theta1 * x
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {theta.theta1:.2f}x + {theta.theta0:.2f}", color="red")
    data.plot(kind="scatter", x="km", y="price", ax=ax, label="data")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
