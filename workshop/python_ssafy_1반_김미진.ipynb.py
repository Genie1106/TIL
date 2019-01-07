# No.1
n,m = map(int,input().split())
star = "*"*n
enter = "\n"
print((star+enter)*m)

# No.2
student = {'python': 80, 'algorithm':99, 'django':89, "flask":83 }
score = sum(student.values())
num=len(student)
avg = score/num
print(avg)

# No.3

blood_types=['A','B','A','O','AB','O','A','B','O',"B",'AB']

A=0
B=0
AB=0
O=0

for i in range(len(blood_types)):
    if blood_types[i]=='A':
        A=A+1
    elif blood_types[i]=='B':
        B=B+1
    elif blood_types[i]=='O':
        O=O+1
    else:
        AB=AB+1

print(f"A형은 {A}명")
print(f"B형은 {B}명")
print(f"O형은 {O}명")
print(f"AB형은 {AB}명")
