# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 저장소 개요

백준 온라인 저지(BOJ) 문제 풀이 저장소. 풀이 파일을 인스타그램 카드뉴스 PNG로 변환하는 자동화 스크립트 포함.

## 디렉터리 구조

- `solved/{bronze,silver,gold,platinum}/` — 난이도별 Python 풀이 파일 (파일명 = 문제번호.py)
- `notes/` — 알고리즘 개념 정리 마크다운
- `card-news/날짜/문제번호/` — 생성된 카드뉴스 PNG 저장 위치
- `scripts/` — 카드뉴스 생성 도구

## 카드뉴스 생성

풀이 Python 파일 → HTML → PNG 5장 변환 파이프라인:

```bash
# 1. HTML 생성
python scripts/generate_card_html.py --src solved/silver/1436.py --out /tmp/card.html

# 2. PNG 스크린샷 (Puppeteer 필요)
node scripts/card_news_screenshot.js --html /tmp/card.html --out card-news/2026-04-10/1436/
```

또는 `/card-news` 스킬로 전체 자동화 실행 가능.

## 풀이 파일 주석 형식

`generate_card_html.py`가 아래 태그를 파싱해 카드뉴스 메타데이터를 추출함:

```python
# Day: 42
# 알고리즘: 브루트포스
# 시간: 30분
# 생각: 풀이 아이디어 설명
# 회고: 배운 점
# 입력: 예제 입력값
# 출력: 예제 출력값
# 조건: 제약 조건
```

태그가 없으면 폴더명으로 난이도를 자동 추론함 (`solved/silver/` → Silver).

## 의존성 설치

```bash
npm install   # puppeteer (카드뉴스 스크린샷용)
```

Python 표준 라이브러리만 사용하므로 별도 pip 설치 불필요.
