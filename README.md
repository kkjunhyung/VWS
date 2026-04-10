# 🗳️ Voting Website (투표 웹사이트)

Django 기반의 투표 시스템 웹 애플리케이션입니다.
사용자는 투표를 생성하고 참여하며, 결과를 직관적으로 확인할 수 있습니다.

---

## 🚀 주요 기능

### ✔ 투표 생성

* 투표 제목 설정
* 여러 개의 선택지 추가
* 이미지 첨부
* 유튜브 링크 첨부 (버튼 클릭 이동)
* 투표 인원 제한 설정 (또는 무제한)

### ✔ 투표 참여

* 카드 UI 기반 투표
* 버튼 클릭으로 간편 참여
* 인원 제한 초과 시 자동 차단

### ✔ 결과 확인

* 공동 순위 알고리즘 적용
  → 예: 공동 1위, 공동 2위
* 🥇🥈🥉 순위 표시
* Chart.js 기반 막대 그래프
* 투표 수 시각화

### ✔ UI/UX

* 카드 스타일 디자인
* 반응형 웹 (모바일 지원)
* hover 애니메이션
* 직관적인 인터페이스

### ✔ 기타 기능

* 투표 초기화 기능 (확인 알림 포함)
* 이미지 비율 유지 및 자동 리사이징

---

## 🛠️ 기술 스택

* Backend: Django (Python)
* Frontend: HTML, CSS, JavaScript
* Chart: Chart.js
* Database: SQLite3

---

## 📂 프로젝트 구조

```
voting-website/
├── voting/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── topic_list.html
│   │   ├── topic_detail.html
│   │   ├── topic_create.html
│   │   ├── result.html
├── db.sqlite3
├── manage.py
```

---

## ⚙️ 실행 방법

```
# 1. 가상환경 생성
python -m venv venv

# 2. 가상환경 실행 (Windows)
venv\Scripts\activate

# 3. Django 설치
pip install django

# 4. 서버 실행
python manage.py runserver
```

---

## 🎯 프로젝트 목적

* Django 기반 웹 서비스 개발 경험
* 사용자 중심 UI/UX 구현
* 데이터 시각화 (Chart.js) 적용
* 실사용 가능한 투표 시스템 제작

---

## 🔥 향후 개선 방향

* 로그인 및 회원 기능 추가
* 1인 1표 제한 기능
* 댓글 기능
* 관리자 기능 강화
* 클라우드 배포 (AWS / Render)

---

## 👨‍💻 개발자

* 강준형

---

## 📌 라이선스

본 프로젝트는 학습 및 졸업 작품 용도로 제작되었습니다.
