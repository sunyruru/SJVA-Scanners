# Plex Series Scanner For Korea
국내 방송용 Plex 파일 스캐너입니다. NEXT 릴 기준으로 작성되어 있습니다.

### 사용법
1. Plex Media Server\Scanners\Series 폴더를 만들고 Plex Series Scanner For Korea.py 파일을 복사
[OS별 Plex Media Server 위치](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)
(예: 윈도우 - C:\Users\default\AppData\Local\Plex Media Server\Scanners\Series )
2. TV쇼 라이브러리 편집 화면에서 스캐너 선택. 스캐너 선택 화면이 나오지 않을 경우 Plex 재시작
3. 기존에 등록되어 있는 라이브러리는 모두 다시 스캔해야 합니다. (메타데이터 새로 고침)

### 기존 스캐너와 차이점
- E 문자 다음 숫자를 회차로 인식합니다. (시즌1)
- 타이틀에 숫자가 들어간 경우 시즌+회차로 인식하는 문제를 수정하였습니다. (예: 응답하라 1988)
- 회자 정보가 없을 경우 180411 형식의 날짜를 방송 날짜로 인식합니다.

### 참고사항
 - 기본 스캐너인 Plex Series Scanner를 수정한 스캐너입니다. 기존 코드를 그대로 사용하고 있으니 미드 등에서도 사용 가능 하리라 생각됩니다.

### Todo
 - 파일의 회차 정보와 Daum의 정보가 다를 경우 회차 정보 수정
