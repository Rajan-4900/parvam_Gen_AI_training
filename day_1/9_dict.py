# ============================================================================
# DICTIONARIES IN PYTHON - SIMPLE EXPLANATION WITH PRACTICAL EXAMPLES
# File: 9_decit.py
# ============================================================================

print("=" * 60)
print("PYTHON DICTIONARIES - Tutorial with Practical Examples")
print("=" * 60)

# ---------------------------------------------------------------------------
# 1. WHAT IS A DICTIONARY?
# ---------------------------------------------------------------------------
print("\n1. WHAT IS A DICTIONARY?")
print("-" * 60)
print("A dictionary is an unordered collection of key:value pairs.")
print("Keys are unique and usually immutable (strings, numbers, tuples).")
print("Values can be any Python object and can be duplicated.")

# ---------------------------------------------------------------------------
# 2. CREATING DICTIONARIES
# ---------------------------------------------------------------------------
print("\n2. CREATING DICTIONARIES")
print("-" * 60)

# literal syntax
person = {"name": "Alice", "age": 30, "city": "London"}
print("person:", person)

# from pairs (list of tuples)
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print("dict from pairs:", d)

# empty dict
empty = {}
print("empty dict:", empty)

# ---------------------------------------------------------------------------
# 3. ACCESSING VALUES
# ---------------------------------------------------------------------------
print("\n3. ACCESSING VALUES")
print("-" * 60)

print("Name:", person["name"])            # direct access (KeyError if missing)
print("Age (safe):", person.get("age")) # safe access using get()
print("Country (with default):", person.get("country", "Unknown"))

# ---------------------------------------------------------------------------
# 4. ADDING AND UPDATING
# ---------------------------------------------------------------------------
print("\n4. ADDING AND UPDATING")
print("-" * 60)

person["email"] = "alice@example.com"   # add new key
print("After adding email:", person)

person["age"] = 31                       # update existing key
print("After updating age:", person)

# update with another dict
person.update({"city": "Paris", "language": "English"})
print("After update():", person)

# setdefault returns existing value or sets default
phone = person.setdefault("phone", "Not provided")
print("setdefault phone:", phone)
print("Person now:", person)

# ---------------------------------------------------------------------------
# 5. REMOVING ELEMENTS
# ---------------------------------------------------------------------------
print("\n5. REMOVING ELEMENTS")
print("-" * 60)

removed = person.pop("email")            # remove by key and return value
print("popped email:", removed)
print("After pop email:", person)

# popitem removes and returns an arbitrary (key, value) pair
k, v = person.popitem()
print("popitem removed:", (k, v))
print("After popitem:", person)

# clear all
person.clear()
print("After clear():", person)

# ---------------------------------------------------------------------------
# 6. ITERATING OVER DICTIONARIES
# ---------------------------------------------------------------------------
print("\n6. ITERATING")
print("-" * 60)

scores = {"Alice": 90, "Bob": 75, "Charlie": 85}
print("scores:", scores)

print("Keys:")
for name in scores:
    print(" -", name)

print("Values:")
for s in scores.values():
    print(" -", s)

print("Items:")
for name, score in scores.items():
    print(f" - {name}: {score}")

# ---------------------------------------------------------------------------
# 7. COMMON USES / PRACTICAL EXAMPLES
# ---------------------------------------------------------------------------
print("\n7. PRACTICAL EXAMPLES")
print("-" * 60)

# Example A: Phonebook (mapping names to numbers)
phonebook = {"Alice": "+44-20-0000", "Bob": "+44-20-1111"}
print("Phonebook:", phonebook)

# Add a contact
phonebook["Carol"] = "+44-20-2222"
print("After adding Carol:", phonebook)

# Lookup with default
print("Lookup Dave:", phonebook.get("Dave", "Not found"))

# Example B: Word frequency counter
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("\nWord frequencies:", freq)

# Example C: Grouping items by a key (classifying ages)
people = [("Alice", 30), ("Bob", 22), ("Carol", 30), ("Dave", 22)]
by_age = {}
for name, age in people:
    by_age.setdefault(age, []).append(name)
print("\nGrouped by age:", by_age)

# Example D: Nested dictionaries (config for users)
config = {
    "user1": {"theme": "dark", "lang": "en"},
    "user2": {"theme": "light", "lang": "fr"}
}
print("\nNested config:", config)
print("User1 theme:", config["user1"]["theme"])

# ---------------------------------------------------------------------------
# 8. DICTIONARY COMPREHENSION
# ---------------------------------------------------------------------------
print("\n8. DICTIONARY COMPREHENSION")
print("-" * 60)

nums = [1, 2, 3, 4]
sq = {n: n * n for n in nums}
print("squares:", sq)

# ---------------------------------------------------------------------------
# 9. MERGING DICTIONARIES (PY3.9+ uses |)
# ---------------------------------------------------------------------------
print("\n9. MERGING DICTIONARIES")
print("-" * 60)

a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
merged = {**a, **b}    # b overwrites a for duplicate keys
print("merged (Python 3.5+ style):", merged)

# If Python >=3.9 you can also do: merged2 = a | b

# ---------------------------------------------------------------------------
# 10. SUMMARY - SIMPLE POINTS
# ---------------------------------------------------------------------------
print("\n" + "=" * 40)
print("SUMMARY")
print("=" * 40)
print("1. Dictionary: unordered collection of key:value pairs.")
print("2. Keys must be unique and hashable (immutable).")
print("3. Use dict.get(key, default) for safe lookup.")
print("4. Common methods: keys(), values(), items(), get(), pop(), update().")
print("5. Useful for mapping, counting, grouping, configurations.")
print("\nRun this file to see the examples: python 9_decit.py")
print("=" * 60)
