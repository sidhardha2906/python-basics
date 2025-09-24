Names = ["reddy","dhanush","farhan","rahul"]
searching_name = input("reddy")#dhanush #farhan
found = False
for i in Names:
    if searching_name == i:
        found = True

if found:
    print("yes")
else:
    print("no")

#count even and odd numbers
numbers = [7,10,12,13,23,45,227,17,455]
# o = 7
# e = 2
evn_cnt = 0 #2
odd_cnt = 0 #1
for i in range(len(numbers)):
    if numbers[i]%2 ==0:
        evn_cnt += 1
    else:
        odd_cnt += 1
print("numbers of even numbers are: ",evn_cnt)
print("number of odd numbers are: ",odd_cnt)

#remove all negitives and positives
numbers = [-1,21,-7,12,-45,-30,-19,5,10,2,-14,-20,0]
negative_list = []
for i in range(len(numbers)):
    if numbers[i] < 0:
        negative_list.append(numbers[i])

print(negative_list)

#multiply each element in the list
numbers = [56,90,6,74,9,42,18,70]
m = int(input("2: "))
after_multiplication = []
for i in numbers:
    after_multiplication.append(i+m)
    print(after_multiplication)


    