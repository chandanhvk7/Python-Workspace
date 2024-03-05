import json
class Book:
    def __init__(self,**kwargs) -> None:
        self.title=kwargs.get('title')
        self.author=kwargs.get('author')
        self.price=kwargs.get('price',0.0)
    def __str__(self):
        title=None if self.title is None else f'"{self.title}"'
        author=None if self.author is None else f'"{self.author}"'
        return f'Book(title={title},author={author},price={self.price})'
    def to_dict(self):
        return self.__dict__
    class BookEncoder(json.JSONEncoder):
        def default(self,obj):
            return obj.__dict__ if isinstance(obj,Book) else json.JSONEncoder.default(obj)

def main():
    b1=Book()
    b2=Book(title='Six of Crows',author='Leigh Bardugo',price=499.0)
    print(b1)
    print(b2)
    b3=eval(b2.__str__()) #deep copy
    print(f'b3 is of type {type(b3)} and b3 is {b3}')
    print(json.dumps(b2.to_dict()))
    books=[Book(title='Shadow and Bone',author='Leigh Bardugo',price=399.0),
           Book(title='Crooked Kingdom',author='Leigh Bardugo',price=499.0),
           b2]
    print(json.dumps([b.to_dict() for b in books],indent=3))


if __name__=="__main__":
    main()