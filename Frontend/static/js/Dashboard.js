function checkValidity(){
    $.ajax({
            url:"http://"+"127.0.0.1"+":8000/dashboard",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
            success:function(result) {
                console.log(result)
                localStorage.setItem("user_name", result.response.token)
                document.getElementById("username").innerHTML = result.response.token;
                if(result.response.role == "User"){
                    $("div.shipment").show();
                    $("div.vshipment").show();
                }
                
                else if(result.response.role == "Admin"){
                    $("div.shipment").show();
                    $("div.vshipment").show();
                    $("div.dds").show();
                    $("div.ddsadmin").show();
                }
            }
            // error: function(xhr, ajaxOptions, thrownError){                    
              
            // }
    })
}

// function getCookie(cName) {
//     const name = cName + "=";
//     const cDecoded = decodeURIComponent(document.cookie); //to be careful
//     const cArr = cDecoded .split('; ');
//     let res;
//     cArr.forEach(val => {
//         if (val.indexOf(name) === 0) res = val.substring(name.length);
//     })
//     return res;
// }

function shipdirect(){
    location.href="../templates/Shipments.html"
}

function ddsdirect(){
    location.href="../templates/DeviceDataStream.html"
}

function vshipdirect(){
    location.href="../templates/UserCollection.html"
}
