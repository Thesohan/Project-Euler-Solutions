"""
Problem 22: https://projecteuler.net/problem=22
Using names.txt (https://projecteuler.net/project/resources/p022_names.txt) (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def solution(file_path):
    with open(file_path, 'r') as file:
        names = file.readline()

    names = names.replace('"', '').split(',')
    names.sort()

    total_score = 0
    for i, name in enumerate(names, start=1):
        score = 0
        for char in name:
            score += ord(char) - 65 + 1 #Make the character 'A' equal 1

        total_score += score * i
    
    return total_score


if __name__ == "__main__":
	print(solution("problem_22/names.txt"))
