import matplotlib.pyplot as plt
import decimal
import pandas as pd


class Regression:

    def float_range(start, stop, step):
        start = decimal.Decimal(start)
        stop = decimal.Decimal(stop)
        while start < stop:
            yield float(start)
            start += decimal.Decimal(step)

    def __init__(self, data_x=None, data_y=None):
        if data_x is not None and data_y is not None:
            self.data_x = list(data_x)
            self.data_y = list(data_y)

    def read_csv(self, file=None, filepath=''):
        if file is None:
            with open(filepath) as file:
                data = pd.read_csv(file)
        else:
            data = pd.read_csv(file)

        data = pd.DataFrame(data)
        c1, c2 = data.columns

        self.data_x = list(data[c1])
        self.data_y = list(data[c2])

    def linear_regression(self):
        data_x = self.data_x
        data_y = self.data_y
        rho = sum(data_x)  # Sum xi
        gamma = sum(data_y)  # Sum Yi
        h = sum(x*x for x in data_x)  # Sum xi^2
        phi = sum(x*y for (x, y) in zip(data_x, data_y))  # Sum xi*yi
        N = min(len(data_x), len(data_y))  # Amount of data

        c_intercept = (rho*phi - h*gamma)/(rho*rho - h*N)
        m_slope = (gamma/rho) - (N*(rho*phi - h*gamma))/(rho*rho*rho - h*N*rho)

        return (m_slope, c_intercept)

    def plot_linear_regression(self):
        data_x = self.data_x
        data_y = self.data_y
        m_slope, c_intercept = self.linear_regression()

        r_max = max(self.data_x)
        r_min = min(self.data_x)

        x_axis = list(Regression.float_range(
            str(r_min), str(r_max), str((r_max-r_min)/1000)))

        plt.title("m = " + str(round(m_slope,4)) + ", c = "+str(round(c_intercept,4)))
        plt.plot(data_x, data_y, 'o')
        plt.plot(x_axis, [r*m_slope + c_intercept for r in x_axis])
        plt.show()

    def info(self):
        print("m =", m_slope)
        print("c =", c_intercept)
        print("R-Square =", 100*Regression.error_rsq(m_slope,
              c_intercept, data_x, data_y), "%")

    def error_rsq(m, c, xi, yi):
        y_reg = [m*x+c for x in xi]
        y_mean = sum(yi)/len(yi)
        sst = sum([(y-y_mean)**2 for y in yi])
        ssr = sum([(y-y_mean)**2 for y in y_reg])
        return ssr/sst


if __name__ == "__main__":
    with open("regression_example.csv") as file:
        data = pd.read_csv(file)

    data = pd.DataFrame(data)
    c1, c2 = data.columns

    data_x = list(data[c1])
    data_y = list(data[c2])

    r_max = max(data_x)
    r_min = min(data_x)

    x_axis = list(Regression.float_range(
        str(r_min), str(r_max), str((r_max-r_min)/1000)))

    rho = sum(data_x)  # Sum xi
    gamma = sum(data_y)  # Sum Yi
    h = sum(x*x for x in data_x)  # Sum xi^2
    phi = sum(x*y for (x, y) in zip(data_x, data_y))  # Sum xi*yi
    N = min(len(data_x), len(data_y))  # Amount of data

    c_intercept = (rho*phi - h*gamma)/(rho*rho - h*N)
    m_slope = (gamma/rho) - (N*(rho*phi - h*gamma))/(rho*rho*rho - h*N*rho)

    print("m =", m_slope)
    print("c =", c_intercept)
    print("R-Square =", 100*Regression.error_rsq(m_slope,
          c_intercept, data_x, data_y), "%")

    plt.plot(data_x, data_y, 'o')
    plt.plot(x_axis, [r*m_slope + c_intercept for r in x_axis])
    plt.show()
