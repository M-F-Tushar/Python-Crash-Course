# List of places I'd like to visit (not in alphabetical order)
places_to_visit = ["Japan", "Iceland", "New Zealand", "Italy", "Norway"]

# Print original list
print("Original list:")
print(places_to_visit)

# Print list in alphabetical order using sorted() (without modifying original list)
print("\nAlphabetical order (temporary):")
print(sorted(places_to_visit))

# Show original list again
print("\nOriginal list after sorted():")
print(places_to_visit)

# Print list in reverse alphabetical order using sorted()
print("\nReverse alphabetical order (temporary):")
print(sorted(places_to_visit, reverse=True))

# Show original list again
print("\nOriginal list after reverse sorted():")
print(places_to_visit)

# Use reverse() to change the list order
places_to_visit.reverse()
print("\nList after reverse():")
print(places_to_visit)

# Use reverse() again to restore original order
places_to_visit.reverse()
print("\nList after second reverse() (back to original):")
print(places_to_visit)

# Use sort() to permanently sort the list alphabetically
places_to_visit.sort()
print("\nList after sort() (alphabetical):")
print(places_to_visit)

# Use sort() again to sort in reverse alphabetical order
places_to_visit.sort(reverse=True)
print("\nList after sort(reverse=True) (reverse alphabetical):")
print(places_to_visit)
