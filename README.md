# melon-playlist-extractor

멜론 재생목록을 txt로 저장시켜주는 프로그램

---

## Feature

- `곡 - 아티스트` 형식으로 플레이리스트 목록이 `txt`파일로 저장됨

---

## Usage

- 같은 디렉토리에 크롬 버젼에 맞는 [chromedriver.exe](https://chromedriver.chromium.org/downloads) 파일이 존재해야 작동함
- `memberKey`에 `https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey=` 뒤에 오는 본인의 플레이리스트 번호 8자리를 입력
- delay에 페이지 자동 넘김 지연시간 입력 (1초 이상 권장, 에러가 나면 더 큰 수로 높이기)

---

## Caution

---

## Change Log

- [CHANGELOG.MD](https://github.com/syki66/melon-playlist-extractor/blob/master/CHANGELOG.MD)

---

## Todo List

---

## Build

> pyinstaller melon_playlist_extractor.py --onefile