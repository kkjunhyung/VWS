# 📊 Django 기반 프로젝트 투표 시스템 개발 보고서

## 1. 개요

본 프로젝트는 웹 기반의 투표 시스템을 구현하는 것을 목표로 하며, 사용자가 다양한 프로젝트에 대해 투표를 진행하고 그 결과를 실시간으로 확인할 수 있는 기능을 제공한다. 관리자는 관리자 페이지를 통해 프로젝트를 등록하고 관리할 수 있다.

---

## 2. 개발 환경

* 언어: Python 3.x
* 프레임워크: Django
* 데이터베이스: SQLite (기본 제공 DB)
* 개발 도구: VS Code
* 운영 환경: Windows

---

## 3. 시스템 구성

### 3.1 전체 구조

본 시스템은 Django의 MVT(Model-View-Template) 구조를 기반으로 설계되었다.

* Model: 데이터베이스 구조 정의
* View: 사용자 요청 처리 및 로직 수행
* Template: 사용자 인터페이스 구성

---

### 3.2 디렉터리 구조

```
voting-website/
├── config/             # 프로젝트 설정
│   ├── settings.py     # 환경 설정
│   ├── urls.py         # URL 라우팅
│
├── voting/             # 앱
│   ├── models.py       # 데이터 모델
│   ├── views.py        # 로직 처리
│   ├── urls.py         # 앱 URL
│   ├── templates/      # HTML 파일
│   │   └── project_list.html
│
├── manage.py           # 실행 파일
```

---

## 4. 주요 기능

### 4.1 프로젝트 등록 기능

* 관리자는 관리자 페이지에서 프로젝트를 등록할 수 있음
* 프로젝트는 제목, 설명, 투표 수로 구성됨

---

### 4.2 프로젝트 목록 조회 기능

* 사용자는 웹 페이지에서 전체 프로젝트 목록 확인 가능
* 각 프로젝트의 제목, 설명, 투표 수 표시

---

### 4.3 투표 기능

* 사용자는 각 프로젝트에 대해 투표 가능
* 투표 시 해당 프로젝트의 투표 수가 1 증가
* 데이터베이스에 실시간 반영

---

### 4.4 정렬 기능

* 투표 수 기준 내림차순 정렬
* 인기 프로젝트가 상단에 표시됨

---

## 5. 데이터베이스 설계

### Project 모델

| 필드명         | 타입           | 설명      |
| ----------- | ------------ | ------- |
| title       | CharField    | 프로젝트 제목 |
| description | TextField    | 프로젝트 설명 |
| votes       | IntegerField | 투표 수    |

---

## 6. 핵심 코드 설명

### 6.1 모델 (models.py)

```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    votes = models.IntegerField(default=0)
```

---

### 6.2 View (views.py)

```python
def project_list(request):
    projects = Project.objects.all().order_by('-votes')
    return render(request, 'project_list.html', {'projects': projects})
```

---

### 6.3 투표 기능

```python
def vote(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.votes += 1
    project.save()
    return redirect('/')
```

---

## 7. 실행 결과

* 웹 페이지에서 프로젝트 목록 확인 가능
* 투표 버튼 클릭 시 투표 수 증가
* 실시간으로 순위 변화 확인 가능

---

## 8. 기대 효과

* 사용자 참여 기반 의사결정 시스템 구현 가능
* 다양한 분야에서 투표 시스템으로 활용 가능
* 웹 서비스 개발에 대한 전반적인 이해 향상

---

## 9. 결론

본 프로젝트를 통해 Django 프레임워크를 활용한 웹 서비스 개발 과정을 학습할 수 있었으며, 데이터베이스 연동 및 사용자 인터페이스 구현 능력을 향상시킬 수 있었다. 향후에는 로그인 기능, 중복 투표 방지 기능 등을 추가하여 보다 완성도 높은 시스템으로 확장할 수 있다.
