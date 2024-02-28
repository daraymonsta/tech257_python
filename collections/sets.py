# Create a frozen set
frozen_set = frozenset(["hello", "world"])

# Trying to add an element to a frozen set would raise an "AttributeError: 'frozenset' object has no attribute 'add'"
# Doesn't work: frozen_set.add("!")

# Create a normal set
normal_set = {"let's", "learn"}
# Add a frozen set to a normal set
# observe
normal_set.add(frozen_set)
# Print the set
print(normal_set)

# Main difference between frozen sets and normal sets
# * Frozen set is immutable (can't be modified)

list_of_things = ["ball", "hat", 5]
normal_set.add(list_of_things)