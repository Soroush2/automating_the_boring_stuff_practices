def printTable(tableData):
    # Determine the number of columns
    num_columns = len(tableData)

    # Find the maximum width for each column
    colWidths = [max(len(item) for item in col) for col in tableData]
    

    # Determine the number of rows (all inner lists have the same length)
    num_rows = len(tableData[0])

    # Print the table row by row
    for row in range(num_rows):
        for col in range(num_columns):
            print(tableData[col][row].rjust(colWidths[col]), end=" ")
        print()  # Move to the next line


# Example usage
tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]
# Example usage 1
tableData1 = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]
print("Example 1:")
printTable(tableData1)
print()

# Example usage 2
tableData2 = [
    ["red", "blue", "green", "yellow"],
    ["circle", "square", "triangle", "hexagon"],
    ["one", "two", "three", "four"],
]
print("Example 2:")
printTable(tableData2)
print()

# Example usage 3
tableData3 = [
    ["python", "java", "c++", "ruby"],
    ["beginner", "intermediate", "advanced", "expert"],
    ["easy", "moderate", "hard", "very hard"],
]
print("Example 3:")
printTable(tableData3)
print()
printTable(tableData)
