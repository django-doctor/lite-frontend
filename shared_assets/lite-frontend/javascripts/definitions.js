$.fn.changeElementType = function(newType) {
    var attrs = {};

    $.each(this[0].attributes, function(idx, attr) {
        attrs[attr.nodeName] = attr.nodeValue;
    });

    var newelement = $("<" + newType + "/>", attrs).append($(this).contents());
    this.replaceWith(newelement);
    return newelement;
};

$('[data-max-length]').each(function() {
    var originalText = $(this).text();
    var shrunkText = $(this).text().substring(0, $(this).data("max-length"));

    if (originalText.length != shrunkText.length) {
        $(this).text(shrunkText + "...");
        $(this).append("<a href='#' class='govuk-link govuk-link--no-visited-state govuk-!-margin-left-2' data-more-text='" + originalText + "'>More</a>");
    }
});

$('[data-more-text]').click(function() {
    $(this).parent().text($(this).data("more-text"));
    return false;
})

$('[data-definition-title]').each(function() {
	$(this).addClass("lite-link--definition");
	$(this).changeElementType("a").attr("href", "#");
});

$('[data-definition-title]').click(function() {
    LITECommon.Modal.showModal($(this).data("definition-title"), $(this).data("definition-text"), false, true, {maxWidth: '500px'});
    return false;
})
