"""
File: batyrov_project_setup.py
Purpose: Automate project folder creation for analytics.
Author: Bakhrom Botirov
"""

# -----------------------------------------
# Imports
# -----------------------------------------
from pathlib import Path
from utils_batyrov import get_byline   # reuse your byline from Module 1

# -----------------------------------------
# Functions
# -----------------------------------------

def create_folder(folder_name: str) -> None:
    """Create a single folder."""
    path = Path(folder_name)
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created folder: {path}")


def create_year_folders(base: str, start: int, end: int) -> None:
    """Create multiple folders for each year in a range."""
    for year in range(start, end + 1):
        path = Path(base) / str(year)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {path}")


def squared_numbers(nums: list[int]) -> list[int]:
    """Return a list of squared numbers using list comprehension."""
    return [n**2 for n in nums]


def check_sales(sales: int) -> str:
    """Return a message based on sales numbers."""
    if sales > 10000:
        return "High sales, allocate more resources!"
    elif sales > 5000:
        return "Moderate sales, monitor closely."
    else:
        return "Low sales, consider promotions."


# -----------------------------------------
# Main Function
# -----------------------------------------

def main():
    """Run project setup tasks."""
    # Print byline from Module 1
    print(get_byline())

    # Create a single folder
    create_folder("data")

    # Create multiple year folders
    create_year_folders("data", 2021, 2024)

    # Demonstrate list comprehension
    nums = [1, 2, 3, 4, 5]
    print("Squared numbers:", squared_numbers(nums))

    # Demonstrate branching
    print(check_sales(12000))
    print(check_sales(6000))
    print(check_sales(2000))


# -----------------------------------------
# Conditional Execution
# -----------------------------------------

if __name__ == "__main__":
    main()