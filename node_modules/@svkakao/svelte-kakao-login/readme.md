# svelte kakao login

[![NPM](https://img.shields.io/badge/svelte-kakao--login-green?logo=svelte)](https://www.npmjs.com/package/@svkakao/svelte-kakao-login)

<br/>

## 모듈 다운로드

    npm install @svkakao/svelte-kakao-login

<br/>

## 기본 사용법

```javascript
/* App.svelte */

<script>
  import KakaoLogin from "@svkakao/svelte-kakao-login";
</script>

<KakaoLogin
  key="..kakao key.."
/>
```

<br/>

### 스타일 변경 유의

```javascript
/* App.svelte */

<script>
  import KakaoLogin from "@svkakao/svelte-kakao-login";
</script>

<KakaoLogin
  key="..kakao key.."
  style=`
    font-size : 12px;
    margin : 0 auto;
  `
/>
```

<br/>

### 파라미터

| params             | value    | default value | description                                                              |
| :----------------- | :------- | :------------ | :----------------------------------------------------------------------- |
| key                | string   | null          | 카카오 개발자 페이지에서 발급받은 key                                    |
| style              | string   | null          | 버튼 스타일 변경                                                         |
| lang               | bool     | false         | 버튼 title의 언어 <br/> `false : korean` <br/> `true : english`          |
| throughTalk        | bool     | true          | 간편 로그인 사용 여부                                                    |
| persistAccessToken | bool     | true          | 세션이 종료된 뒤에도 액세스 토큰을 사용할 수 있도록 로컬 스토리지에 저장 |
| needProfile        | bool     | true          | 사용자 정보 받아오는지 유무                                              |
| useLoginForm       | bool     | false         | 로그인폼 사용 여부                                                       |
| onSuccess          | function | console.log   | 로그인 성공시 실행될 함수 <br/> 로그인 결과를 인자로 받음                |
| onFail             | function | console.log   | 로그인 실패시 실행될 함수 <br/> 로그인 실패 사유를 인자로 받음           |
