# Only Whole Numbers are allowed in the list
# O(n) time complexity

def counter_sort(lst:list) -> list:
    counter=0
    sorted_list=[]
    while len(sorted_list)<=len(lst):
        counter+=1
        if counter in lst:
            sorted_list.append(counter)
        else:
            break
    return sorted_list

print(counter_sort([1,4,2,3,5,6,8,7,9,10]))    