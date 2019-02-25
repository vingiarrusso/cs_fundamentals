import pudb
pu.db

def calculate(s):
    def doOperation(operation, num):
        if operation == "+":
            nums.append(num)
        if operation == "-":
            nums.append(-num)
        if operation == "*":
            nums.append(nums.pop() * num)
        if operation == "/":
            numerator = nums.pop()
            # because python...
            nums.append((numerator // num) if numerator >= 0 else -(-numerator//num))

    sign = "+"
    num = 0
    nums = []

    for char in s:
        if char == ' ':
            continue
        if char.isnumeric():
            num = (num * 10) + int(char)
        else:
            doOperation(sign, num)
            sign = char
            num = 0
    
    doOperation(sign, num)

    return sum(nums)
calculate("14-3/2")
