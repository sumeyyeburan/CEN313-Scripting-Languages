
def data_dict():
    data=[]

    with open("portfolio.csv",'r') as f:
        next(f) #ilk satırı okur ama atama yapmaz,genelde ilk satırlar başlık olduğu için
        for line in f:
            temp=line.strip().split(',')
            d={
                "name":temp[0],
                "shares":temp[1],
                "price":temp[2]
            }  
            data.append(d)   

    return data

def data_tuple():
    data=[]  # veri saklamak için boş liste oluşturulur

    with open("portfolio.csv",'r') as f:
        next(f)
        for line in f:
            temp=line.strip().split(',')
            t=(temp[0],int(temp[1]),float(temp[2]))
            data.append(t)

    return data        

print("\nDictionary")
data_list=data_dict()
for data in data_list:
    print(data)

print("\nTuple")
data_list2=data_tuple()
for data in data_list2:
    print(data)    