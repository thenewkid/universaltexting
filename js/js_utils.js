function hide(elementId) {
	$("#" + elementId).hide();
}

function show(elementId) {
	$("#" + elementId).show();
}

function getElement(eid) {
	return document.getElementById(eid);
}

function showModal(modalId) {
	$("#" + modalId).modal();
}

function closeModal(modalId) {
	$("#" + modalId).modal('hide');
}

function log(data) {
	console.log(data);
}

function logArgs(args) {
	each(args, function(i) {
		log(i);
	});
}

function each(args, cb) {
	for (var i = 0, len = args.length; i < len; i++) {
		cb(args[i]);
	}
}

function htmlExists(id) {
	return getElement(id) != null;
}
