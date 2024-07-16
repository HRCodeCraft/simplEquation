def convert_to_natural_language(statement, predicate1, predicate2):
    if statement.startswith('∀'):
        quantifier = 'All'
        variable = statement[1]
        predicate = statement[4:]
        return f"{quantifier} {predicate1}({variable}) is {predicate2}({variable})"

    elif statement.startswith('∃'):
        quantifier = 'Some'
        variable = statement[1]
        predicate = statement[4:]
        if '¬' in predicate:
            predicate = predicate.replace('¬', 'not ')
            return f"{quantifier} {predicate1}({variable}) is {predicate2}({variable})"
        else:
            return f"{quantifier} {predicate1}({variable}) is not {predicate2}({variable})"

    else:
        return "Invalid input: statement must start with '∀' or '∃'"

# Example usage:
statements = [
    "∀x P(x)",
    "∀x( S(x) →¬P(x) )",
    "∃x (S(x) ∧ P(x) )",
    "∃x (S(x) ∧¬P(x) )"
]
predicate1 = "S"
predicate2 = "P"

for statement in statements:
    natural_language_statement = convert_to_natural_language(statement, predicate1, predicate2)
    print("Predicate Logic Statement:", statement)
    print("Natural Language Statement:", natural_language_statement)
    print()