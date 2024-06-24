
with open('C:\Máy tính\GitHub\AIO-Exercise\module1_week2\P1_data.txt', 'r') as f:
    document = f.read()

document = document.lower()
words = document.split()

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)
