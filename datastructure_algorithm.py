import math
from algorithm_search_sort import quick_sort

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)

#print(factorial(3))

def english_ruler():
    def draw_line(tick_length,tick_label=""):
        """ Draw a line of a given tick length with a given label"""
        line="-"*tick_length
        if tick_label:
            line+="  " +tick_label
        print(line)
    
    def draw_interval(center_length):
        """ Draw tick interval based on the center_length"""
        if center_length >0:
            draw_interval(center_length -1)
            draw_line(center_length)
            draw_interval(center_length -1)

    def draw_ruler(num_inches,major_length):
        """ Draw english ruler with a given number of inches and given length"""
        draw_line(major_length,'0')
        for j in range(1,1+num_inches):
            draw_interval(major_length-1)
            draw_line(major_length,str(j))
        
    draw_ruler(4,5)

def binary_search():
    list_data=[]
    size=int(input("What should be the size of the tuple?"))
    for i in range(0,size):
        list_data.append(int(input("Enter data: ")))
    print(list_data)
    sorted_data=quick_sort(list_data)
    print("Sorted data {0}".format(sorted_data))

    def bn_search(data,target,start,end):
        print("Searching data from {0} to {1}".format(start,end))
        if end>=start:
            mid= start + end //2
            print(mid)
            if data[mid]==target:
                return mid
            elif data[mid] >target:
                return bn_search(data,target,start,mid -1)
            elif data[mid]< target:
                return bn_search(data,target,mid + 1,end)
        else:
            print("Element is not present")
            return -1
    search_el=int(input("Provide search data: "))
    index_for_data=bn_search(sorted_data,search_el,0,len(sorted_data)-1)
    if index_for_data!=-1:
        print("Element is present at: %d" % index_for_data)
    else:
        print("Element is not present in the array")



binary_search()

#english_ruler()


        
    



    
