#Only Whole Numbers are allowed in the list

def counter_sort(lst:list) -> list:
    counter=0
    sorted_list=[]
    while True:
        counter+=1
        if counter in lst:
            sorted_list.append(counter)
        if len(sorted_list)==len(lst):
            return sorted_list