$(document).ready(function() {
	if (htmlExists("new_user_modal"))
		showModal("new_user_modal");
	else if (htmlExists("welcome-modal"))	
		showModal("welcome-modal");
});

