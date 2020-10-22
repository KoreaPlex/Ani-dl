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

### 2020-10-14 (2)

args 추가. 우분투나 시놀로지 및 윈도우에서 인자를 줌으로써 자동화 가능.

사용법은 ani-dl.py --help 를 쳐보기를 권장 (주기적으로 바뀌거나 잠수함 패치 가능성이 있습니다.)

    다음과 같은 argument가 사용이 가능하다.

    parser.add_argument('--keyword_download_start' , type=str , help="키워드 다운로드 자동시작. 키워드는 하나만 입력. 해당 키워드가 들어간 모든 애니메이션 다운로드. (리스트에서)")
    parser.add_argument('--number_download_start' , type=int , help="수량 다운로드 자동시작. 숫자만 입력.")
    parser.add_argument('--auto_download_start', type=bool, help="설정 그대로 다운로드 시작 True or False로 bool 타입만 입력")
    parser.add_argument('--raname_folder_type', type=str, help="해당 폴더 내부 파일들 전부(recursive) 리네임하기.\n"
                        "1. 구글 시트 리네이밍 (시트에 키워드가 있는 파일만 리네이밍 및 파일 이동)\n"
                        "2. 자동 리네이밍 (시트 제외)\n"
                        "3. Absolute Numbering 리네이밍 (원피스, 코난같은 작품 파일 처리)\n"
                        "4. 자동 리네이밍 (시트 포함)\n"
                        "구분자는 |\n"
                        "작성 예시 : 3|F:\# INCOMING\최신 애니\원피스 (1998)")
    parser.add_argument('--date_download_start', type=str, help="특정 날짜에 포함된 것들만 다운. ex ) 2020-09:2020-10 또는 2019-3: 또는 :2020-1")
    parser.add_argument('--wait' , type=int , help="특정 시간마다 신작 리스트 재호출 후 스크립트 그대로 다시시작. 숫자만 입력. 입력하지 않을 경우 1사이클 돌고 종료.")


버전에 따라서 달라질 수 있으므로 위에서 언급했던 것처럼 ani-dl.py --help 를 쳐보기를 권장.

### 2020-10-16

자동으로 꺼지는 버그 수정

### 2020-10-21

ani365 일부 지원

tmp folder 위치 변경 가능

### 2020-10-22

ani365 인자 지원

다음을 참조 (--wait 인자랑 같이 쓰길 추천)

    parser.add_argument('--ani365' , type=str , help='ani365에 캐싱된 애니메이션 다운. 명령어는 그대로 (ex : 최신:300|나루토|원피스:100|제로부터')

각종 버그 수정

### 2020-10-23

나루토:-103 같은 인자로 특정 에피소드 다운 가능

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
