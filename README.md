
# Package Sorter

This is a simple Python script that classifies packages into the correct stack based on their volume and mass. It's designed for use in an automated robotic dispatch system.

## Objective

Sort packages into one of three categories:

- **STANDARD**: Not bulky and not heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

## Rules

A package is:

- **Bulky** if:
  - Volume ≥ 1,000,000 cm³ **OR**
  - Any dimension ≥ 150 cm

- **Heavy** if:
  - Mass ≥ 20 kg

## Function

```python
def sort(width, height, length, mass):
    # Returns one of: "STANDARD", "SPECIAL", "REJECTED"
````

## Running Tests

To run the built-in tests:

```bash
python test.py
```

You should see:

```
All tests OK.
```

## Requirements

Just Python 3 — no external libraries needed.

## File Structure

* `main.py`: contains the sorting logic and tests.
* `test.py` : test cases
* `README.md`: you're reading it.

## Example

```python
sort(100, 100, 100, 10)
# Output: 'STANDARD'
```
