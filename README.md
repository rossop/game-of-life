# Game of Life in Python

Welcome to our implementation of Conway's Game of Life in Python! This project provides a Python package for simulating the Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970. Our implementation allows users to explore the fascinating world of cellular automata through an interactive and customisable environment.

## Features

- **Customisable Grid Sizes**: Users can define the size of the simulation grid according to their preferences.
- **Interactive Visualisation**: Utilising [matplotlib](https://matplotlib.org/) or [pygame](https://www.pygame.org/news), the game provides a visual representation of the cell's evolution over time.
- **Pattern Loading and Saving**: Offers the ability to load predefined patterns or save current states to be reused in future simulations.
- **Flexible Ruleset**: While the classic Game of Life rules are the default, our implementation allows for experimenting with alternate rulesets.
- **User Interaction**: Supports starting, pausing, and resetting the simulation, as well as modifying the grid state before or during the simulation.

## Project Structure
```bash
game-of-life/
│
├── gameoflife/          # Main package directory
│   ├── __init__.py      # Initialises the Python package
│   ├── core.py          # Core logic for the Game of Life
│   ├── utils.py         # Utility functions, e.g. pattern loading
│   └── visualisation.py # Visualisation tools
│
├── docs/                # Documentation files
│   ├── index.md         # Homepage of the documentation
│   └── usage.md         # Usage examples and explanations
│
├── tests/               # Automated tests directory
│   ├── __init__.py
│   ├── test_core.py     # Tests for core logic
│   └── test_utils.py    # Tests for utility functions
│
├── examples/            # Example scripts and notebooks
│   └── basic_example.py # Basic usage example
│
├── .gitignore           # Specifies intentionally untracked 
│                        #    files to ignore
├── LICENSE              # License information
├── README.md            # Project overview, installation, 
│                        #    and usage guide
└── setup.py             # Setup script for installing 
                         #    the package

```

## Getting Started

### Prerequisites

Ensure you have Python 3.6+ installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/game-of-life-python.git
    ```
2. Navigate to the cloned directory:
    ```bash
    cd game-of-life
    ```
3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Simulation
To start the Game of Life simulation, run:
```bash
    python -m gameoflife
```

Follow the on-screen instructions to customise your simulation parameters.

## Usage Examples
For more examples and usage, please refer to the Examples directory.

## Development
Want to contribute? Great! Feel free to fork the repository, make your changes, and submit a pull request.

## Testing
To run the automated tests for this project, execute:

```bash
    pytest
```

## License
Distributed under the MIT License. See [LICENSE](LICENCE) for more information.

## Acknowledgements
John Horton Conway, for the original concept of the Game of Life.
The Python community, for the invaluable libraries and tools.
