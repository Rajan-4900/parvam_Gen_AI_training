# ============================================================================
# SET IN PYTHON
# ============================================================================
# A set is an unordered collection of unique elements
# Sets are mutable (can be modified) but can only contain immutable elements
# Sets use curly braces {} and are useful for removing duplicates and membership testing
# ============================================================================

print("=" * 60)
print("PYTHON SETS - Tutorial with Practical Examples")
print("=" * 60)

# ============================================================================
# 1. CREATING SETS
# ============================================================================
print("\n1. CREATING SETS")
print("-" * 60)

# Creating an empty set
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

# Creating a set with elements
fruits = {"apple", "banana", "orange", "mango"}
print(f"\nFruits set: {fruits}")

# Creating a set from a list
numbers = [1, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = set(numbers)
print(f"List with duplicates: {numbers}")
print(f"Set from list (duplicates removed): {unique_numbers}")

# ============================================================================
# 2. SET PROPERTIES
# ============================================================================
print("\n\n2. SET PROPERTIES")
print("-" * 60)

# Sets are unordered
set1 = {1, 2, 3}
print(f"Set 1: {set1}")
print("Note: Sets are unordered, so order may vary each run")

# Sets contain only unique elements
duplicate_set = {1, 1, 2, 2, 3, 3}
print(f"\nSet with duplicates input: {{1, 1, 2, 2, 3, 3}}")
print(f"Result: {duplicate_set}")

# ============================================================================
# 3. ADDING AND REMOVING ELEMENTS
# ============================================================================
print("\n\n3. ADDING AND REMOVING ELEMENTS")
print("-" * 60)

colors = {"red", "blue", "green"}
print(f"Original set: {colors}")

# Add a single element
colors.add("yellow")
print(f"After add('yellow'): {colors}")

# Remove an element (raises error if not found)
colors.remove("red")
print(f"After remove('red'): {colors}")

# Discard an element (doesn't raise error if not found)
colors.discard("purple")  # Doesn't exist, but no error
print(f"After discard('purple'): {colors}")

# Pop removes and returns an arbitrary element
removed = colors.pop()
print(f"After pop(): {colors} (removed: {removed})")

# Clear removes all elements
colors.clear()
print(f"After clear(): {colors}")

# ============================================================================
# 4. SET OPERATIONS
# ============================================================================
print("\n\n4. SET OPERATIONS")
print("-" * 60)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union - all elements from both sets
union = set_a.union(set_b)
union_alt = set_a | set_b
print(f"\nUnion (A | B): {union}")

# Intersection - common elements
intersection = set_a.intersection(set_b)
intersection_alt = set_a & set_b
print(f"Intersection (A & B): {intersection}")

# Difference - elements in A but not in B
difference = set_a.difference(set_b)
difference_alt = set_a - set_b
print(f"Difference (A - B): {difference}")

# Symmetric difference - elements in either A or B but not both
sym_diff = set_a.symmetric_difference(set_b)
sym_diff_alt = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {sym_diff}")

# ============================================================================
# 5. MEMBERSHIP TESTING
# ============================================================================
print("\n\n5. MEMBERSHIP TESTING")
print("-" * 60)

animals = {"cat", "dog", "bird", "fish"}
print(f"Animals set: {animals}")

print(f"\n'cat' in animals: {'cat' in animals}")
print(f"'lizard' in animals: {'lizard' in animals}")
print(f"'dog' not in animals: {'dog' not in animals}")

# ============================================================================
# 6. SET COMPARISON
# ============================================================================
print("\n\n6. SET COMPARISON")
print("-" * 60)

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4}
set_z = {1, 2, 3}

print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Set Z: {set_z}")

print(f"\nX == Z (equal): {set_x == set_z}")
print(f"X != Y (not equal): {set_x != set_y}")
print(f"X < Y (X is subset of Y): {set_x < set_y}")
print(f"X <= Z (X is subset or equal to Z): {set_x <= set_z}")
print(f"Y > X (Y is superset of X): {set_y > set_x}")
print(f"Y >= X (Y is superset or equal to X): {set_y >= set_x}")

# ============================================================================
# 7. PRACTICAL EXAMPLE 1: REMOVING DUPLICATES FROM A LIST
# ============================================================================
print("\n\n7. PRACTICAL EXAMPLE 1: REMOVING DUPLICATES")
print("-" * 60)

student_ids = [101, 102, 103, 102, 104, 101, 105, 103]
print(f"Student IDs (with duplicates): {student_ids}")

unique_ids = list(set(student_ids))
print(f"Unique student IDs: {unique_ids}")

# ============================================================================
# 8. PRACTICAL EXAMPLE 2: FINDING COMMON INTERESTS
# ============================================================================
print("\n\n8. PRACTICAL EXAMPLE 2: COMMON INTERESTS")
print("-" * 60)

john_interests = {"coding", "gaming", "reading", "music"}
jane_interests = {"reading", "music", "sports", "cooking"}

print(f"John's interests: {john_interests}")
print(f"Jane's interests: {jane_interests}")

common = john_interests.intersection(jane_interests)
print(f"\nCommon interests: {common}")

john_only = john_interests.difference(jane_interests)
print(f"Only John likes: {john_only}")

jane_only = jane_interests.difference(john_interests)
print(f"Only Jane likes: {jane_only}")

# ============================================================================
# 9. PRACTICAL EXAMPLE 3: CHECKING DUPLICATE EMAILS
# ============================================================================
print("\n\n9. PRACTICAL EXAMPLE 3: DUPLICATE EMAIL CHECK")
print("-" * 60)

emails = ["user1@gmail.com", "user2@gmail.com", "user1@gmail.com", "user3@gmail.com", "user2@gmail.com"]
print(f"Email list: {emails}")

if len(emails) == len(set(emails)):
    print("✓ All emails are unique")
else:
    duplicates = set([email for email in emails if emails.count(email) > 1])
    print(f"✗ Duplicate emails found: {duplicates}")

# ============================================================================
# 10. PRACTICAL EXAMPLE 4: WORD FREQUENCY (UNIQUE WORDS)
# ============================================================================
print("\n\n10. PRACTICAL EXAMPLE 4: UNIQUE WORDS IN A SENTENCE")
print("-" * 60)

sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
unique_words = set(words)

print(f"Sentence: {sentence}")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Unique words set: {unique_words}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n\n" + "=" * 60)
print("SUMMARY - KEY POINTS ABOUT SETS")
print("=" * 60)
print("""
1. Sets are unordered collections of unique elements
2. Sets are mutable (elements can be added/removed)
3. Sets cannot contain duplicate elements
4. Sets use curly braces {} for creation
5. Common operations: add(), remove(), union, intersection, difference
6. Useful for: removing duplicates, membership testing, comparing collections
7. Set elements must be immutable (strings, numbers, tuples)
8. Cannot index sets (no set[0], use lists instead)
9. Sets are faster than lists for membership testing
10. Perfect for tracking unique items or finding common elements
""")
print("=" * 60)
