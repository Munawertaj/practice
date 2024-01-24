import matplotlib.pyplot as plt


def pure_pursuit(xBomber, yBomber, xf, yf, fighterSpeed):
    xFighter = []
    yFighter = []
    time = 0
    escapeDistance, caughtDistance = 900, 10

    while True:
        xFighter.append(xf)
        yFighter.append(yf)

        plt.clf()
        plt.title("Simulation of a Pure Pursuit")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")

        plt.plot(xFighter, yFighter, marker=".", label="Fighter")
        plt.plot(xBomber[0: time + 1], yBomber[0: time + 1], marker=".", label="Bomber")

        plt.xlim(-100, 200)
        plt.ylim(-100, 100)
        plt.legend()
        plt.grid()
        plt.pause(1)

        distance = (((xf - xBomber[time]) ** 2 + (yf - yBomber[time]) ** 2) ** 0.5)

        print(f"Time={time} XF={xf:.2f} YF={yf:.2f} XB={xBomber[time]:.2f} YB={yBomber[time]:.2f} Distance={distance:.2f}")

        if distance <= caughtDistance:
            print(f"Target caught at {time} second")
            break
        if distance > escapeDistance or time > len(xBomber):
            print(f"Target escaped at {time} second")
            break

        sin = (yBomber[time] - yf) / distance
        cos = (xBomber[time] - xf) / distance
        time += 1

        xf += fighterSpeed * cos
        yf += fighterSpeed * sin

    plt.show()


def main():
    xb = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
    yb = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
    xf, yf = 0, 50
    speed = 20
    pure_pursuit(xb, yb, xf, yf, speed)


if __name__ == "__main__":
    main()
