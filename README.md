# Django로 수강 신청 페이지 만들기

CNU 2024 fall 스터디 강의 자료

---

## 📚 프로젝트 목표
- Django 프레임워크를 학습하며 실제로 동작하는 수강 신청 시스템을 개발.
- 데이터베이스 설계 및 관리, CRUD 구현, 인증/권한 관리, 검색 및 필터링 기능 등을 단계적으로 학습.
- 복잡한 모델 설계와 확장.

---

## 📆 학습 커리큘럼

### **1주차: Django 개발 환경 설정**
- **목표**: Django 개발 환경을 설정하고 프로젝트를 시작
- **주요 내용**:
  - Django 설치 및 가상환경 설정
  - 개발 서버 실행 및 기본 구조 이해
- **결과**: Django 기본 프로젝트 생성 완료.

---

### **2주차: 데이터베이스와 모델**
- **목표**: Django 모델을 사용하여 데이터베이스를 설계
- **주요 내용**:
  - 과목(Course), 사용자(User) 등 주요 모델 설계
  - 데이터베이스 마이그레이션 및 관리
  - ORM(QuerySet)을 활용한 데이터 조작
- **결과**: 과목 및 사용자 테이블 생성.

---

### **3주차: 과목 관리 및 CRUD 구현**
- **목표**: 과목을 관리할 수 있는 CRUD 기능을 구현
- **주요 내용**:
  - 과목 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 기능
  - `ModelForm`과 `Class-based Views`를 사용한 CRUD 구현
- **결과**: 과목 CRUD 기능 구현 완료.

---

### **4주차: 인증 및 권한 관리**
- **목표**: 인증과 권한을 통해 사용자에 따라 접근을 제한
- **주요 내용**:
  - **JWT 인증**:
    - Django REST Framework의 `SimpleJWT`를 사용하여 토큰 기반 인증 구현.
    - 사용자 로그인 시 JWT 발급 및 API 요청에 대한 인증 처리.
  - **Django 기본 세션 인증**:
    - Django의 기본 인증 시스템(세션 기반)을 활용하여 로그인 및 로그아웃 처리.
  - **Role-Based Access Control (RBAC)**:
    - 사용자 역할(Role)을 정의하여 권한 관리.
    - 교수(Professor), 학생(Student) 등 역할별 접근 권한 설정.
- **결과**:
  - JWT 기반 인증 및 세션 기반 인증 구현.
  - 사용자 역할(Role)에 따른 접근 제어 기능 완성.
---

### **5주차: 복잡한 모델 설계 및 확장 (1)**
- **목표**: 더 정교한 모델링과 기능 확장
- **주요 내용**:
  - `ManyToManyField` 및 관계형 데이터 설계
  - 수강 신청(Enrollment) 모델 구현
  - 수강 신청 기록 모델 생성
- **결과**: 복잡한 데이터 관계 설계 완료.

---

### **6주차: 복잡한 모델 설계 및 확장 (2)**
- **목표**: 복잡한 데이터 구조를 활용하여 실제 수강 신청 로직을 구현
- **주요 내용**:
  - 수강 신청 제한 조건 (학점 초과, 중복 과목 등) 추가
  - 과목의 선수 과목(Prerequisite) 구현
  - 사용자별 수강 신청 현황 관리
- **결과**: 실제 수강 신청 로직 구현 완료.

---

### **7주차: 검색 및 필터링 기능 구현**
- **목표**: 과목을 검색하고 필터링할 수 있는 기능을 추가
- **주요 내용**:
  - `django-filter`를 활용한 필터링
  - 강의명, 교수명, 학점 등 다양한 조건으로 검색
  - REST API로 검색 및 필터링 구현
- **결과**: 강력한 검색 및 필터링 기능 구현.


## 💡 주요 기능
1. **사용자 인증 및 권한 관리**:
   - 로그인/로그아웃, 사용자 등록
2. **과목 관리**:
   - 과목 CRUD
   - 선수 과목 설정 및 데이터 관계 관리
3. **수강 신청**:
   - 수강 신청 및 기록 관리
4. **검색 및 필터링**:
   - 강의명 등으로 검색/필터링

## 강의 자료

https://whatdagodda.notion.site/Python-Django-10930c40e2c4804f857ce9c37dc07f5f?pvs=74
