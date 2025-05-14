import pandas
import numpy
import theta


KM = "km"
PRICE = "price"
LEARNING_RATE = 0.01


def standardize(feature: numpy.ndarray) -> tuple[numpy.ndarray, float, float]:
    """Standardize each values from the feature."""
    mean = feature.mean()
    std = feature.std()
    return (feature - mean) / std, mean, std


def gradient_descent(km: numpy.ndarray, price: numpy.ndarray, theta0: int = 0, theta1: int = 0) -> tuple[float, float]:
    for i in range(1000):
        predicted_price = theta0 + theta1 * km
        theta0 -= LEARNING_RATE * (predicted_price - price).mean()
        theta1 -= LEARNING_RATE * ((predicted_price - price) * km).mean()
    return theta0, theta1


def main():
    data = pandas.read_csv("data.csv")
    km, price = data[KM].values, data[PRICE].values
    km_scaled, km_mean, km_std = standardize(km)
    price_scaled, price_mean, price_std = standardize(price)
    theta0_scaled, theta1_scaled = gradient_descent(km_scaled, price_scaled)
    theta.theta1 = theta1_scaled * price_std / km_std
    theta.theta0 = price_std * theta0_scaled - theta.theta1 * km_mean + price_mean


if __name__ == "__main__":
    main()
