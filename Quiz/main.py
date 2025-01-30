import numpy as np
import random

def generate_map():
    try:
        # Get the number range for the map
        print("Please enter the number range for the map.")
        lower_bound = int(input("Lower bound: "))
        upper_bound = int(input("Upper bound: "))

        if lower_bound >= upper_bound:
            print("Invalid selection: Lower bound must be less than upper bound.")
            return

        # Get the map dimensions
        print("Please enter the map dimensions (e.g., 8x10).")
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))

        if rows <= 0 or columns <= 0:
            print("Invalid selection: Number of rows and columns must be positive.")
            return

        # Create the map
        game_map = np.random.randint(lower_bound, upper_bound + 1, size=(rows, columns))

        # Select random starting coordinates
        start_x = random.randint(0, rows - 1)
        start_y = random.randint(0, columns - 1)

        print("\nGenerated Map:")
        print(game_map)
        print(f"\nRandom Starting Coordinates: (x, y) = ({start_x}, {start_y})")

        # Select a random path
        path_choice = random.randint(1, 3)
        print(f"\nSelected Path: {path_choice}")

        result = 0   

        # Determine movements based on the selected path
        if path_choice == 1:
            print("Selected Path 1")
            movements = [
                (start_x, start_y),
                (start_x, start_y + 1),
                (start_x + 1, start_y + 1),
                (start_x + 2, start_y + 1)
            ]
        elif path_choice == 2:
            print("Selected Path 2")
            movements = [
                (start_x, start_y),
                (start_x, start_y + 1),
                (start_x + 1, start_y + 1),
                (start_x + 1, start_y + 2)
            ]
        elif path_choice == 3:
            print("Selected Path 3")
            movements = [
                (start_x, start_y),
                (start_x, start_y + 1),
                (start_x + 1, start_y + 1),
                (start_x + 1, start_y + 3),
                (start_x, start_y + 3)
            ]

        # Perform XOR operations along the movements
        for (move_row, move_column) in movements:
            move_row = move_row % rows
            move_column = move_column % columns  

            value = game_map[move_row][move_column]
            print(f"XOR {result} ^ {value} = {result ^ value}")
            result ^= value

        # Get a number from the user and perform XOR
        user_number = int(input("\nEnter a number: "))
        print(f"Result XOR {result} ^ {user_number} = {result ^ user_number}")
        result ^= user_number

        print(f"\nFinal Result: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_map()
