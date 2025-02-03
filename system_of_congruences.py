import math
import random

def euc(a, b):
    # This function calculates the GCD using recursion method.
    # Find the modulus of a and b.
    r = a % b
    
    # If remainder does not equal 0, call the euc() function again. If remainder equals 0, return b which is the GCD.
    if r != 0:
        result = euc(b, r)
    else:
        result = b

    return result

def crt_solve(congruences):
    # Initialize variables. Collect all modulus values.
    m_val = [congruences[i][1] for i in range(len(congruences))]
    pair_set = []
    gcd_val = set()

    # Collect all modulus pairs and run Euclidean algorithm to check whether they are all relatively prime.
    for i in range(len(m_val)):
        for j in range(len(m_val)):
            if j != i:
                pair = sorted([m_val[i], m_val[j]])
                if pair not in pair_set:
                    pair_set.append(pair)
                else:
                    pass
            else:
                continue

    for pair in pair_set:
        gcd = euc(pair[0], pair[1])
        gcd_val.add(gcd)

    # Check that there is only one value of 1 in gcd_val. Flag it as True, if so. If not, flag it as False.
    if len(gcd_val) == 1 and 1 in gcd_val:
        r_prime = True
    else:
        r_prime = False

    # If gcd value calculated above is 1, this means that the modulus values are relatively prime. If not, return None.
    if r_prime == True:
        # Formula: x ≡ ri mod mi
        # Collect all the ri values.
        rmy_set = []
        ri = [congruences[i][0] for i in range(len(congruences))]

        # Run a loop to calculate Mi, yi(modular inverse of Mi), and the product of ri, Mi, and yi.
        # Get the sum of all riMiyi mod M.
        for i in range(len(ri)):
            Mi = math.prod(m_val) // m_val[i]
            yi = pow(Mi, -1, m_val[i])
            rmy = ri[i] * Mi * yi
            rmy_set.append(rmy)

        result = (sum(rmy_set) % math.prod(m_val), math.prod(m_val))
        
    else:
        result = None

    return result

def convert_input(usr_input):
    # This function converts user input into a list of tuples.
    # Initializing variables.
    usr_list = []
    num_list = []
    valid = True
    
    # Manipulating usr_input string to convert it into a valid list of tuples of (x,y) format.
    usr_input = usr_input.replace(' ', '')
    usr_input = usr_input.split(',')

    for index, i in enumerate(usr_input):
        try:
            if '(' in i:
                i = i.strip('(')
                usr_input[index] = int(i)
            elif ')' in i:
                i = i.strip(')')
                usr_input[index] = int(i)
            else:
                raise ValueError
        except ValueError:
            valid = False
            break
    
    for i in usr_input:
        num_list.append(i)
        
        if len(num_list) >= 2:
            num_tuple = tuple(num_list)
            usr_list.append(num_tuple)
            num_list = []
        else:
            continue
    
    return usr_list, valid

def main():
    # This is the main function.
    # Inputfield to entering system of congruence equations.
    user_input = input("Enter tuples of integer pair separated by commas (e.g. (x,y), (w,q), (p, h), where (x,y) represents x mod y): ")

    # Calling convert_input() function to turn the user input into a list of tuples.
    user_input, check = convert_input(user_input)

    # If input is valid, solve the system of congruences. If not, output error message.
    if check == True:
        final = crt_solve(user_input)
        print("The value X that satisfies the system of congruences is:", final)
    else:
        print("\nInvalid input. Please restart program and try again.")
        print("Input must be a list of integer tuples representing modular equations (e.g. (2,3), (5, 7), ... , (x,y) where (x, y) represents x mod y).\n")

if __name__ == "__main__":
    main()
