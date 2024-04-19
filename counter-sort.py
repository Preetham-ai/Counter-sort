# Only Whole Numbers are allowed in the list
# O(n^2) time complexity

def counter_sort(lst:list) -> list:
    counter=0
    sorted_list=[]
    while len(sorted_list)<len(lst):
        counter+=1
        if counter in lst:
            sorted_list.append(counter)
    return sorted_list

if __name__ == "__main__":
    counter_sort()