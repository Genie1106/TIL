# TIL

### day02

#### 파일명 변경

1. os.chdir(r"폴더 주소")
2. os.listdir('.') : 현재 working directionary의 파일목록 리스트
3. os.rename("바꾸려는 이름","바꿀 이름")

### Git 설정 

* git config --global user.name "Mijin"
* git config --global user.email "mijin5122@naver.com"
* git config --global --list
* git init : git 초기화. git으로 관리하겠다.
* git remote add origin 주소 : 원격 저장소 등록
* git remote set-url origin 주소 : 원격 저장소 수정

### Git Commit & Push

* git status : 현재 폴더의  git 상태
* git add . : 현재 폴더의 변경사항을 commit하기 위해 준비
* git commit -m 'file_name'  : commit 변경 사항 저장
* git push -u origin master : remote로 등록된 원격 저장소
  * 이후에는  git push 만 입력해도 동작



* Markdown 기록할 것. 

  * Typora or VSCode
  * Github Student Developer Pack
