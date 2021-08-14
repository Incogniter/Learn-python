# challenge to find the number of words in a word
# count of a word
text = input("enter the text :")

# total_count = []
# for x in text.split():
#     total_count.append(len(x))
# print(total_count)

answer = [len(x) for x in text.split()]
print(answer)

total_count = []
for x in text.split():
    total_count.append((x, len(x)))
print(total_count)

# dictionary {} it wont be order as it is an unordered
answer = {(x, len(x)) for x in text.split()}
print(answer)
