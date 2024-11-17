names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
        
max = names[0].len()
for i in names:
    if names[i].len() > max: max = names[i].len()
return max

for x in names:
    sum += names[x].len()
return sum

