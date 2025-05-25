glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'A collection which is ordered and changeable.',
    'function': 'A block of code that only runs when it is called.',
}

glossary['tuple'] = 'An immutable ordered list of items.'
glossary['string'] = 'A sequence of characters enclosed in quotes.'
glossary['boolean'] = 'A data type with only two values: True or False.'
glossary['comment'] = 'Text in code that is not executed, used for documentation.'
glossary['indentation'] = 'Whitespace used to define blocks of code in Python.'

for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}")
