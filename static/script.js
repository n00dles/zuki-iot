console.log("starting zuki JS script");


jQuery(document).ready(function($) {
    jQuery(".instance").each(function(index,item)
		{
            var id = $(item).data('id')
            $.get({url: "/getinstance/"+id, 
                success: function(result){
                    var obj = JSON.parse(result);
                    var values =  obj.values.split(',');
                    
                    $("#ibody-"+id).html(obj.current+"("+obj.type+")");
                    console.log("VALUES: " + values);
                    console.log(values.length);
                    values.forEach(element => {
                        console.log(element);
                    });
                    var ctx = document.getElementById("chart-"+id);
                    var myChart = new Chart(ctx, {
                        type: 'line',
                            data: {
                                labels: [16.00, 16.30, 17.00, 17.30,18.00, 18.30, 19.00, 19.30],
                                datasets: [{
                                    label: 'temp',
                                    borderColor: 'ff0000',
                                    data: values,
                                    fill: false,
                                }]
			
                        }
                    }
              
                )
            }
        }
    )
})
});
