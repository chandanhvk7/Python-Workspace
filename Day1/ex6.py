import sys
from chanutils import to_float

def main():
    total=0
    for each_arg in sys.argv[1:]:
        total+=to_float(each_arg)
    print(f'Total={total},and average={total/(len(sys.argv)-1)}')

if __name__=="__main__":
    main()