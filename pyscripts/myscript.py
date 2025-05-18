import random
import time

def cool_ascii_fireworks():
    fireworks = [
        "        *",
        "       ***",
        "      *****",
        "    *********",
        "  *************",
        "*****************",
        "      *****",
        "      *****",
        "      *****"
    ]
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    reset = "\033[0m"
    for _ in range(5):
        color = random.choice(colors)
        for line in fireworks:
            print(color + line.center(40) + reset)
            time.sleep(0.1)
        print("\n" * 2)
        time.sleep(0.5)

if __name__ == "__main__":
    print("Enjoy the fireworks show!\n")
    cool_ascii_fireworks()