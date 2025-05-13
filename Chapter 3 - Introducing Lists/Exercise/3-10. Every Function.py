# Create a list of languages
languages = ["Python", "Spanish", "Japanese", "German", "French"]

# Print original list
print("Original list:")
print(languages)

# Access elements
print("\nAccessing elements:")
print(f"My favorite language is {languages[0]}.")
print(f"I'd like to learn {languages[2]} someday.")

# Modify an element
languages[1] = "Mandarin"
print("\nModified list:")
print(languages)

# Add elements
languages.append("Italian")  # Add to end
languages.insert(2, "Korean")  # Insert at position 2
print("\nAfter adding elements:")
print(languages)

# Remove elements
del languages[3]  # Delete by index
print("\nAfter deleting an element by index:")
print(languages)

removed_language = languages.pop()  # Remove last item
print(f"\nI just removed {removed_language} using pop().")
print("Current list:", languages)

unwanted_language = "Mandarin"
languages.remove(unwanted_language)  # Remove by value
print(f"\nRemoved {unwanted_language} using remove().")
print("Current list:", languages)

# Sort the list temporarily
print("\nTemporarily sorted list:")
print(sorted(languages))

# Show original list again
print("Original list after sorted():")
print(languages)

# Sort the list permanently
languages.sort()
print("\nPermanently sorted list:")
print(languages)

# Sort in reverse alphabetical order
languages.sort(reverse=True)
print("\nReverse sorted list:")
print(languages)

# Reverse the order of the list
languages.reverse()
print("\nReversed order of list:")
print(languages)

# Find the length of the list
print(f"\nThe list contains {len(languages)} languages.")
