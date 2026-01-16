import itertools

def generate_sudoku_encoding():
    """
    Generates the propositional logic encoding for a 4x4 Sudoku
    using the "a1, a2..." variable naming scheme
    (e.g., g4 = True means we have to put number 4 in the cell at row 2, column 3)
    The result is printed to the console.
    """
    
    print("Welcome to the Sudoku SAT Encoder")
    print("+---+---+---+---+ \n| a | b | c | d | \n+---+---+---+---+ \n| e | f | g | h | \n+---+---+---+---+ \n| i | j | k | l | \n+---+---+---+---+ \n| m | n | o | p | \n+---+---+---+---+")

    print("\nSelect encoding mode:")
    print("1. Standard [Empty Sudoku]")
    print("2. Custom [Specify Filled Cells]")
    print("3. Abort [Exit Encoder]")
    choice = input("Enter selection (1/2/3): ").strip()

    user_clauses = []

    if choice == "2":
        user_input = input("Enter filled cells separated by commas (e.g. d4, a1, k1, m2, p3): ")
        if user_input.strip():
            items = user_input.split(",")
            for item in items:
                clean_item = item.strip()
                if clean_item:
                    user_clauses.append(f"({clean_item})")
    elif choice == "3":
        print("Exiting...")
        return None

    # the grid structure is the english alphabet from left to right
    rows = [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']
    ]
    
    cols = [
        ['a', 'e', 'i', 'm'],
        ['b', 'f', 'j', 'n'],
        ['c', 'g', 'k', 'o'],
        ['d', 'h', 'l', 'p']
    ]
    
    blocks = [
        ['a', 'b', 'e', 'f'],
        ['c', 'd', 'g', 'h'],
        ['i', 'j', 'm', 'n'],
        ['k', 'l', 'o', 'p']
    ]
    
    all_cells = [cell for row in rows for cell in row]
    digits = [1, 2, 3, 4]
    all_clauses = []

    for cell in all_cells:
        clause_parts = []
        for d in digits:
            clause_parts.append(f"{cell}{d}")
        all_clauses.append(f"({' | '.join(clause_parts)})")

    for cell in all_cells:
        for d1, d2 in itertools.combinations(digits, 2):
            all_clauses.append(f"(!{cell}{d1} | !{cell}{d2})")
    
    def add_connected_constraints(cell_group_list, group_name=""):
        """
        Generates different color constraints for a list of cell groups
        (e.g., a list of rows, list of columns, or list of blocks).
        """
        for i, cell_group in enumerate(cell_group_list):
            for cell1, cell2 in itertools.combinations(cell_group, 2):
                for d in digits:
                    all_clauses.append(f"(!{cell1}{d} | !{cell2}{d})")

    add_connected_constraints(rows, "Row")
    add_connected_constraints(cols, "Column")
    add_connected_constraints(blocks, "Block")

    all_clauses.extend(user_clauses)

    full_encoding = " & \n".join(all_clauses)
    
    print("--- START OF SUDOKU ENCODING ---")
    print(full_encoding)
    print("--- END OF SUDOKU ENCODING ---")
    print(f"\nTotal clauses generated: {len(all_clauses)}")