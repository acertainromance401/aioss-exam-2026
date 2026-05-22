## 변경 요약
- 

## 테스트 내역
- [ ] `python -m ruff check app tests scripts`
- [ ] `python -m pytest -q`
- [ ] 수동 확인(필요 시): `/health`, `/recommendation`

## 롤백 계획
1. 문제 PR Revert
2. `FEATURE_NEXT_RECOMMENDER=false`로 즉시 비활성화
3. 마지막 정상 배포 아티팩트 기준으로 재배포

## 리뷰 체크리스트
- [ ] 요구사항 반영 여부 확인
- [ ] 실패 로그/원인/수정 이력 확인
- [ ] 테스트 케이스 적절성 확인
- [ ] Feature Flag OFF 기본값 확인
- [ ] 배포/메트릭 아티팩트 생성 확인
