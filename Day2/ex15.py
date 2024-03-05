import math
from pprint import pprint

def main():
    nums=[19,29,1,3,3,2,3,2,233,2,12]
    unique_nums=sorted(list(set(nums)))

#Filter operations
    even_nums=[each_num for each_num in nums if each_num%2==0]
    odd_nums=[each_num for each_num in nums if each_num%2]

    #map Operations
    squares=[each_num**2 for each_num in nums]

    #transform a list to a dict
    square_roots={each_num:math.sqrt(each_num) for each_num in unique_nums}

    print(nums)
    print(even_nums)
    print(odd_nums)
    print(squares)
    pprint(square_roots)

if __name__=="__main__":
    main()