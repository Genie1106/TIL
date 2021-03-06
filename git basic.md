# Git & GitHub

### Git에 내 정보 설정

* `git config --global user.name "Mijin Kim"`  : 이름설정
* `git config --global user.email "mijin5122@naver.com"` : 메일 설정
* `git config --global --list` : 정보 설정 확인

### Git repo를 처음 생성한 경우

* `git init` :  git  초기화. 지금 폴더를  git으로 관리하겠다.
* `git remote add origin 주소` : 원격 저장소(remote repository) 주소 등록
  * `git remote set-url origin 주소 ` : 원격 저장소 수정

### Git repo clone한 경우

* `git clone 주소 [폴더이름]` : 이 주소로부터 내용 내려받기
  * 이 경우에는 `git init`,`git remote add origin  주소`를 하지 않아도 이미 다 되어있다.

### Git Commit & Push

*  `git status` : 현재 폴더의 git 상태 확인
*  `git add .` : 현재 폴더의 변경사항들을  commit하기 위해 준비 . 대신에 특정 파일 이름도 가능.
*  `git commit -m "D04 | 190107 AM | Git& CLI"` : commit 변경사항 저장. ' '안은 자유롭게 작성 가능
*  `git push -u origin master` : remote로 등록된 원격 저장소에 commit한 것들 올리기
  * 이 후에는 `git push`만 입력해도 동작한다. `git clone`을 한 경우에도 해당.
  * 이 컴퓨터에서 최초 push인 경우, 로그인 창이 뜨며 로그인을 해준다.

### Git Pull

* `git pull` : GitHub에 올라가 있는 내용들 즉, commit 들을 내려받는 것
* 아침에 오자마자  `git pull` 한번 하고 시작합시다!!



### Git & GitHub 재설정

```bash
# Git 이름, 이메일 재설정
git config --global user.name "Mijin Kim"
git config --global user.email "mijin5122@naver.com"

# GitHub 로그인 정보 초기화
git credential reject
protocol=https
host=github.com
```





