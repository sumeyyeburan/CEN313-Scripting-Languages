class A: pass
class B: pass
class C(B,A): pass
class D(B): pass
class E(C,D): pass

# print(C.__mro__)
print(E.__mro__)

# class A: pass
# class B: pass
# class C(A,B): pass
# class D: pass
# class E(C,D): pass

# print(C.__mro__)
# print(E.__mro__)

# class A: pass
# class B: pass
# class C(A,B): pass
# class D(B): pass
# class E(C,D): pass

# print(C.__mro__)
# print(E.__mro__)
