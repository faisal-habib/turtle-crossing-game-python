# Turtle Crossing Game

A small arcade game written in Python with the built-in `turtle` module. Guide
the turtle across a busy road to reach the top of the screen without being hit
by a car. Every successful crossing raises your level and makes the cars faster.

## Features

- Control the turtle with the **Up arrow** key.
- Cars appear at random heights and colors and drive across the screen from the
  right.
- Each crossing increases the level, which is shown at the top left, and speeds
  up all cars.
- The game ends with a **GAME OVER** message when a car hits the turtle.

## Technologies Used

- Python 3
- The Python standard library only: `turtle`, `random` and `time`
  (no third-party packages)

## Project Structure

```
turtle-crossing-game/
├── main.py            # Entry point: creates the window and runs the game loop
├── player.py          # Player: the turtle you control
├── car_manager.py     # CarManager: creates, moves and checks the cars
├── scoreboard.py      # Scoreboard: shows the level and the GAME OVER message
├── README.md          # This file
└── .gitignore
```

## Prerequisites

- **Python 3.9 or newer.** The code uses the `list[Turtle]` type hint, which
  needs 3.9+. It was run and checked with Python 3.12.
- **Tkinter**, which `turtle` uses to draw the window. It is included with the
  standard Python installers for Windows and macOS. On Debian/Ubuntu Linux,
  install it with:

  ```bash
  sudo apt install python3-tk
  ```

You can check that Tkinter is available with:

```bash
python3 -m tkinter
```

A small test window should open.

## Installation

No packages need to be installed. Download or clone the project:

```bash
git clone https://github.com/faisal-habib/turtle-crossing-game.git
cd turtle-crossing-game
```

## How to Run

From the project folder:

```bash
python3 main.py
```

On Windows you may need to use `python main.py` or `py main.py` instead.

## How to Play

1. The turtle starts at the bottom of the window. Your goal is to reach the top.
2. Press the **Up arrow** key to move the turtle forward. Each key press moves
   it a short distance, so tap the key repeatedly.
3. Avoid the cars. If a car touches the turtle, the game is over.
4. When you reach the top, the turtle returns to the start, your level goes up
   and the cars get faster.
5. After **GAME OVER**, click anywhere in the window to close it.

