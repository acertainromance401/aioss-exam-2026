# AI OSS 실습 시험 최종 보고서

## 저장소 / 제출 정보
- 저장소 링크: 
- 브랜치: 
- PR 링크: 
- Collaborator 추가 확인(`chunsejin`): [ ] 완료

## 문항 1. 협업 워크플로우 구성
### 브랜치 전략 설명 (5문장 이내)
1. `main`을 항상 배포 가능 상태로 유지한다.
2. 작업은 `feature/*` 브랜치에서 짧게 수행한다.
3. 모든 변경은 PR로 병합하고 테스트 결과를 첨부한다.
4. CI 실패 시 원인을 기록하고 수정 후 재실행한다.
5. 문제 발생 시 PR Revert와 Feature Flag OFF로 빠르게 롤백한다.

### 리뷰 코멘트
- 링크/내용: 

## 문항 2. CI 파이프라인 구축 및 최적화
### 워크플로우 실행 링크 (2개 이상)
- 실패 실행: 
- 수정 후 성공 실행: 

### 품질 게이트
- Lint: `ruff check app tests scripts`
- Test: `pytest -q`
- Build gate: `python -m compileall app tests scripts`

### Matrix 전략
- axis1: OS (`ubuntu-latest`, `macos-latest`)
- axis2: Python (`3.11`, `3.12`)

### 최적화 전/후 시간 비교표
| 구분 | 실행 시간 | 비고 |
|---|---:|---|
| 최적화 전 |  |  |
| 최적화 후 |  | pip cache 적용 |

## 문항 3. Shift-left 테스트
### 테스트 실행 로그 요약
- 명령: `python -m pytest -q`
- 결과: 

### 실패 -> 수정 -> 성공 커밋
- 실패 커밋: 
- 수정 커밋: 

### 테스트 전략 설명 (5문장 이내)
1. 변경 비용이 낮은 단위 테스트를 먼저 배치해 빠른 피드백을 받는다.
2. 핵심 비즈니스 로직(old/next recommender)은 단위 테스트로 안정화한다.
3. API 경계(`/health`, `/recommendation`)는 통합 테스트로 계약을 검증한다.
4. Feature Flag OFF/ON 시나리오를 테스트에 포함해 회귀를 줄인다.
5. 실패 테스트를 먼저 만들고 통과시키는 흐름으로 요구사항을 구체화한다.

## 문항 4. Feature Flag + TBD
### 플래그 유형 및 선택 이유
- 유형: 사용자 버킷 기반 rollout
- 이유: 사용자별 일관된 노출 제어와 점진적 배포가 가능

### OFF/ON 동작 증빙
- OFF 캡처/로그: 
- ON 캡처/로그: 

### 롤백 절차 (3단계)
1. `FEATURE_NEXT_RECOMMENDER=false`로 즉시 비활성화
2. 장애 원인 커밋 Revert
3. 정상 버전 재배포 후 모니터링

## 문항 5. 배포 및 운영 메트릭
### 배포 결과
- 실행 명령: `python scripts/deploy_simulation.py`
- 결과 파일: `artifacts/deployment_result.json`

### DORA 지표 수집 요약표
| 지표 | 값 | 수집 방식 |
|---|---:|---|
| lead_time_hours | 6.5 | `scripts/collect_dora_metrics.py` |
| deployment_frequency_per_week | 10 | `scripts/collect_dora_metrics.py` |
| mttr_minutes | 35 | `scripts/collect_dora_metrics.py` |
| change_failure_rate_percent | 8.0 | `scripts/collect_dora_metrics.py` |

### MTTR 단축 액션
- Runbook + On-call alert template를 운영해 진단 시간을 단축한다.

## 최종 체크
- [ ] 요구사항 1~5 답변 완료
- [ ] Actions 링크 2개 이상 첨부
- [ ] 배포 결과 첨부
- [ ] 최종 보고서 작성 완료
