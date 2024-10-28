import random
import time

def display_intro():
  """Displays the welcome message and game instructions."""
  print("Welcome to the Model Rocket Terminal Simulator!")
  print("You are about to launch your very own model rocket.")
  print("Make careful choices to ensure a successful flight!")
  print("--------------------------------------------------")

def get_rocket_type():
  """Asks the user to choose a rocket type."""
  while True:
    print("Choose your rocket type:")
    print("1. Beginner Rocket (Short flight, easy to control)")
    print("2. Intermediate Rocket (Longer flight, more challenging)")
    print("3. Advanced Rocket (High altitude, complex maneuvers)")
    choice = input("Enter your choice (1-3): ")
    if choice in ['1', '2', '3']:
      return int(choice)
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")

def get_engine_power():
  """Asks the user to choose an engine power level."""
  while True:
    print("Choose your engine power:")
    print("1. Low Power (Gentle ascent, short flight)")
    print("2. Medium Power (Moderate ascent, longer flight)")
    print("3. High Power (Powerful ascent, high altitude)")
    choice = input("Enter your choice (1-3): ")
    if choice in ['1', '2', '3']:
      return int(choice)
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")

def launch_sequence():
  """Simulates the rocket launch sequence."""
  print("--------------------------------------------------")
  print("3... 2... 1... LIFT OFF!")
  print("The rocket ascends with a roar...")
  time.sleep(2)

def flight_simulation(rocket_type, engine_power):
  """Simulates the rocket's flight based on chosen parameters."""
  print("--------------------------------------------------")
  altitude = 0
  flight_time = 0
  max_altitude = 0

  while altitude >= 0:
    flight_time += 1
    if rocket_type == 1:
      altitude_change = random.randint(1, 5)
    elif rocket_type == 2:
      altitude_change = random.randint(3, 8)
    else:
      altitude_change = random.randint(5, 12)

    if engine_power == 1:
      altitude_change -= 1
    elif engine_power == 2:
      altitude_change -= 2
    else:
      altitude_change -= 3

    altitude += altitude_change
    max_altitude = max(max_altitude, altitude)

    print(f"Flight Time: {flight_time} seconds, Altitude: {altitude} meters")
    time.sleep(1)

  print("--------------------------------------------------")
  print(f"The rocket has reached its peak altitude of {max_altitude} meters.")
  print("It is now descending...")
  time.sleep(2)

  if altitude < -10:
    print("The rocket has crashed! Better luck next time.")
  else:
    print("The rocket has landed safely!")

def play_again():
  """Asks the user if they want to play again."""
  while True:
    choice = input("Do you want to launch another rocket? (y/n): ").lower()
    if choice in ['y', 'n']:
      return choice == 'y'
    else:
      print("Invalid choice. Please enter 'y' or 'n'.")

def main():
  """The main function of the program."""
  display_intro()

  while True:
    rocket_type = get_rocket_type()
    engine_power = get_engine_power()

    launch_sequence()
    flight_simulation(rocket_type, engine_power)

    if not play_again():
      break

if __name__ == "__main__":
  main()
