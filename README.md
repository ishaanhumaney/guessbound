# GuessBound

A lightweight, robust command-line number guessing game built in pure Python. It handles invalid entries, enforces boundary constraints, and features a deterministic loop that handles user state across multiple replays.

It is designed to showcase clean conditional logic, basic exception filtering, and streamlined interactive terminal feedback without external dependencies.

## Key Features
* **State Control:** Maintains player history and allows seamless game restarts without program interruption.
* **Input Resilience:** Uses isolated try-except blocks to catch string-to-integer conversion failures without crashing.
* **Boundary Validation:** Actively filters guesses outside the logical 1–100 range before burning user attempts.
* **Dynamic UX:** Tracks attempt tracking and reduces maximum tries linearly while adjusting terminal hints.

## Tech Stack Breakdown
* **Core Engine:** Python 3.x (Standard Library only)
* **Randomization:** `random.randint` pseudo-random generation
* **CI Pipeline:** GitHub Actions for passive script compilation checks

## Quick Start

### Run via GitHub Codespaces (100% Browser-Based)
1. Click the **Code** button at the top right of this repository.
2. Select the **Codespaces** tab, then click **Create codespace on main**.
3. Once the web-based container loads, open the terminal and type:
   ```bash
   python main.py

### Quick Local Running
If you have Python installed locally, run the script directly:
  python main.py

## Project Structure

├── .github/

│      └── workflows/

│             └── ci.yml      # Continuous integration setup

├── .gitignore                # Environment filter files

├── main.py                   # Main game executable and logic

└── README.md                 # Documentation

## Roadmap

[ ] Add difficulty scaling (toggling target numbers up to 500 or lowering total attempts).

[ ] Track high scores/lowest attempt counts across replays using local session memory.

[ ] Introduce a simple scoring system based on performance speed.
