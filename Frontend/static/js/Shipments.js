async function checkValidity(){
  await $.ajax({
          url:"http://"+ window.location.hostname +":8000/dashboard",
          type:"GET",
          headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
          success:function(result) {
            console.log(result)
            localStorage.setItem("user_name", result.response.token);
            if(result.response.role == "Admin"){
                    $("div.ddsadmin").show();
                }
          }
          // error: function(xhr, ajaxOptions, thrownError){                    
            
          // }
  })
}

// --onclick() function
  var sinum =  document.getElementById("sinum")
  var cnum = document.getElementById("cnum")
  var sdesc= document.getElementById("sdesc")
  var rdetails =  document.getElementById("rdetails")
  var gdtypes = document.getElementById("gdtypes")
  var device = document.getElementById("device")
  var exdate = document.getElementById("exdate")
  var ponum =  document.getElementById("ponum")
  var delnum = document.getElementById("delnum")
  var ndcnum = document.getElementById("ndcnum")
  var bid =  document.getElementById("bid")
  var goodsno = document.getElementById("goodsno")
  var error = document.getElementById("errorm")
  var user_name = localStorage.getItem("user_name")

  function getbulkinput(){
      dataload();
  }

  function clearinput(){
    sinum.value=""
    cnum.value=""
    sdesc.value=""
    rdetails.value=""
    gdtypes.value=""
    device.value=""
    exdate.value=""
    ponum.value=""
    delnum.value=""
    ndcnum.value=""
    bid.value=""
    goodsno.value=""
  }

  function dataload(){
      var data = {
        "user_name": user_name,
        "Shipment_Invoice_Number": sinum.value,
        "Container_Number" : cnum.value,
        "Shipment_Description" : sdesc.value,
        "Route_Details" : rdetails.value,
        "Goods_Type" : gdtypes.value,
        "Device" : device.value,
        "Expected_Delivery_Date" : exdate.value,
        "PO_Number" : ponum.value,
        "Delivery_Number" : delnum.value,
        "NDC_Number" : ndcnum.value,
        "Batch_ID" : bid.value,
        "Serial_Number_of_goods" : goodsno.value,
        }
        $.ajax({
          url: "http://"+window.location.hostname+":8000/shipment", 
          type: "POST",
          headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
          dataType: "json",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function (result) {
            error.style.display="flex";
            error.innerHTML="Shipment Created!"
            error.style.color="green"
            console.log(result)
            // console.log("Registered Successfully")
              // when call is sucessfull
           },
           error: function(xhr){
            if(xhr.responseJSON.detail=="Please enter the required fields!"){
              error.style.display="flex";
              error.innerHTML="Please enter the required fields!"
            }
            else if (xhr.responseJSON.detail=="PO Number should be a number of six digits."){
              error.style.display="flex";
              error.innerHTML="PO Number should be a number of six digits."
            }
            else if (xhr.responseJSON.detail=="Shipment already exists."){
              error.style.display="flex";
              error.innerHTML="Shipment already exists."
            }
            else if (xhr.responseJSON.detail=="Shipment number should only be alphanumeric."){
              error.style.display="flex";
              error.innerHTML="Shipment number should only be alphanumeric."
            }
            else if (xhr.responseJSON.detail=="Please enter the description within 120 characters."){
              error.style.display="flex";
              error.innerHTML="Please enter the description within 120 characters."
            }
          }
        }); // ajax call closing
        // console.log(json.innerHTML=JSON.stringify(data))
    }