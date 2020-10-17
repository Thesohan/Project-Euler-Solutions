"""
Problem 79: https://projecteuler.net/problem=79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt (https://projecteuler.net/project/resources/p079_keylog.txt), contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""


def place_fragment(code, frags):
    if len(frags) == 0:                             #If there are no fragments, the code is done
        return code

    head = { f[0] for f in frags }                  #All first digits
    tail = { t for f in frags for t in f[1:] }      #All tailing digits have some digit before it

    next_frag = (head - tail).pop()                 #Next digit fragment is digit which is not a tailing digit
    next_code = code + next_frag                    #Append next digit fragment to existing code

    next_frags = [f.replace(next_frag, '') for f in frags if f != next_frag]    #Remove found digit from fragments, filter empty fragments
    
    return place_fragment(next_code, next_frags)    #Place next digit fragment based on new fragments


def solution(file_path):
    """
    This solution assumes passcodes do not have duplicate numbers 
    as we want the shortest possible solution.

    The solution strategy is in short the following:
    1. All successful entries are called fragments.
    2. Create a set of first digits from all fragments.
    3. If any first digit in this set appear anywhere other than 
       the first position in any fragment, said digit has digits before it.
    4. Remove all digits that have digits before it from the set.
    5. Choose some remaining digit in the set (we only need to find the shortest passcode).
    6. Remove the chosen digit from all fragments. 
    7. If a fragment is empty, remove it.
    8. If there are more fragments, go to step 2.
    9. There are no more fragments, the code is the chosen digits in the order chosen.
    """

    with open(file_path, 'r') as file:
        fragments = file.readlines()

    return place_fragment("", [p.strip() for p in fragments])   #Initialize with empty code and trim whitespace from fragments



if __name__ == "__main__":
    print(solution("problem_79/keylog.txt"))
