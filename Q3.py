#You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n. 
# For each index i, names[i] and heights[i] denote the name and height of the ith person. Return names sorted in descending order by the people's heights.

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    sorted_names = [name for height, name in sorted(zip(heights, names), reverse=True)] #creates a list of tuples where each tuple contains a name and a height.
    return sorted_names

names = ["Bob", "Bob", "Charlie"]
heights = [165, 170, 175]
print(sortPeople(names, heights)) # Output ['Charlie','Bob','Bob]


names = ["Bob", "Alice", "Charlie"]
heights = [165, 179, 175]
print(sortPeople(names, heights)) # Output ['Alice','Charlie','Bob']
