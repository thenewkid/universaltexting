
function googleAuth() {
	if (document.URL.indexOf("localhost") != -1) 
		window.location = "http://localhost:" + window.location.port + "/authenticate_google";
	else if (document.URL.indexOf(".appspot") != -1) {
		window.location = "https://dylans-gae-template.appspot.com/authenticate_google";
	}
}

