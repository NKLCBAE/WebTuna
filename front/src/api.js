<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
const BASE_URL = 'http://j7a403.q.ssafy.io:8443/api'
=======
const BASE_URL = 'https://j7a403.q.ssafy.io:8443/api'
>>>>>>> 65b58c3 (chore: API https 적용)

const ACCOUNTS_URL = '/accounts'
const WEBTOONS_URL = '/webtoons'

const USER_URL = '/user'

const LOGIN_URL = '/login'
const SIGNUP_URL = '/signup'
const EMAIL_URL = '/email'
const NICKNAME_URL = '/nickname'

const SEARCH_IMG_URL = '/search/image'
<<<<<<< HEAD
=======
const BASE_URL = "http://localhost:8000/api/";
=======
const BASE_URL = 'https://j7a403.p.ssafy.io:8443/api'
>>>>>>> 1013f2b (fix: backend 통신 api 수정)

const ACCOUNTS_URL = "accounts/";
const WEBTOONS_URL = "webtoons/";

const USER_URL = "user/";

const LOGIN_URL = "login/";
const LOGOUT_URL = "logout/";
const INFO_URL = "info/";
const SIGNUP_URL = "signup/";
const EMAIL_URL = "email/";
const NICKNAME_URL = "nickname/";
const PASSWORD_URL = "check/";

const SEARCH_IMG_URL = "search/image/";
>>>>>>> 6e82ed7 (feat: toonbti 질문&보기 구현)

const TOONBTI_URL = "games/question/";

const TOON_LIST_URL = 'list/'
=======
const DETAIL_URL = '/detail'
>>>>>>> 7bb19ad (feat: detai l페이지 UI 구성)

const api = {
  login: () => BASE_URL + ACCOUNTS_URL + USER_URL + LOGIN_URL,
  logout: () => BASE_URL + ACCOUNTS_URL + USER_URL + LOGOUT_URL,
  fetchInfo: () => BASE_URL + ACCOUNTS_URL + USER_URL + INFO_URL,

  // signupSlice
  signup: () => BASE_URL + ACCOUNTS_URL + USER_URL + SIGNUP_URL,
  checkEmail: () => BASE_URL + ACCOUNTS_URL + USER_URL + EMAIL_URL,
  checkNickname: () => BASE_URL + ACCOUNTS_URL + USER_URL + NICKNAME_URL,

  // editSlice
  checkPassword: () => BASE_URL + ACCOUNTS_URL + USER_URL + PASSWORD_URL,

  //uploadSlice
  fetchUpload: () => BASE_URL + WEBTOONS_URL + SEARCH_IMG_URL,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

  //toonlistSlice
  fetchToonlist: (pageNum) => BASE_URL + WEBTOONS_URL + TOON_LIST_URL + pageNum,
<<<<<<< HEAD
>>>>>>> 921bee3 (feat: 웹툰 전체 목록 api 연결)
=======

  //detailSlice
  detail:(webtoonId) => BASE_URL + WEBTOONS_URL + '/' + webtoonId + DETAIL_URL,
>>>>>>> 7bb19ad (feat: detai l페이지 UI 구성)
}
=======
=======

  //toonBTISlice
>>>>>>> 71b23ff (feat: 각각의 웹툰 상세페이지 이동 구현)
  fetchToonBTI: () => BASE_URL + TOONBTI_URL,
};
>>>>>>> 7ddf941 (feat: toonbti slice&api 생성 및 store 등록)

export default api
