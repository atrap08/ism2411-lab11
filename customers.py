"""
Reflection Questions:

1. Bracket notation (dict[key]) is best used when a key is required to exist, so if it's missing, Python raises a KeyError to catch data issues early. .get(key, default) is best used for optional keys or when a default value can be safely used. Rule of thumb: use bracket notation for mandatory fields and .get() for optional fields.

2. Building a summary dictionary with a loop is very similar to using a Pivot Table or SUMIF in Excel. Python's version is more useful for large datasets because it avoids Excel's row limits, executes faster in memory, and allows automated, reproducible data workflows.
"""

# EXERCISE 1 · Beginner: One customer
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print("Exercise 1 Output:")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
print()

# EXERCISE 2 · Beginner: Update and add
customer["phone"] = "555-0199"
print("After adding phone:")
print(customer)

customer["tier"] = "platinum"
print("After updating tier:")
print(customer)

del customer["email"]
print("After deleting email:")
print(customer)
print()

# EXERCISE 3 · Beginner: Safe lookup
email_get = customer.get("email", "no email on file")
print("Exercise 3 - .get():", email_get)

try:
    email_bracket = customer["email"]
    print(email_bracket)
except KeyError as e:
    print(f"Exercise 3 - Bracket lookup raised KeyError: {e}")
print()

# EXERCISE 4 · Beginner: Iterate
print("Exercise 4 Output:")
for key, value in customer.items():
    print(f"{key}: {value}")
print()
# Comment: Iterating with .items() returns both keys and values, whereas iterating over dict directly only yields keys.

# EXERCISE 5 · Intermediate: Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

cust_tier = customer.get("tier", "bronze")
discount_rate = tier_discounts.get(cust_tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Exercise 5 - Tier: {cust_tier}, Discount: {discount_rate * 100:.0f}%, Final Price: ${final_price:.2f}")
print()

# EXERCISE 6 · Intermediate: List of dicts
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "bronze"}
]

print("Exercise 6 Output:")
for c in customers:
    disc_rate = tier_discounts.get(c["tier"], 0)
    disc_amount = 300 * disc_rate
    print(f"{c['name']} ({c['tier']}): Discount on $300 is ${disc_amount:.2f}")
print()

# EXERCISE 7 · Intermediate: Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

print("Exercise 7 Output:")
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} items in stock!")
print()

# EXERCISE 8 · Advanced: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}
for t in transactions:
    r = t["region"]
    sales_summary[r] = sales_summary.get(r, 0) + t["amount"]

print("Exercise 8 Output (Sales by Region):")
for r in sorted(sales_summary.keys()):
    print(f"{r}: {sales_summary[r]}")
