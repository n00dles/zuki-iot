console.log("starting zuki JS script");


jQuery(document).ready(function($) {
    jQuery(".instance").each(function(index,item)
		{
            var id = $(item).data('id')
            console.log(id);
            $.get({url: "/getinstance/"+id, 
                success: function(result){
                    console.log("#ibody-"+id);
                    $("#ibody-"+id).html(result);
                }
            });
        }
    );
});
