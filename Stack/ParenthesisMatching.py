# write the above code of Stack first, then do the following:
def parenthesis_matching(S):
    if S == "":
        return 1
        
    stack = Stack()
    for char in S:
        if char == '{' or char == '[' or char == '(':
            stack.push(char)

        elif char == '}' or char == ']' or char == ')':
            if stack.isEmpty():
                return 0
            elif (char == '}' and stack.peek() == '{') or (char == ')' and stack.peek() == '(') or (char == ']' and stack.peek() == '['):
                _ = stack.pop()
            else:
                return 0
    
    if stack.isEmpty():
        return 1
    else:
        return 0
