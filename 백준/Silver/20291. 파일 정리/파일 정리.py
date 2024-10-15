n = int(input())
file_dict = {}

for _ in range(n):
    file_name = input()
    
    # Check if the file has an extension by checking if there's a dot in the name
    if '.' in file_name:
        _, extension = file_name.rsplit(".", 1)
        
        # Count the occurrences of each extension
        if extension in file_dict:
            file_dict[extension] += 1
        else:
            file_dict[extension] = 1

# Sort extensions alphabetically and print the counts
for extension in sorted(file_dict):
    print(extension, file_dict[extension])