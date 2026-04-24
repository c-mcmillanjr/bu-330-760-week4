"""Product lookup module for querying prices from products.json."""

import json


def load_products(path: str = "products.json") -> dict:
    """Load products from a JSON file and return as a dictionary."""
    with open(path, "r") as file:
        return json.load(file)


def lookup(product_name: str, path: str = "products.json") -> str:
    """Look up the price of a product by name (case-insensitive).

    Returns the product name and price if found, or a list of
    available products if the name is not recognized.
    """
    products = load_products(path)
    product_name_lower = product_name.lower()

    for name, price in products.items():
        if name.lower() == product_name_lower:
            return f"{name} costs ${price}"

    available = list(products.keys())
    return f"Product not found. Available products are: {available}"


def list_products(path: str = "products.json") -> None:
    """Print all available products and their prices."""
    products = load_products(path)
    print("Available products:")
    for name, price in products.items():
        print(f"  {name}: ${price}")


if __name__ == "__main__":
    list_products()
    print()

    test_queries = ["Alpha Widget", "gamma widget", "Beta Widget", "Unknown Widget"]
    for query in test_queries:
        print(f"Lookup '{query}': {lookup(query)}")
