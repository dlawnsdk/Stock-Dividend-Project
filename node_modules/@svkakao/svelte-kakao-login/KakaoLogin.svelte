<script lang="ts">
  /* kakao developer's key */
  export let key = null;

  /**
   * kakao login button style
   * require form
   *   style=`
   *      background-color : green;
   *      font-size : 12px;
   *   `
   */
  export let style = null;

  /**
   * kakao button language
   * default is false (korean)
   *          if true, english
   */
  export let lang = false;

  /* other options */
  export let throughTalk = true;
  export let persistAccessToken = true;
  export let needProfile = true;
  export let useLoginForm = false;

  /* login success function */
  export let onSuccess = (response) => {
    console.log("kakao login success \n", response);
  };

  /* login fail function */
  export let onFail = (error) => {
    console.log("kakao login fail \n", error);
  };

  /* kakao initialize */
  if (!window.Kakao) {
    /* Kakao is not defined */
    console.error("kakao.js sdk is not existed");
  } else {
    /* Kakao is defined */
    if (!window.Kakao?.isInitialized()) {
      /* kakao initalize */
      window.Kakao?.init(key);
    }
  }

  /* apply options */
  const method = useLoginForm ? "loginForm" : "login";
  const title = lang ? "Kakao Login" : "카카오 로그인";
  const _style = style || null;

  /* kakao login button click */
  const onLogin = () => {
    (window.Kakao?.Auth)[method]({
      throughTalk,
      persistAccessToken,
      success: (response) => {
        if (needProfile) {
          window.Kakao?.API.request({
            url: "/v2/user/me",
            success: (profile) => {
              const result = { response, profile };
              onSuccess(result);
            },
            fail: onFail,
          });
        } else {
          onSuccess({ response });
        }
      },
      fail: onFail,
    });
  };
</script>

<button style={_style} on:click={onLogin}>{title}</button>

<style>
  button {
    display: inline-block;
    padding: 0px;
    width: 222px;
    height: 49px;
    line-height: 49px;
    color: rgb(60, 30, 30);
    background-color: rgb(255, 235, 0);
    border: 1px solid transparent;
    border-radius: 3px;
    font-size: 16px;
    font-weight: 500;
    text-align: center;
  }
</style>
