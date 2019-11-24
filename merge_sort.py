def split(base_list):
    """ Splits the list and returns the left and right sub list"""
    list_mid_pointer=len(base_list)//2
    return base_list[:list_mid_pointer],base_list[list_mid_pointer:]

def merge_sorted_list(left_sublist,right_sublist):
    """ Merges the sorted list provided and returns the sorted list"""
    left_index=right_index=0
    sorted_list=[]
    base_list_length=len(left_sublist)+len(right_sublist)
    while len(sorted_list)<base_list_length:
         if left_sublist[left_index]<right_sublist[right_index]:
             sorted_list.append(left_sublist[left_index])
             left_index+=1
         else:
             sorted_list.append(right_sublist[right_index])
             right_index+=1
        
         if left_index==len(left_sublist):
             sorted_list+=right_sublist[right_index:]
             break
         if right_index==len(right_sublist):
             sorted_list+=left_sublist[left_index:]
             break
    
    return sorted_list

def merge_sort(target_data):
    if len(target_data)==1:
        return target_data
    else:
        left_sub_list,right_sub_list=split(target_data)
        return merge_sorted_list(merge_sort(left_sub_list),merge_sort(right_sub_list))

print(merge_sort([99,88,77,66]))

