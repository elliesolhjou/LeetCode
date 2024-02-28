'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


# closing paran starts with closest opening -> last in opening stack

def isValid(s):
    options={
        '(': ')',
        '{':'}',
        '[':']'
    }
    open = ['(', '{', '[']
    stack=[]
    if len(s)%2 !=0:
        return False
    for c in s:
        if c in open:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                if c == options[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
    if len(stack) != 0:
        return False
    else:
        return True


