import random
import time

# Function to display cool ASCII fireworks animation
def cool_ascii_fireworks():
    # List of strings representing the firework shape
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
    # ANSI color codes for colorful output
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    reset = "\033[0m"  # Reset color code
    for _ in range(5):  # Repeat the fireworks show 5 times
        color = random.choice(colors)  # Pick a random color for each show
        for line in fireworks:
            # Print each line of the firework, centered and colored
            print(color + line.center(40) + reset)
            time.sleep(0.1)  # Short pause for animation effect
        print("\n" * 2)  # Add space between fireworks
        time.sleep(0.5)   # Pause before next firework

if __name__ == "__main__":
    print("Enjoy the fireworks show!\n")
    cool_ascii_fireworks()