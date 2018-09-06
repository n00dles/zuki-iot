console.log("starting zuki JS script");


jQuery(document).ready(function($) {
    jQuery(".instance").each(function(index,item)
		{
            var id = $(item).data('id')
            $.get({url: "/getinstance/"+id, 
                success: function(result){
                    var obj = JSON.parse(result);
                    $("#ibody-"+id).html(obj.current);
                }
            });
        }
    );
});
