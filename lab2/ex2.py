with open('a.txt', 'r', encoding="utf-8") as infile:
    list = infile.read().split('\n')

# print(list)
with open('b2.txt', 'w', encoding="utf-8") as oddfile:
    with open('b1.txt', 'w', encoding="utf-8") as evenfile:
        for x in range(0, len(list)):
            if x % 2 == 0:
                oddfile.write("%s\n" % list[x].upper())
            else:
                evenfile.write("%s\n" % list[x].lower())
