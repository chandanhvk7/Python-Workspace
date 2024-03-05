def base_name(path:str)->str:
    start=path.rindex('\\')+1
    end=path.rindex('.')
    return path[start:end]

def folder_path(path:str):
    return path[:path.rindex('\\')]

def main():
    some_path='C:\Python Workspace\Day1\ex10.py'
    filename=base_name(some_path)
    print(f'filename is "{filename}"')
    print(f'and it is located at "{folder_path(some_path)}"')

if __name__=="__main__":
    main()