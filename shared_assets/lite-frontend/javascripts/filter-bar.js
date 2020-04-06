$('#filters').hide();
$('#show-filters-link').show();
$('#hide-filters-link').hide();

$('#filters input, #filters select').each(function() {
	if ($(this).val() != ''
		&& $(this).val() != 'Select'
		&& $(this).val() != 'blank'
		&& $(this).attr('type') != 'hidden'
		&& ($(this).attr('type') != 'checkbox' || $(this).attr('type') == 'checkbox' && $(this).attr('checked')))
	{
		$('#filters').show();
		$('#show-filters-link').hide();
		$('#hide-filters-link').show();
	}
});

$('#show-filters-link, #hide-filters-link').click(function() {
	$('#filters').toggle();
	if ($('#filters').is(':visible')) {
		$('#show-filters-link').hide();
		$('#hide-filters-link').show();
	} else {
		$('#show-filters-link').show();
		$('#hide-filters-link').hide();
	}
	return false;
});
