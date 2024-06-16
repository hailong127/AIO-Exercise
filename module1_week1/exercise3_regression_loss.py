import numpy as np

def mae(y, y_hat):
    return np.mean(np.abs(y - y_hat))


def mse(y, y_hat):
    return np.mean(np.square(y - y_hat))


def rmse(y, y_hat):
    return np.sqrt(mse(y, y_hat))


def print_statement(loss_name, sample_num, y, y_hat, loss_val):
    print(
        f"loss name: {loss_name.upper()}, sample: {sample_num}, pred: {y}, target: {y_hat}, loss: {loss_val}")


def main():
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number.")
        return

    num_samples = int(num_samples)
    loss_func = input("Input loss name (mae, mse, rmse): ")
    loss_func = loss_func.lower()
    if loss_func not in ["mae", "mse", "rmse"]:
        print("Loss function must be one of the following: mae, mse, rmse.")
        return

    rnd_gen = np.random.default_rng(seed=42)
    for i in range(num_samples):
        y = rnd_gen.uniform(0, 10)
        y_hat = rnd_gen.uniform(0, 10)
        if loss_func == "mae":
            loss_val = mae(y, y_hat)
        elif loss_func == "mse":
            loss_val = mse(y, y_hat)
        else:
            loss_val = rmse(y, y_hat)

        print_statement(loss_func, i, y, y_hat, loss_val)


if __name__ == "__main__":
    main()