setSmsFormSubmit();





function setSmsFormSubmit() {
	var sms_form = document.sms_form;
	$(sms_form).submit(function(){
		var sms_num_elems = document.getElementsByClassName("sms_number");
		var numbers_csv = collectNumbersCsv(sms_num_elems);
		var message = this.message.value;
		sendSmsData(message, numbers_csv);
		return false;
	});
}

function setVoiceFormSubmit() {
	var voice_form = document.voice_form;
	$(voice_form).submit(function() {
		var numberElements = document.getElementsByClassName("number");
		var numbers_csv = collectNumbersCsv(numberElements);
		var voice_type = this.children.voice_gender.selectedOptions[0].value;
		var voice_language = this.children.voice_language.selectedOptions[0].value;
		var voice_message = this.recording.value;
		sendVoiceData(voice_message, numbers_csv, voice_type, numbers_csv);
		return false;
	});
}
function sendSmsData(message, to) {
	$.ajax({
		url: document.URL,
		data: {"to":to,"message":message},
		method: "post",
		success: function(dt) {
			console.log(dt);
		}
	});
}

function sendVoiceData(vm, to, vt, vl) {
	$.ajax({
		url: document.URL + "makecall",
		data: {"voice_to":to,"vm":vm, "vt":vt, "vl":vl},
		method: "post",
		success: function(dt) {
			console.log(dt);
		}

	});
}

function collectNumbersCsv(numberElements) {
	var numbers = [];
	var i;
	var current_number;
	for (i = 0, len = numberElements.length; i < len; i++) {
		current_number = numberElements[i].value;
		if (validNumber(current_number));
			numbers.push(current_number);
	}
	return numbers.join(",");
}