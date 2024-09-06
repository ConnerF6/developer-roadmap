number_list = []

def prompt():
    mathtype = input("""What type of math would you like to solve?
                     Please use symbols (ex +, -, x, /, ^) """).strip()
    
    if mathtype not in ["+", "-", "x", "/", "^"]:
        print("Please enter a valid math type")
        return prompt()
    
    number_of_numbers = input("How many numbers are there in your equation? ").strip()
    
    try:
        number_of_numbers = int(number_of_numbers)
    except ValueError:
        print("Please enter a valid number for the count of numbers.")
        return prompt() 
    
    number_list.clear()
    
    for i in range(number_of_numbers):
        num = input(f"What is number {i + 1}? ").strip()
        try:
            num = float(num)
        except ValueError:
            print("Please enter a valid number.")
            return prompt()
        number_list.append(num)
    
    Answer = 0
    if mathtype == "+":
        Answer = sum(number_list)
    elif mathtype == "-":
        Answer = number_list[0]
        for num in number_list[1:]:
            Answer -= num
    elif mathtype == "x":
        Answer = 1
        for num in number_list:
            Answer *= num
    elif mathtype == "/":
        Answer = number_list[0]
        for num in number_list[1:]:
            if num == 0:
                print("Division by zero is not allowed.")
                return
            Answer /= num
    elif mathtype == "^":
        Answer = number_list[0]
        for num in number_list[1:]:
            Answer **= num

    print(f"Your answer is: {Answer}")
    prompt()
prompt()