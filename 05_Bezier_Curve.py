import matplotlib.pyplot as plt


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def nCr(n, r):
    return factorial(n) / float(factorial(r) * factorial(n - r))


def BEZ(n, k, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n-k))


def bezierCurve(xControlPoints, yControlPoints):

    n = len(xControlPoints) - 1
    eps = 0.01
    xCurvePoints = []
    yCurvePoints = []
    u = 0

    while u < 1.01:
        x = 0
        y = 0

        for k in range(0, len(xControlPoints)):
            bez = BEZ(n, k, u)
            x += xControlPoints[k] * bez
            y += yControlPoints[k] * bez

        xCurvePoints.append(x)
        yCurvePoints.append(y)
        u += eps

        plt.clf()
        plt.title("Bezier Curve")

        plt.plot(xControlPoints, yControlPoints, label="Control Graph")
        plt.plot(xCurvePoints, yCurvePoints, label="Bezier Curve")

        plt.legend()
        plt.grid()
        plt.pause(0.01)

    plt.show()


def main():
    xControlPoints = [1, 15, 30, 50]
    yControlPoints = [5, 10, 5, 10]

    bezierCurve(xControlPoints, yControlPoints)


if __name__ == "__main__":
    main()
