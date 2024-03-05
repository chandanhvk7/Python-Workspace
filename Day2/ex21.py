class Employee:
    def __init__(self,**kwargs) -> None:
        self.id=kwargs.get('id',0)
        self.name=kwargs.get('name')
        self.salary=kwargs.get('salary',45000)

    #getter property (accessor or readable property)
    @property
    def id(self):
        return self.__id
    
    #setter for the above getter;mutator property
    @id.setter
    def id(self,value):
        if value is not None and type(value) is not int:
            raise TypeError('id must be int')
        if value is not None and value<=0:
            raise ValueError('id must be >0')
        
        self.__id=value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if value is not None and type(value) is not str:
            raise TypeError('name must be str')
        if value is not None and len(value)>30:
            raise ValueError('name must be less than 30 characters')
        
        self.__name=value

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        if value is not None and type(value) is not int:
            raise TypeError('salary must be int')
        if value is not None and value<45000:
            raise ValueError('salary must be greater than 45k')
        if value is not None and value>1000000:
            raise ValueError('salary must be less than 10 lakhs')
        
        self.__salary=value
    
def main():
    e1=Employee(id=2,name='Chandan',salary=1000000)
    print(e1)

if __name__=="__main__":
    main()
