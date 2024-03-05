#SLICE OPERATIONS

def main():
    nums=[45, 22, 9, 0, 53, 85, 45, 10, 20, 30]
    print(nums)
    print(f'element at index 5 is {nums[5]}')
    print(f'3 elements from index 5 is {nums[5:8]}')
    print(f'all elements from index 5 is {nums[5:]}')
    print(f'all elements from index 5 except last element is {nums[5:-1]}')
    print(f'all elements till index 5 is {nums[:5]}')
    print(f'elements at even indices is {nums[::2]}')
    print(f'elements at odd indices is {nums[1::2]}')
    print(f'elements in reverse order is {nums[::-1]}')
    print(f'elements in reverse order from index 5 is {nums[5::-1]}')

if __name__=="__main__":
    main()