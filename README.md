# FitHub

> Team 신사숙녀 |
> 김성민 김예인 장인건
> 
![캡처](https://github.com/user-attachments/assets/14a65eb9-a1ee-4e3c-a5ca-ab251925f78f)

### 📂 Content

- [🔎 기술 스택](#기술-스택)
- [🔎 서비스 고안 배경](#서비스-고안-배경)
- [🔎 서비스 매커니즘](#서비스-매커니즘-사용-가이드)
- [🔎 주요 기능](#주요-기능)
- [🔎 상세 기능](#상세-기능)
- [🔎 FE 폴더 구조](#FE-폴더-구조)
- [🔎 와이어프레임](#와이어프레임)
- [🔎 데이터베이스 구조](#데이터베이스-구조)
- [🔎 api 명세](#api-명세)
- [🔎 개발 과정](#개발-과정)
- [🔎 팀 소개](#팀-소개)

<br>

## 🛠️기술 스택

![기술 스택](meong_signal/static/readme/new_stack.png)
<br>

> 프론트엔드 (FrontEnd)

- React
- HTML5
- CSS
- JavaScript
- 스타일링: Styled-Components
- 포매터: ESLint + Prettier
- 라우팅: React Router
- HTTP 클라이언트: Axios

> 백엔드 (BackEnd)

- Django Redis

> 데이터베이스 관리 (Database Management)

- AWS RDS (MySQL)

> 서버 배포 (Server Deployment)

- AWS EC2

> 협업 툴 (Collaboration Tools)

- Notion
- Slack
- Git
- GitHub
- Figma

<br>

## 🌟서비스 고안 배경

대개 견주들은 바쁘거나, 일정이 존재하여 강아지를 산책시킬 시간을 내기 어려울 때가 종종 있습니다.
이에 따라 일정의 보수를 받고 강아지를 대신 산책시켜주는 '도그워커'가 등장하기도 하였습니다.

그러나 보수가 목적이 아닌 단순 강아지와 함께 산책을 하고자 하는 일반인도 존재하며, 이러한 무보수 도그워커까지 폭넓게 포함하여
견주와 도그워커를 매칭해주는 서비스가 있다면 편리할 것입니다.

산책자는 혼자 하는 산책보다 더 즐거운 시간을 보낼 수 있고, 귀여운 강아지와의 교감을 통해 더욱 특별한 추억을 만들 수 있습니다. 견주들은 강아지가 충분히 운동하고 행복하게 산책할 수 있어서 안심할 수 있죠!

또한, 단순 산책 뿐만 아니라 챌린지, 업적, 추천 산책로 등 다양한 기능을 통해 산책의 건강한 즐거움을 체험하고, 다각적 방면의 사용자 건강 증진을 기대합니다.

이제 강쥐시그널과 더 건강하개, 더 귀엽개 산책하세요!

또한, 단순 산책 뿐만 아니라 앱 내 다양한 재미요소와 미션을 걸어 산책의 즐거움을 사용자에게 체험하게함으로써, 다각적인 방면에서의 건강을 증진시키는 것을 기대합니다.

<br><br>

## 🔗서비스 매커니즘; 사용 가이드

![가이드1](meong_signal/static/readme/guide1.png)
![가이드2](meong_signal/static/readme/guide2.png)

```python
강쥐시그널은 견주와 도그워커를 연결하는 플랫폼으로, 바쁜 생활 속에서도 강아지에게 충분한 운동을 제공하기 위해 만들어졌습니다.
강아지와 산책을 원하는 사용자는 자신의 위치를 기반으로 근처에서 강아지를 산책시킬 수 있는 도그워커를 찾습니다.
도그워커는 원하는 강아지를 선택하고 견주와 채팅을 통해 산책 일정을 조율할 수 있습니다.

산책 중에는 견주가 강아지의 위치를 실시간으로 추적할 수 있으며, 산책이 끝난 후에는 산책 기록을 조회하고 리뷰를 남길 수 있습니다.
이 외에도 추천 산책로와 다양한 챌린지 기능을 제공하여 사용자들이 더욱 즐겁고 건강한 산책을 즐길 수 있도록 돕습니다.

 강쥐시그널은 단순히 강아지 산책을 돕는 것을 넘어, 강아지와 사람 모두에게 즐거운 시간을 제공하고자 합니다.
이 서비스를 통해 도그워커는 강아지와의 시간을 통해 스트레스를 해소하고 건강을 증진시킵니다.
또, 견주가 자신의 바쁜 일정으로 인해 강아지 산책에 대해 걱정하거나 불안해하는 부담을 덜어줍니다.
강쥐시그널은 강아지와 견주, 그리고 도그워커 모두에게 윈-윈(win-win) 상황을 제공하며,
사용자의 건강과 행복을 동시에 추구하는 산책의 새로운 접근 방식을 제공합니다.
```

<br>

**⭐ '내'가 강아지의 '도그워커'로써 어플리케이션을 사용할 때!**

> 1. 홈 화면에서 내 주변의 산책 가능한 강아지를 조회합니다.
>
> 2. 마음에 드는 강아지를 발견했나요? 강아지의 프로필을 클릭하여 보호자와 채팅을 시작합니다.
>
> 3. 채팅으로 약속을 조율하고, 캘린더 버튼을 눌러 약속을 생성합니다.
>
> 4. 약속 날짜가 되면 보호자와 컨택하고, 강아지와 산책을 시작합니다! (추천 산책로 서비스를 이용 가능합니다.)
>
> 5. 산책을 완료하면, 다시 강아지를 보호자에게 돌려 보내고 리뷰를 작성합니다.

<br>

**⭐ '내'가 강아지의 '보호자'로써 어플리케이션을 사용할 때!**

> 1. '내 정보' 화면에서 강아지를 등록합니다. (성별, 나이, 성격 등을 설정할 수 있습니다.)
>
> 2. 내 강아지의 현재 상태에 따라 '내 정보' 창에서 강아지의 상태를 변경할 수 있습니다!
>
>    > 심심해요 : 강아지가 산책을 원하는 상태로, 도그워커의 지도에 내 강아지 정보가 표시됩니다.
>    >
>    > 산책중! : 도그워커와 강아지가 산책을 시작하면 자동으로 전환되는 상태입니다. 다른 도그워커의 지도에 강아지 정보가 표시되지 않습니다.
>    >
>    > 쉬는 중 : 강아지가 산책을 원하지 않는 상태/산책이 필요없는 상태로, 다른 도그워커의 지도에 강아지 정보가 표시되지 않습니다.
>
> 3. 도그워커에게 채팅이 오면, 약속을 조율하고 약속을 생성 및 확인합니다.
>
> 4. 도그워커가 약속 날 산책을 시작하면, '지도' 화면의 '산책현황'에서 내 강아지가 어디 있는지 확인할 수 있습니다.
>
> 5. 도그워커의 산책이 끝나면, 도그워커에게 리뷰를 써 주세요!

<br>

## 🔔주요 기능

![주요기능](meong_signal/static/readme/primefunc.png)

<br><br>
**🗺️사용자 위치 기반 지도**

- 도그워커의 현재 위치를 기반으로 **주변의 강아지 정보**를 불러옵니다.
- 견주의 집 위치를 기반으로 강아지 정보를 생성합니다.
- 도그워커가 견주의 강아지와 산책 중일 때, 견주는 도그워커의 현재 위치를 원격으로 볼 수 있습니다.
- 도그워커가 **이동한 경로**가 지도에 표시되며, **이동 거리와 소모 칼로리**가 계산됩니다.

---

**💬실시간 채팅**

- 도그워커가 지도에서 강아지의 정보를 확인하고, 견주와 **채팅을 시작**할 수 있습니다.
- 채팅방 안에서 날짜와 시간, 약속명을 설정하여 **약속을 생성**할 수 있습니다.
- 채팅방 목록에서 곧 다가오는 **산책 약속을 확인**할 수 있습니다.

---

**🙌다양한 재미요소**

- 다양한 업적을 달성하고, **칭호**를 획득할 수 있습니다. 칭호는 당신의 이름을 더욱 빛내줄거에요!
- 강아지와 산책하는 것만으로 **챌린지**를 달성하고, 재화를 획득할 수 있습니다. 획득한 재화는 물건 구매나 리뷰 작성 시 상대방에게 선물할 수 있습니다.
- **산책 기록 데이터**를 통해 내가 얼마나 산책했는지 확인할 수 있습니다.

<br>

## ✨상세 기능

![detail1](meong_signal/static/readme/new_detail1.png)
<br><br>

![detail2](meong_signal/static/readme/new_detail2.png)
<br><br>

**⭐카테고리 별 기능**

> **💛산책**
```python
- 지도에서 반경 2km 내의 강아지 정보를 확인 가능합니다.
- 지도에서 강아지 프로필을 탭해 강아지 주인과 채팅을 시작할 수 있습니다. 
- 산책을 시작하면 현 위치부터 움직이는 경로가 지도에 표시됩니다.
- 산책하는 동안 이동 거리가 계산됩니다.
- 산책 종료 후, 산책에서의 소모 칼로리가 계산됩니다.
- 도그워커가 산책하는 동안 보호자는 원격으로 도그워커의 현 위치를 확인할 수 있습니다.
- 추천 경로를 저장할 수 있고, 저장한 경로는 산책 때 활용할 수 있습니다.
- 산책 기록을 열람할 수 있고, 날짜별 산책 그래프가 표시됩니다.  
```

> **💛채팅**
```python
- 읽지 않은 채팅은 색인되어 편하게 확인 가능합니다.
- 실시간 통신을 지원합니다.
```

> **💛강아지**
```python
- 자신의 강아지를 등록할 수 있습니다. 
- 강아지 별 산책 기록을 확인할 수 있습니다. 산책 날짜, 이동 거리, 소모 칼로리, 주고받은 리뷰가 표시됩니다.
- 강아지의 상태를 변경할 수 있습니다.
- 강아지의 성격에 따라 태그를 지정할 수 있습니다. 지정한 태그는 필터링에 사용됩니다. 
```

> **💛약속**
```python
- 채팅 페이지 안에서 약속을 생성할 수 있습니다. 약속 이름, 만나는 날짜 및 시간을 선택 가능합니다.
- 곧 다가오는(3일 이내의) 약속이 채팅방 상단에 표시됩니다.
- 약속을 수락하지 않은 채로 약속 날짜보다 하루가 지나면, 자동으로 약속이 제거됩니다.  
```

> **💛리뷰**
```python
- 산책 종료 후, 도그워커와 견주는 서로 상대방에게 리뷰를 작성할 수 있습니다. 
- 리뷰 작성 시 견주는 도그워커에게 별점을 줄 수 있습니다.
- '멍'을 선물 가능합니다.
- '내 정보' 페이지의 리뷰 관련 탭에서 남기거나 남겨진 리뷰를 확인할 수 있습니다.
```

> **💛업적**
```python
- 업적을 달성해 칭호를 획득할 수 있습니다.
- 획득한 칭호를 대표 칭호로 설정하여 채팅 시 이름 옆에 노출시킬 수 있습니다.
- 업적 현황을 열람할 수 있습니다. 
```


> **💛그 외 기능**
```python
- 한국관광공사가 제공하는 산책 데이터를 활용해 내 현재 위치 주변 추천 산책로 정보를 제공합니다.
- 현재 멍을 자유롭게 충전 가능합니다.
- 멍샵에서 상품 페이지를 확인할 수 있습니다.
- 토글 버튼으로 지도에서 현재 산책이 가능한 강아지(심심한 강아지)만 조회 가능합니다.
- 회원가입, 정보 수정 시 우편번호 검색으로 도로명 주소 입력이 가능합니다.
- 챌린지 기능을 통해 재화 '멍'을 획득 가능합니다.
- 회원가입 때 입력한 비밀번호를 DB에 저장할 때 해싱하여 저장합니다. 
```

## 🙌시장 진입 전략

> **❤️초기 자본 투자로 홍보 효과 기대**

위치 기반 산책로 추천 시스템에 요즘 미디어 트렌드에 걸맞는 '인증 챌린지'를 접목합니다. 본 서비스를 이용하며 추천 산책로에 방문하고, '인증샷'을 SNS에 올리는 강쥐시그널 산책 인증 챌린지를 진행합니다. 
챌린지의 경품으로 강쥐시그널의 로고가 삽입된 강아지 목줄, 하네스, 물병 등 상품을 제공하며, 이를 통해 일상적인 강아지 산책에서 서비스의 자연스러운 노출과 홍보 효과를 기대합니다.

> **❤️유동 잠재 고객이 많은 곳에 홍보물 부착**

본 서비스의 잠재 고객인 '바쁜 일정 때문에 강아지 산책을 불가피하게 하지 못한 경험이 있는 견주', '강아지와 함께 산책을 하고 싶은 경험이 있는 일반인'이 자주 방문하는 공원이나 동물병원, 애견용품샵 등 관련 업체들과 제휴하여 홍보물을 부착합니다. 



## 🗒️FE 폴더 구조

```
├─ .github
│  ├─ ISSUE_TEMPLATE
│  └─ PULL_REQUEST_TEMPLATE.md
├─ .gitignore
├─ .prettierrc
├─ eslint.config.mjs
├─ package-lock.json
├─ package.json
├─ public
│  └─ index.html
├─ README.md
├─ setting.json
├─ src
│  ├─ 🧾apis
│  ├─ App.css
│  ├─ App.jsx
│  ├─ 🖼️assets
│  │  ├─ fonts
│  │  ├─ icons
│  │  └─ images
│  ├─ ✨components
│  │  ├─ Achievement
│  │  ├─ Button
│  │  ├─ Calendar
│  │  ├─ Chat
│  │  ├─ Dog
│  │  ├─ Footer
│  │  ├─ Goods
│  │  ├─ Graph
│  │  ├─ Header
│  │  ├─ Image
│  │  ├─ Input
│  │  ├─ Layout
│  │  ├─ Map
│  │  ├─ Rate
│  │  ├─ Reservation
│  │  ├─ Review
│  │  ├─ Schedule
│  │  ├─ Tag
│  │  ├─ Trail
│  │  └─ Walk
│  ├─ 💾hooks
│  │  ├─ useForm.js
│  │  ├─ useKakaoMap.js
│  │  └─ useUserMap.js
│  ├─ index.css
│  ├─ index.js
│  ├─ 🗂️pages
│  │  ├─ Chat
│  │  │  ├─ ChatList.jsx
│  │  │  └─ ChatRoom.jsx
│  │  ├─ Home.jsx
│  │  ├─ Login.jsx
│  │  ├─ Map
│  │  │  ├─ MapInfo.jsx
│  │  │  ├─ MapStatus.jsx
│  │  │  ├─ MapStatusUser.jsx
│  │  │  └─ TagFiltering.jsx
│  │  ├─ MeongShop
│  │  │  ├─ MeongShop.jsx
│  │  │  └─ MyGoods.jsx
│  │  ├─ MyInfo
│  │  │  ├─ GoalStatus.jsx
│  │  │  ├─ MoreRecordMyDogWalk.jsx
│  │  │  ├─ MyInfoEdit.jsx
│  │  │  ├─ MyInfoMain.jsx
│  │  │  ├─ MyWalk.jsx
│  │  │  ├─ OwnerReview.jsx
│  │  │  ├─ RecordMyDogWalk.jsx
│  │  │  ├─ RegisterDog.jsx
│  │  │  ├─ ReviewReceived.jsx
│  │  │  ├─ ReviewWritten.jsx
│  │  │  └─ UserReview.jsx
│  │  ├─ NotFound.jsx
│  │  ├─ SignUp
│  │  ├─ SocialLogin
│  │  │  ├─ GoogleAuth.jsx
│  │  │  ├─ KakaoAuth.jsx
│  │  │  └─ NaverAuth.jsx
│  │  ├─ TopUp.jsx
│  │  └─ Walk
│  ├─ reset.css
│  └─ 🥪utils
└─ webpack.config.js
```


## 💎와이어프레임

![와이어프레임](meong_signal/static/readme/frame.png)
<br>

#### [🛠️강쥐시그널 와이어프레임 프로토타입 링크](https://www.figma.com/design/YznRx0ey7UWGjUKVWEql8c/%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85?node-id=1-17&t=e4APDaxG8BwdyHzq-1)

<br>

## 🗃️데이터베이스 구조

![erd](meong_signal/static/readme/erd2.png)
<br>

#### [🛠️강쥐시그널 ERD 링크](https://www.erdcloud.com/d/8iGrcJThkHzbaZ5nH)

<br>

## ⛓️api 명세

#### [🛠️강쥐시그널 기능명세 노션 링크](https://abyss-2.notion.site/e607658be211483a9aa4f76c5e8223c2?pvs=4)

<br>

## 💻개발 기간

**24.07.15~24.08.03**

> **아이디어 회의** | 07.15
>
> **기획, 피그마 작업** | 07.15 ~ 07.18
>
> **개발, 테스트** | 07.18 ~ 08.03

## 😎팀 소개

멋쟁이사자처럼 인하대학교 12기 중앙 해커톤 1팀, 감자탕후루 팀입니다.

![팀 소개 페이지](meong_signal/static/readme/team.png)

| 김시원                                   | 김애리                               | 백세희                                 | 유승인                                           | 이영주                                 |
| ---------------------------------------- | ------------------------------------ | -------------------------------------- | ------------------------------------------------ | -------------------------------------- |
| BE                                       | FE                                   | BE                                     | FE                                               | FE                                     |
| [@seaniiio](https://github.com/seaniiio) | [@aeli22](https://github.com/aeli22) | [@sae2say](https://github.com/sae2say) | [@seung-in-Yoo](https://github.com/seung-in-Yoo) | [@abyss-s](https://github.com/abyss-s) |

<br>
