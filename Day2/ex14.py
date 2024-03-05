def print_info(**kwargs):
    print(f'kwargs is of type {type(kwargs)}')

    for each_key in kwargs:
        print(f'{each_key}-->{kwargs[each_key]}')

def main():
    b1=dict(title='Six of crows',price =799.0)
    print_info(fname='Chandan',lname='Kshatriya',fav_num=7)
    print_info(**b1) #spreads b1 and then feeds it to the func

if __name__=="__main__":
    main()