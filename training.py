import pandas
import numpy
import numbers


LEARNING_RATE = 0.01


def standardize(feature: numpy.ndarray) -> tuple[numpy.ndarray, float, float]:
    """This fucntion standardize each values from the feature."""
    if not isinstance(feature, numpy.ndarray):
        raise ValueError("feature must be a numpy's array.")
    if feature.ndim != 1:
        raise ValueError("feature must me a 1D array.")
    mean = feature.mean()
    std = feature.std()
    return (feature - mean) / std, mean, std


def gradient_descent(
    km: numpy.ndarray,
    price: numpy.ndarray,
    theta0: float = 0,
    theta1: float = 0
) -> tuple[float, float]:
    """This function apply a gradient descent algorithm to find an accepteble \
linear regression line equation and returns the slope and the y-intercept of \
the equation."""
    if not isinstance(km, numpy.ndarray):
        raise ValueError("km must be a numpy's array.")
    if km.ndim != 1:
        raise ValueError("km must be a 1D array.")
    if not isinstance(price, numpy.ndarray):
        raise ValueError("price must be a numpy's array.")
    if price.ndim != 1:
        raise ValueError("price must be an 1D array.")
    if not isinstance(theta0, numbers.Number):
        raise ValueError("theta0 must be a number.")
    if not isinstance(theta1, numbers.Number):
        raise ValueError("theta1 must be a number.")
    for i in range(1000):
        predicted_price = theta0 + theta1 * km
        theta0 -= LEARNING_RATE * (predicted_price - price).mean()
        theta1 -= LEARNING_RATE * ((predicted_price - price) * km).mean()
    return theta0, theta1


def training(data: pandas.DataFrame, theta: pandas.DataFrame) -> None:
    """This function standardize the values from each columns of datas \
parameter, then applies a gradient descent algorithm to find good values for \
the thetas from theta parameter. The new thetas values are destandardize \
before the saving."""
    if not isinstance(data, pandas.DataFrame):
        raise ValueError("data must be a pandas' DataFrame.")
    if "km" not in data.columns or "price" not in data.columns:
        raise ValueError("data must contains 'km' and 'price' columns.")
    if not isinstance(theta, pandas.DataFrame):
        raise ValueError("theta must be a pandas' DataFrame.")
    if "theta0" not in theta.columns or "theta1" not in theta.columns:
        raise ValueError("theta must contains 'theta0' and 'theta1' columns.")
    km, price = data["km"].values, data["price"].values
    km_scaled, km_mean, km_std = standardize(km)
    price_scaled, price_mean, price_std = standardize(price)
    theta0_scaled, theta1_scaled = gradient_descent(km_scaled, price_scaled)
    theta1 = theta1_scaled * price_std / km_std
    theta0 = price_std * theta0_scaled - theta1 * km_mean + price_mean
    theta.loc[0, "theta0"] = theta0
    theta.loc[0, "theta1"] = theta1


def main():
    try:
        data = pandas.read_csv("data.csv")
        theta = pandas.DataFrame({
            "theta0": [0],
            "theta1": [0]
        })
        training(data, theta)
        theta.to_csv("theta.csv", index=False)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
