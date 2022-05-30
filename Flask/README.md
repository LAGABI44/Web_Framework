# Flask
## vscode에서 Flask 설치하기
1. 빈 파일 생성 후 가상환경 폴더 생성
```
python -m venv env
```
2. 파이썬 인터프리터 설정 `command+shift+P`   
  => python:Select Interpreter   
  => Python 3.10.4('env':venv)   
3. 터미널 새로 꺼내서 (env) 표시 확인
4. 가상환경의 pip 업데이트 진행
```
python -m pip install --upgrade pip
```
5. Flask 설치
```
python3 -m pip install flask
```
