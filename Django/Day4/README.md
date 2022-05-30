# Day4
- 날짜 : 


## bz2 압축 풀기


- 파일명 : shape_predictor_68_face_landmarks.dat.bz2 
- [참고1](https://4369.tistory.com/entry/%EB%A6%AC%EB%88%85%EC%8A%A4-%EC%95%95%EC%B6%95%EB%AA%85%EB%A0%B9)
- [참고2](https://windowsreport.com/extract-decompress-bz2-file/)
```
$ bunzip2 -k filename.bz2
```

## 필수 변경 사항
|No|파일명|변경 전|변경 후|
|---|---|---|---|
|01|settings.py|'DIRS': []|'DIRS': [BASE_DIR/'templates']|
|02|sticker.html </br> stickerResult.html|x|templates\Landing|
