# Recipe Unit Converter

A simple, open-source Python utility for converting common kitchen volume measurements. It is designed to help home cooks and developers working on recipe applications convert measurements quickly.

## Features

- Convert between millilitres (`ml`), teaspoons (`tsp`), tablespoons (`tbsp`), and cups (`cup`).
- Simple command-line interface.
- Input validation for unsupported units.
- No external Python packages required.
- Beginner-friendly code that can be reused or extended.

## Supported Units

| Unit | Meaning |
|---|---|
| `ml` | Millilitre |
| `tsp` | Teaspoon |
| `tbsp` | Tablespoon |
| `cup` | Cup |

**Note:** The converter uses approximate standard volume conversions. Cup and spoon sizes may vary by country and recipe.

## Requirements

- Python 3.8 or later

No additional packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/snikithavavi-debug/recipe-unit-converter.git
```

Move into the project folder:

```bash
cd recipe-unit-converter
```

## Usage

Run the program:

```bash
python converter.py
```

Enter the amount and the source and target units when prompted.

Example:

```text
Enter amount: 2
Convert from (ml/tsp/tbsp/cup): tbsp
Convert to (ml/tsp/tbsp/cup): ml
2.0 tbsp = 29.57 ml
```

Another example:

```text
Enter amount: 1
Convert from (ml/tsp/tbsp/cup): cup
Convert to (ml/tsp/tbsp/cup): ml
1.0 cup = 236.59 ml
```

## How It Works

The program stores conversion factors relative to millilitres. It first converts the supplied amount into millilitres, then converts that intermediate value into the requested unit.

This approach makes it easy to add more volume units in the future.

## Limitations

- Only the four listed volume units are supported.
- Conversions are approximate.
- Weight-to-volume conversions, such as grams of flour to cups, are not supported because ingredient density varies.
- The current version uses a command-line interface rather than a graphical interface.

## Future Improvements

- Add more volume measurements.
- Add automated unit tests.
- Provide an optional web interface.
- Support ingredient-specific conversions where reliable density data is available.

## Contributing

Contributions, bug reports, and suggestions are welcome. Please test changes before submitting them and explain the purpose of each contribution.

## License

This project is released under the MIT License. See the `LICENSE` file for details.
