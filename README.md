# Plex Series Scanner For Korea
Plex Show Scanner

### 사용법
1. Plex Media Server\Scanners\Series 폴더를 만들고 Plex Series Scanner For Korea.py 파일을 복사
[OS별 Plex Media Server 위치](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)
(예: 윈도우 - C:\Users\default\AppData\Local\Plex Media Server\Scanners\Series )
2. TV쇼 라이브러리 편집 화면에서 스캐너 선택. 스캐너 선택 화면이 나오지 않을 경우 Plex 재시작

### 파일별 기능
1. Plex Series Scanner Patch.py
   - 기본 Plex Series Scanners에서 mp4 태그 읽는 부분만 삭제
2. SJVA_Scanner_KoreaTV.py
   - 국내방송용 스캐너. 
   - E 문자 뒤의 숫자 에피소드 번호 인식. 6자리 숫자 날짜 인식
3. SJVA_Scanner_KoreaTV_Download.py
   - 국내방송 다운로드 폴더 전용 스캐너.
   - 폴더명은 무시하고 파일명으로 쇼이름 인식
4. Plex Series Scanner For Korea OLD.py
   - 최초버전.
