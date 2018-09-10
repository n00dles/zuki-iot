console.log("starting zuki JS script");


jQuery(document).ready(function($) {
    jQuery(".instance").each(function(index,item)
		{
            var id = $(item).data('id')
            $.get({url: "/getinstance/"+id, 
                success: function(result){
                    var obj = JSON.parse(result);
                    var values =  obj.values.split(',');
                    var timestamps =  obj.timestamps.split(',');
                                        
                    $("#ibody-"+id).html(obj.current+"("+obj.type+")");

                    var ctx = document.getElementById("chart-"+id);
                    var myChart = new Chart(ctx, {
                        type: 'line',
                            data: {
                                labels: timestamps,
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


function formatDate(date, fmt) {
    function pad(value) {
        return (value.toString().length < 2) ? '0' + value : value;
    }
    return fmt.replace(/%([a-zA-Z])/g, function (_, fmtCode) {
        switch (fmtCode) {
        case 'Y':
            return date.getUTCFullYear();
        case 'M':
            return pad(date.getUTCMonth() + 1);
        case 'd':
            return pad(date.getUTCDate());
        case 'H':
            return pad(date.getUTCHours());
        case 'm':
            return pad(date.getUTCMinutes());
        case 's':
            return pad(date.getUTCSeconds());
        default:
            throw new Error('Unsupported format code: ' + fmtCode);
        }
    });
}
