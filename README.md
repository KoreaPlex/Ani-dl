# Ani-dl

Beta (2020-10-10)

# 패치노트

### 2020-10-11

BS11 을 시즌 11로 인식하는 점 수정

FLAG 기능 추가

[HorribleSubs] Re Zero kara Hajimeru Isekai Seikatsu 이 릴의 이 작품은 시즌없이 Absolutet Numbering으로 뿌리니까 후처리 할 때 자동으로 변경

ex : [HorribleSubs] Re Zero kara Hajimeru Isekai Seikatsu - 36 [720p].mkv  -->>  Re  제로부터 시작하는 이세계 생활 (2016)\S02\Re  제로부터 시작하는 이세계 생활 (2016) S2E11 [720p].mkv

### 2020-10-12

리네이밍 관련 버그 픽스

캐시 삭제 추가

캐시 용량이 수십기가가 되는 문제 

### 2020-10-13

자동 리네이밍 (시트 제외) : 특수문자 폴더명에 들어가는 버그 수정

### 2020-10-14

몇몇 버그 수정

특정 키워드 전부 다운로드 옵션 추가

특정 년도 (2020-09:2020-10 이런 식) 다운로드 기능 추가


# 필요사항

Apikey 

# 특징


![image](https://user-images.githubusercontent.com/70357228/93705827-98a88c80-fb5b-11ea-925a-d97c2332fd19.png)

![image](https://user-images.githubusercontent.com/70357228/93705830-a2ca8b00-fb5b-11ea-84b5-a9aec71faa56.png)



![image](https://user-images.githubusercontent.com/70357228/93707361-c47e3f00-fb68-11ea-822d-23c6fbcbb182.png)

![image](https://user-images.githubusercontent.com/70357228/95635333-16124d80-0ac7-11eb-8fa5-ed5a4a707457.png)

![image](https://user-images.githubusercontent.com/70357228/95635354-27f3f080-0ac7-11eb-9d1e-9867bc95166d.png)

![image](https://user-images.githubusercontent.com/70357228/95635922-c03ea500-0ac8-11eb-960c-de7982e4e1bd.png)

![image](https://user-images.githubusercontent.com/70357228/95635981-ec5a2600-0ac8-11eb-8124-4f1bcfe84afd.png)


Plex TVDB에 맞추어 시즌과 에피소드명을 자동으로 리네이밍

No Torrent Client is Needed.

애니메이션 정리 기능 추가

구글 시트를 통해 공동으로 파일 정리하는 기능 추가 (디스코드 내에서 권한 요청 바람)

https://discord.gg/e2YHZCe


# 파일 정리에 대한 이해

기본적으로 이해가 있어야지 사용을 하던가 아니면 기여를 하던가 할 수 있으므로..

우선, 자동으로 정리되는 부분은

myanimelist에서 시즌을 파악하는 것입니다. (anidb는 밴이 잦아서..


![image](https://user-images.githubusercontent.com/70357228/95666817-7de49900-0b98-11eb-9cb4-954691b60020.png)

시놉시스에서 Fourth 시즌이라 써있으면, TVDB에서도 4시즌이겠구나 하고 리네이밍 하는 것이죠.

즉. Myanimelist에서 틀린 거라면 노답이라는 것입니다.

이부분은 Sheet에서 수정을 해주셔야합니다.


자동 다운로드는 다음과 같은 로직을 거칩니다

다운 -> 파일 정리 진입 -> 우선적으로 myanimelist 참조해 파일 정리 -> 시트 참조(여기서 시트에 반영할 게 있다면 추가적으로 정리)


따라서, 시트는 최종적으로 '가장 중요'한 리네이밍 참조처가 되는 것입니다.


아... 메뉴얼 작성하자니까 넘 어렵네요

누가 좀 해주세요.
