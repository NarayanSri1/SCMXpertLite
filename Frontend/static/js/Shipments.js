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
  

  function getbulkinput(){
      dataload();
  } 
  
  function dataload(){
      var data = {
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
          url: "http://127.0.0.1:8000/shipment", 
          type: "POST",
          dataType: "json",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function (result) {
            alert("Data Loaded Successfully")
            // console.log("Registered Successfully")
              // when call is sucessfull
           },
           error: function (err) {
            console.log(err)
           // check the err for error details
           }
        }); // ajax call closing
        // console.log(json.innerHTML=JSON.stringify(data))
    }

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
    

    function valsi(){
      var a = sinum.value;
    }