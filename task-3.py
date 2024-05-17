def check_symmetry(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return "Несиметрично"
            elif stack[-1] == mapping[char]:
                stack.pop()
            else:
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

# Приклади вхідних рядків
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expression in expressions:
    result = check_symmetry(expression)
    print(f"{expression}: {result}")
