async function checkValidity(){
    await $.ajax({
            url:"http://"+"127.0.0.1"+":8000/dashboard",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
            success:function(result) {
                return {result}
            }
            // error: function(xhr, ajaxOptions, thrownError){                    
              
            // }
    })
}

function getDeviceData() {
    var token = localStorage.getItem("access_token");
                if(token == undefined){                  
                    window.location.href = "../../Frontend/templates/Login.html"
                }else{   
  fetch("http://127.0.0.1:8000/devicedata", {
    method:'GET',
    headers: {
    Accept: 'application/json',
    Authorization: 'Bearer ' + localStorage.getItem('access_token')}}).then(
  res => {
    res.json().then(
      data => {
        console.log(data);
        if (data.length > 0) {
          var temp = "";
          data.forEach((itemData) => {
            temp += "<tr>";
            temp += "<td>" + itemData.Shipment_Invoice_Number + "</td>";
            temp += "<td>" + itemData.Device + "</td>";
            temp += "<td>" + itemData.Goods_Type + "</td>";
            temp += "<td>" + itemData.Route_Details + "</td>";
            temp += "<td>" + itemData.Expected_Delivery_Date + "</td></tr>";
          });
          document.getElementById('data').innerHTML = temp;
        }
      }
    )
  }
)
}
  }