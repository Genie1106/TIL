import os

os.chdir(r"C:\Users\student\mijin\day02\dummy")
#print(os.getcwd())
for filename in os.listdir('.'):
    # replace 함수 이용, 새로운 파일 이름 생성
    # os.rename 함수 이용, 파일 이름 변경
    filename.replace("지원")
    os.rename(filename,filename.replace('지원자','합격자'))
    