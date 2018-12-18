import os

os.chdir(r"C:\Users\student\mijin\day02\dummy")
#print(os.getcwd())
for filename in os.listdir('.'):
    os.rename(filename,filename.replace('지원자','합격자'))
    
