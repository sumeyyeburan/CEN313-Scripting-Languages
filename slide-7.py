class Employee():
    # class içerisinde sadece name,age ve salary değişkenleri kullanılacak
    # değişkenler private olduğu için _name şeklinde yazılır
    # eğer private olmasaydı name yazılırdı
    __slots__=('_name','_age','_salary')

    # init metodu içinde doğrudan atama yapılmıyor, set metoru çağrılıyor
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    @property #get
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str) or len(value)<3:
            raise TypeError("Excepted string and at least 3 character")
        self._name=value


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if not isinstance(value,int) or value<18 or value>65:
            raise TypeError("Excepted integer and between 18 and 65")
        self._age=value
        
        
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if not isinstance(value,int) or value<10000:
            raise TypeError("Excepted integer and at least 10000")
        self._salary=value   

try:
    e=Employee('sumeyye',21,27000)
    print(e.name,e.age,e.salary)
except TypeError as e:
    print("Type error: ",e)

