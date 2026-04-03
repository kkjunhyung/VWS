# 🗳️ Django Voting Web Service

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Chart.js](https://img.shields.io/badge/Chart-Chart.js-orange)

> 주제 기반 투표 시스템 + 실시간 결과 시각화 웹 서비스

---

# 🌐 Live Demo

👉 (배포 후 링크 추가)

```
https://vws-a5fl.onrender.com
```

---

# 📸 Screenshots

### 🏠 메인 화면

* 투표 주제 목록 확인

### 🗳️ 투표 화면

* 항목 선택 및 투표 진행

### 📊 결과 화면

* 그래프 기반 결과 확인
* 순위 및 공동 순위 표시

---

# 🚀 주요 기능

## ✅ 투표 시스템

* 주제별 투표 진행
* 항목 선택 후 투표
* 투표 후 동일 페이지 유지

---

## ✅ 투표 제한 시스템

* 주제별 최대 투표 수 설정 가능
* 제한 초과 시 투표 차단
* “투표수 제한 없음” 옵션 제공

---

## ✅ 결과 시각화

* Chart.js 기반 막대 그래프
* 항목별 투표 수 표시

---

## ✅ 순위 시스템

* 자동 순위 계산
* 공동 순위 지원

```
👑 1등
🥈 2등
🥉 3등
```

---

## ✅ 관리자 기능

* Topic 기반 VoteItem 관리
* Inline UI 제공
* 검색 및 필터 기능

---

## ✅ 투표 초기화

* 관리자/결과 페이지에서 초기화 가능

---

# 🏗️ 시스템 구조

## Backend (Django)

* Models: Topic, VoteItem
* Views: 투표 처리 / 제한 로직 / 결과 계산
* Admin: 데이터 관리 UI

## Frontend

* HTML / CSS / JavaScript
* Chart.js (데이터 시각화)

---

# 🔄 서비스 흐름

```
사용자 → 주제 선택 → 투표 → 결과 확인
```

1. 주제 목록 조회
2. 투표 항목 선택
3. 투표 제한 검증
4. 투표 반영
5. 결과 그래프 출력

---

# 📦 설치 및 실행

## 1️⃣ 프로젝트 클론

```bash
git clone https://github.com/your-username/voting-website.git
cd voting-website
```

---

## 2️⃣ 가상환경 (선택)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 3️⃣ 패키지 설치

```bash
pip install -r requirements.txt
```

---

## 4️⃣ DB 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ 관리자 계정 생성

```bash
python manage.py createsuperuser
```

---

## 6️⃣ 서버 실행

```bash
python manage.py runserver
```

👉 접속:

```
http://127.0.0.1:8000/
```

---

# ⚙️ 관리자 페이지

```
http://127.0.0.1:8000/admin/
```

### 기능

* 투표 주제 생성
* 항목 추가
* 투표 제한 설정
* 제한 없음 설정

---

# 🧱 데이터 모델

```text
Topic
 ├── name
 ├── vote_limit
 └── is_unlimited

VoteItem
 ├── topic (FK)
 ├── title
 ├── description
 ├── votes
 ├── image
 └── link
```

---

# 📊 기술 스택

* Python 3.12
* Django 5.x
* SQLite (기본 DB)
* Chart.js
* HTML / CSS / JavaScript

---

# 💡 핵심 구현 포인트

* 주제 기반 투표 구조 설계
* 투표 제한 / 무제한 로직 분리
* 공동 순위 알고리즘 구현
* Chart.js 시각화
* Django Admin 커스터마이징

---

# 🏁 향후 개선

* 사용자 로그인 기반 1인 1표 제한
* REST API (DRF) 확장
* AWS / Render 배포
* 모바일 UI 개선

---

# 👨‍💻 Author

* 강준형

---

# 📄 License

MIT License
