from itertools import product

input_file = 'top_10_passwords.txt'
output_file = 'bc_final_pwlist.txt'
try:
    with open(input_file,'r') as f:
        words = [line.strip() for line in f.readlines()]

    words += [word.upper() for word in words]

    with open(output_file,'w') as f:
        for combo in product(words,repeat=2):
            f.write(''.join(combo) + '\n')
except Exception as e:
    print("Something went wrong")
    print(f"Here is what went wrong: ({e})")