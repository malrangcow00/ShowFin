# 팀명: Finan길

# 프로젝트명: ShowFin

노션 주소: https://github.com/malrangcow00/ShowFin.git


# 금융 상품 비교 앱

https://jealous-falcon-f89.notion.site/Finan-4f1c724f1dec49a7ba83aeb1e2910634?pvs=4




### 메인페이지
- 최소한5개 이상의 URL 페이지를 사용



1. 예적금 금리 비교 Product 
API
 ProductLIst
      필터링 / 정렬 가능하도록...
   - 은행
   - 예치기간
- 
productDetail 



2. 환율 계산
API 받아와서 ..

   
 국가정보만 두개 입력하는데
. interest

화면단은 하난데..
원화를 입력하면 아래 선택한 국가의 화폐단위 표시
타국 통화 입력 선택시 



3. 집 주변 은행


4. 상품 추천
   프로필에 입력되는 정보
   나이, 자산, 연봉
   나와 나이, 현재 가진 금액, 연봉의 분포가 비슷한 사람들이 가입한 상품을 10개 추천합니다. (Numpy 사용)


상품 모델
- id

프로필 
- id, 가입한 상품 목록(상품 id), 유저이름, 나이, 자산, 연봉, 이메일, 

# 가져와야할 API
### 금융감독원 API
- https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029
- fin_API_URL = 'f5e5273d3415b407b8b70072028c8174
  '
### 한국수출입은행 환율정보 API (환율 계산기)
- https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=C&searchselect=&searchword=
- exchange_API_URL = '9tvmZZArSdQ9sEmu0hZG0wnAU40eZthD'
- https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=9tvmZZArSdQ9sEmu0hZG0wnAU40eZthD&data=AP01

### 카카오맵 API
- https://apis.map.kakao.com/
- map_API_URL = 'fbdd32eecea9ea022e10dec2254581c7'
- ![img.png](img/img.png)