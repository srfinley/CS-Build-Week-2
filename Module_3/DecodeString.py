class Solution:
    def __init__(self):
        self.nums = ['1','2','3','4','5','6','7','8','9','0']

    def split_leading_val(self, s):
        """Identifies number, string pairs after splitting"""
        number = []
        trailing = ''
        for index, char in enumerate(s):
            if char in self.nums:
                number.append(char)
            else:
                trailing = s[index:]
                break
        if len(number) == 0:
            value = 1
        else:
            value = int(''.join(number))
        return [value, trailing]
        
    def splitsies(self, s):
        """Splits a multipart expression into top-level parts"""
        depth = 0
        splits = []
        last_index = 0
        for index, char in enumerate(s):
            if char == '[':
                depth += 1
            if char == ']':
                depth -= 1
                if depth == 0:
                    splits.append(s[last_index:index+1])
                    last_index = index + 1
            elif char not in self.nums and depth == 0:
                splits.append(s[last_index:index+1])
                last_index = index + 1
        if last_index < len(s):
            splits.append(s[last_index:])
        return splits
        
    def decodeString(self, s: str, n=1) -> str:
        """recursively splits and evaluates a coded string"""
        if s.count("[") == 0:
            return n * s
        if s[1:-1].count("[") == 0:
            return n * s[1:-1]
        total = ''
        for statement in self.splitsies(s):
            expression = self.split_leading_val(statement)
            if expression[1][0] == '[' and expression[1][-1] == ']':
                expression[1] = expression[1][1:-1]
            total += self.decodeString(expression[1], expression[0])
        total *= n
        return total
        