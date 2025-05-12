import pandas
import numpy
import matplotlib.pyplot as plt
from estimate_price import estimate_price


KM = "km"
PRICE = "price"
LEARNING_RATE = 0.001


def main():
    data = pandas.read_csv("data.csv")
    print(data.shape[0])
    tmp_theta0 = LEARNING_RATE * (estimate_price(data[KM]) - data[PRICE]).sum() / data.shape[0]
    tmp_theta1 = LEARNING_RATE * ((estimate_price(data[KM]) - data[PRICE]) * data[KM]).sum() / data.shape[0]
    print(tmp_theta0)
    print(tmp_theta1)


# def main():
#     data = pandas.read_csv("data.csv")
#     a = ((data[KM] * data[PRICE]).mean() - data[KM].mean() * data[PRICE].mean())/((data[KM]**2).mean() - data[KM].mean()**2)
#     b = data[PRICE].mean() - a * data[KM].mean()
#     x = numpy.array(range(0, 240001, 1000))
#     y = a * x + b
#     fig, ax = plt.subplots()
#     ax.plot(x, y, label=f"y = {a:.2f}x + {b:.2f}", color="red")
#     data.plot(kind="scatter", x=KM, y=PRICE, ax=ax, label="data")
#     plt.legend()
#     plt.show()


if __name__ == "__main__":
    main()
