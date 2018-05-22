# Plex Series Scanner For Korea
국내 방송용 Plex 파일 스캐너입니다. NEXT 릴 기준으로 작성되어 있습니다.

### 사용법
1. Plex Media Server\Scanners\Series 폴더를 만들고 Plex Series Scanner For Korea.py 파일을 복사
[OS별 Plex Media Server 위치](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)
(예: 윈도우 - C:\Users\default\AppData\Local\Plex Media Server\Scanners\Series )
2. TV쇼 라이브러리 편집 화면에서 스캐너 선택. 스캐너 선택 화면이 나오지 않을 경우 Plex 재시작
3. 기존에 등록되어 있는 라이브러리는 모두 다시 스캔해야 합니다. (메타데이터 새로 고침)

### 추가 설정
- wonipapa님의 [다음 시리즈 에이전트](https://github.com/wonipapa/DaumMovieTVSeries.bundle)를 사용하시는 경우 8라인 ```KOR_AGENT = USING_DAUM_SERIES_AGENT``` 로 변경.
- 로그파일을 보시려면 ```USE_LOG = True``` 로 변경하시고 ```LOGFILE```을 절대경로로 변경.


### 기존 스캐너와 차이점
- E 문자 다음 숫자를 회차로 인식합니다. (시즌1)
- 타이틀에 숫자가 들어간 경우 시즌+회차로 인식하는 문제를 수정하였습니다. (예: 응답하라 1988)
- 회자 정보가 없을 경우 180411 형식의 날짜를 방송 날짜로 인식합니다.
- 천회 이상 인식.

### 참고사항
 - 기본 스캐너인 Plex Series Scanner를 수정한 스캐너입니다. 기존 코드를 그대로 사용하고 있으니 미드 등에서도 사용 가능 하리라 생각됩니다.


### ChangeLog
##### 0.1.5 (2018-04-25)
- 시즌제 대응
  + wonipapa님 에이전트를 사용하시는 경우 S2를 붙여야 하나, 파일명 수정없이 E03앞에 시즌2, 혹은 숫자로 끝나는 경우 시즌으로 인식합니다.
- 회차를 무시해야하는 경우
  + 일부 릴은 회차정보가 잘못 되어 있습니다. 이런 방송은 날짜로 매칭하는게 더 좋기 때문에 회차정보를 무시하는게 좋습니다. 무시 할 방송은 ```EPISODE_NUMBER_IGCNORE = ['한국기행', '인간극장']``` 형식으로 방송을 추가해주면 됩니다.
