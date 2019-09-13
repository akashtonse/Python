def remove_duplicates(numbers):
    list=[]
    for number in numbers:
        if number not in list:
            list.append(number)

    print(list);
    return list
remove_duplicates([1,2,3,4,5,5,5,6,3,2])

#list comprehension
s=[x**2 for x in range(10)]
m=[x for x in s if x%2==0]
print(m)
m.reverse()
print(m)


