import os.path
check_file = os.path.exists(input())
if check_file != True:
    print("Not found")
else:
    with open("example.txt", encoding="utf8") as file:
        data = [line.strip() for line in file]
        print(max(data))
