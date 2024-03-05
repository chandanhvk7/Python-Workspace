import sys

def divide(numerator,denominator,/):#position only args
    return numerator//denominator,numerator%denominator
def main():
    try:
        arg1=sys.argv[1] #possible index error
        arg2=sys.argv[2] #possible index error
        num=int(arg1) #possible Value error
        den=int(arg2) #possible Value error
        quot,rem=divide(num,den) #possible zero division error
        print(f'{num} / {den} is {quot}')
        print(f'{num} % {den} is {rem}')
    except IndexError:
        print('not enough inpts')
    except ValueError:
        print('Wrong Datatype of values')
    except ZeroDivisionError:
        print('Cannot Divide by zero')
 
if __name__=="__main__":
    print('Before main')
    main()
    print('After main')

