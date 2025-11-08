# 25
a = input("키 입력: ").split()
b = list(map(int,input("값 입력: ").split()))
c = dict(zip(a,b))
c.pop('alpha')
c.pop('delta')
print(c)

# 26
park = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
print(park['english'],park['science'])

# 27
kim = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
a = dict.fromkeys(kim,100)
print(a)

# 28
lee = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
lee.pop('english')
print(lee)

# 29
lim = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
for i, j in lim.items():
    print(i,j)

# 30
choi = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
a = {key: value for key,value in choi.items() if value >= 90}
print(a.keys())

# 31
yoo = {'korean': 94, 'english' : 91, 'mathematics':89,'science':83}
a=sum(yoo.values())
print(a/len(yoo))
