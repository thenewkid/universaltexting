

function handleLoginResponse(response) {
	log(response);

  /* 
  
  */
	if (response.status === 'connected') {
    	log("user is logged into fb on this app");
    	if (window.location.pathname === "/")
        window.location = "http://dtd3dgames.appspot.com/authenticate_facebook?fb_user=true"
      else if (window.location.pathname === "/facebook_user_profile")
        log("loading in fb data");
    }

    else if (response.status === 'not_authorized') {

      // The person is logged into Facebook, but not your app.
      log("user is logged into fb but not my app");
    }

    else {

      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      log("user is not logged into fb");
    }
}

function checkLoginState() {
	FB.getLoginStatus(function(response) {
    	handleLoginResponse(response);
    });
}

function loginFB() {
	FB.login(function(response) {
    handleLoginResponse(response);
  });
}

function logoutFB() {
  FB.logout(function(response) {
    log(response);
    window.location.pathname = "/";
  });
}
window.fbAsyncInit = function() {
    FB.init({
    	cookie     : true,
		appId      : '183777251992877',
		xfbml      : true,
		version    : 'v2.5'
	});

    //checkLoginState();
};

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


