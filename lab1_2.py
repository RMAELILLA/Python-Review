def remove_dup(input_str):
    result_str = ""
    for char in input_str:
        if input_str.count(char) == 1:
            result_str += char
    return result_str

num_str = int(input("Enter the number of strings: ")) # Input: Number of strings

for _ in range(num_str):
    input_str = input("Enter a string: ")
    result_str = remove_dup(input_str)
    print(result_str)