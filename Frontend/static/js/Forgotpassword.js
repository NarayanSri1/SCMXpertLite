// Assigning varibales to HTML input fields
  // --onclick() function
  let fpemail =  document.getElementById("fpemail")
  // var json = document.getElementById("json")
 
  function emailenter(){
    $.ajax({
        url: "http://"+window.location.hostname+":8000/forgotpwd", 
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
            "emailid": fpemail.value,
          }),
        success: function (result) {
           console.log(result.emailid);
           localStorage.setItem("emailid",result.emailid)
           // for local
          //  window.location.href = "../../Frontend/templates/Resetpassword.html"

           // for cloud
            window.location.href="../templates/Resetpassword.html"
         },
         error: function(xhr) {
          let femailErrorMsg = document.getElementById("ferrorMessageEmail")
          if(xhr.responseJSON.detail=="Email not found."){
            femailErrorMsg.style.display="flex";
            femailErrorMsg.innerHTML="Email not found.";
            return false
          }
          else if (fpemail=="") {
            femailErrorMsg.style.display="flex";
            femailErrorMsg.innerHTML="Please enter your registered email address";
            return false
          }
          else{
            femailErrorMsg.innerHTML="";
            return true;
          }
         // check the err for error details
         }
      }); // ajax call closing
      // console.log(json.innerHTML=JSON.stringify(data))
  }

