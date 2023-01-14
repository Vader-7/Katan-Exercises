"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    if len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        return [s[i:i+2] for i in range(0, len(s)-1, 2)] + [s[-1] + '_']



tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)
