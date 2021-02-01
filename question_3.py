d={}  #input dictionary
n = int(input("Enter the number of keys:"))
output=[] #output list
#taking key-value input in dictionary
for i in range(n):
    keys = input('Enter key:')
    values = input('Enter value:')
    values=values.split()
    d[keys] = values
max_length=0
#finding the maximum length of value
for i in d:
    if(len(d[i])>max_length):
        max_length=len(d[i])
#appending the key-value tuples to output list
for i in range(1,max_length+1):
    for j in sorted(d):
        if(len(d[j])==i):
            output.append((j,d[j]))
print(output)
