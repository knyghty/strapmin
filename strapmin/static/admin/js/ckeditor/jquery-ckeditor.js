django.jQuery(function() {
    function init_cke() {
    	$('textarea[data-type=ckeditortype]').each(function() {
        	if ($(this).data('processed') == "0" && $(this).attr('id').indexOf('__prefix__') == -1) {
	            $(this).data('processed',"1");
	            CKEDITOR.replace($(this).attr('id'));
	        }
	    });
    }

    init_cke();

    $(".add-row a").click(function() {
		init_cke();
		return true;
	});
});
