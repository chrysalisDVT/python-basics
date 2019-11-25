import math


def split_list(data):
    mid=len(data)//2
    print(data[:mid])
    print(data[mid:])
    return data[:mid],data[mid:]

def merge_sorted_list(left_sub_list,right_sub_list):
    """ Merge sort implementation """
    print(left_sub_list)
    print(right_sub_list)
    if len(left_sub_list)==0:
        return right_sub_list
    elif len(right_sub_list) ==0:
        return left_sub_list
    #General case where we are required to merge the provided list
    index_left=index_right=0
    list_merged=[]
    len_target_list=len(left_sub_list)+len(right_sub_list)

    while len(list_merged) < len_target_list:
        if left_sub_list[index_left]<=right_sub_list[index_right]:
            list_merged.append(left_sub_list)
            index_left+=1
        else:
            list_merged.append(right_sub_list)
            index_right+=1
        
        if index_right == len(right_sub_list):
            list_merged+=right_sub_list[index_right:]
            break
        elif index_left == len(left_sub_list):
            list_merged+=left_sub_list[index_left:]
            break
    return list_merged

def merge_sort(data):
    if len(data)<=1:
        return data
    else:
        left_sub_list,right_sub_list= split_list(data)
        return merge_sorted_list(merge_sort(left_sub_list),merge_sort(right_sub_list))

def bubble_sort():
    """ Bubble sort implementation """

def insertion_sort(data):
    """ Insertion sort implementaion 
    
    Sample Input: [100,99,101,23]
    
    I1->
        Key=99
        temp=data[compare_index]
        data[compare_index]=key
        data[compare_index+1]=temp
        compare_index=compare_index-1
        data[compare_in]
        [99,100,101,23]
    I2->
        Key=101
        [99,100,101,23]
    I3->
        Key=23
        compare=101 key=23
        99,100,23,101
        compare=100
        99,23,100,101
        compare=99
        23,99,100,101
    """
    for start in range (1,len(data)):
        compare_index=start -1
        key=data[start]
        while compare_index>=0 and key<data[compare_index]:
            #temp=data[compare_index]
            data[compare_index+1],data[compare_index]=data[compare_index],key
            #data[compare_index]=key
            compare_index=compare_index-1
        #data[compare_index+1]=key
    return data

print(insertion_sort([100,88,77,66]))

def quick_sort(data):
    """ Sorting the passed data based on the quick sort algorithm"""
    def partition(data,start,end):
        """ Creating the partition and returning the partition key to sort further"""
        i=start-1
        for j in range(start,end):
            if data[j]<=data[end]:
                i+=1
                data[i],data[j]=data[j],data[i]
        data[i+1],data[end]=data[end],data[i+1]
        return i+1
        
    def sort(data,start,end):
        """
        Sorting the data provided 
        """
        if start < end:
            partition_index=partition(data,start,end)
            sort(data,start,partition_index-1)
            sort(data,partition_index+1,end)
    sort(data,0,len(data)-1)
    #print(data)
    return data
data=[99,88,77,66]
quick_sort(data)
print(data)

print(quick_sort.__doc__)

def intro_sort(data):
    """ Introspection sort based on the data size and recurssion depth"""
    recurssion_depth=2*math.log(len(data))
    if len(data) < 15:
        insertion_sort(data)
    elif recurssion_depth==0:
        merge_sort(data)
    else:
        quick_sort(data)



