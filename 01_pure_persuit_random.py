import matplotlib.pyplot as plt
import random
import sys


def purePersuit(fighterSpeed):
    xf = random.uniform(1, 1000)
    yf = random.uniform(1, 1000)
    xb = random.uniform(1, 1000)
    yb = random.uniform(1, 1000)

    xFighter = []
    yFighter = []
    xBomber = []
    yBomber = []

    time = 0
    escapeDistance = 900
    caughtDistance = 100

    with open('output.txt', 'w') as output_file:
        sys.stdout = output_file

        while True:
            xFighter.append(xf)
            yFighter.append(yf)
            xBomber.append(xb)
            yBomber.append(yb)

            plt.clf()
            plt.title("Simulation of a Pure Pursuit")
            plt.xlabel("X Position")
            plt.ylabel("Y Position")
            
            plt.plot(xFighter, yFighter, marker = ".", label="Fighter")
            plt.plot(xBomber, yBomber, marker = ".",label="Bomber")

            plt.xlim(-1000, 1200)
            plt.ylim(-1000, 1200)
            plt.legend()
            plt.grid()
            plt.pause(1)


            distance = ((yb - yf) ** 2 + (xb-xf) ** 2) ** 0.5

            print(f"Time = {time}\t XF = {xf:.2f}\t YF = {yf:.2f}\t XB = {xb:.2f}\t YB = {yb:.2f}\t Distance = {distance:.2f}")

            if distance <= caughtDistance:
                print(f"Bomber caught at {time} seconds")
                break
            if distance >= escapeDistance:
                print(f"Bomber escaped from Fighter at {time} seconds")
                break
            
            sin = (yb - yf) / distance
            cos = (xb - xf) / distance
            time += 1

            xf += fighterSpeed * cos
            yf += fighterSpeed * sin

            xb += random.uniform(-100, 100)
            yb += random.uniform(-100, 100)
        
        plt.show


def main():

    speed = int(input("Enter the Fighter Speed: "))

    purePersuit(speed)

if __name__ == "__main__":
    main()
