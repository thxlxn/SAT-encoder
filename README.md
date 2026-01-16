# Sudoku SAT Encoder
A Python tool that translates a 4×4 Mini-Sudoku puzzle into a Boolean Satisfiability (SAT) formulation. 
<br> It generates a propositional logic formula in Conjunctive Normal Form (CNF) that ensures a valid Sudoku solution.

<br> The resulting encoding in limboole syntax is then printed to the console.

## How It Works
The script maps the 4×4 grid to boolean variables using the format [cell][digit].
- Variables: a1 means "Cell a contains the number 1".
- Total Variables: 16 cells × 4 digits = 64 boolean variables.

## Project Structure
```
.
├── docs
    ├── gc.pdf        # Explains the concept of graph coloring using SAT
    └── origin.pdf    # Description of the original task
├── main.py           # Entry point of the application
└── src
    └── satenc.py     # Core logic for generating SAT clauses

```
