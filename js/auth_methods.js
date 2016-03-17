
function googleAuth() {
	if (document.URL.indexOf("localhost") != -1) 
		window.location = "http://localhost:" + window.location.port + "/authenticate_google";
	else if (document.URL.indexOf("dtd3dgames") != -1) {
		window.location = "https://dtd3dgames.appspot.com/authenticate_google";
	}
}

