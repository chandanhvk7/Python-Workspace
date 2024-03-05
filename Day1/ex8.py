#list
import copy

def main():
    nums=[17,45,22,56,9,0,53,85,45]
    print(f'count of 22 in nums is {nums.count(22)}')
    print(f'count of 10 in nums is {nums.count(10)}')
    print(f'count of 45 in nums is {nums.count(45)}')
    evens=[10,20,30]
    nums.extend(evens)
    #nums+=evens #which is same as extend
    print(nums)
    #nums*=2 #content of the list gets duplicated i.e. [1,2] becomes [1,2,1,2]
    nums+=['chvk']
    print(nums)
    print(nums.pop(),nums)
    print(nums.pop(0),nums) #for invalid index, raises an IndexError
    print(nums.remove(56),nums) #for value not found raises a ValueError


def main2():
    nums=[17,45,22,56,9,0,53,85,42]
    print(f'address of nums is {id(nums)}')
    print(f'nums contains {len(nums)} elements')
    nums.append(75)
    print(nums)
    nums.insert(0,1000)
    print(nums)
    nums.insert(-1,290)
    print(nums)
    nums.insert(100,1298)
    print(f'Index of 1298 is {nums.index(1298)}')
    nums.insert(-1000,3000)
    print(nums)
    print(f'Index of 3000 is {nums.index(3000)}')
    nums.clear()
    print(nums)
    print(f'address of nums is {id(nums)}')

def main3():
    nums1=[17,45,[22,90]]
    nums2=nums1.copy()
    nums3=copy.deepcopy(nums1)
    print(f'address of nums1 is {id(nums1)}')
    print(f'address of nums2 is {id(nums2)}')
    print(f'address of nums3 is {id(nums3)}')
    print(nums1)
    print(nums2)
    print(nums3)
    print()
    nums1[0]=50
    print(nums1)
    print(nums2)
    print(nums3)
    nums1[2][0]=99
    print()
    print(nums1)
    print(nums2)
    print(nums3)
    nums1[2].append(88)
    print()
    print(nums1)
    print(nums2)
    print(nums3)
    print(f'address of nums1 is {id(nums1)}')
    print(f'address of nums2 is {id(nums2)}')
    print(f'address of nums3 is {id(nums3)}')


if __name__=="__main__":
    main()