function checkValidity(){
    $.ajax({
            url:"http://"+"127.0.0.1"+":8000/dashboard",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
            success:function(result) {
                console.log(result)
                document.getElementById("username").innerHTML = result.response.token;
            }
            // error: function(xhr, ajaxOptions, thrownError){                    
              
            // }
    })
}

function shipdirect(){
    location.href="../templates/Shipments.html"
}

function ddsdirect(){
    location.href="../templates/DeviceDataStream.html"
}
