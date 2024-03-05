def print_table(num):
    for i in range(1,11):
        print(f'{num} X {i}={num*i}')

if __name__=='__main__':#This is done to prevent this part from executing when it is being imported from somewhere else
    num=input('Enter the number:') #Here the num is returned as a string
    num=int(num)
    print_table(num)
    print('End of exec!')