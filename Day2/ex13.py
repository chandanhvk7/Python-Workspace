def subtotal(code, *nums):
    match code:
        case 1:
            return sum(nums)
        case 2:
            return len(nums)
        case 3:
            return sum(nums)/len(nums)
        case _:
            return None

def main():
    s=subtotal(1,1,2,3,4,5)
    print(s)
    s=subtotal(2,1,2,3,4,5)
    print(s)
    s=subtotal(3,1,2,3,4,5)
    print(s)

if __name__=="__main__":
    main()