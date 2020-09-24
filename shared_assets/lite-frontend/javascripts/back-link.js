$(".govuk-back-link").on("click", function() {
	address = $(this).attr("href");
		window.history.back();
	return false;
});
