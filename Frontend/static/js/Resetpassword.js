// Assigning varibales to HTML input fields
  // --onclick() function
  var fpwd = document.getElementById("fpwd")
  var rfpwd = document.getElementById("rfpwd")

  function inputpasswordreset(){
    if (validationfpwd()==true &&
    validationrfpwd()==true){
        passwordreset();
    }
    else{
        validationpassword();
    }
  }

  function validationpassword(){
    validationfpwd();
    validationrfpwd();
  }

  function passwordreset(){
    $.ajax({
        url: "http://127.0.0.1:8000/resetpassword", 
        type: "PUT",
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({
            "emailid": localStorage.getItem('emailid'),
            "password" : fpwd.value
          }),
        success: function (result) {
            alert(result.message)
           console.log(result);
           window.location.href="../../Frontend/templates/Login.html"
         },
         error: function(xhr) {
     
         // check the err for error details
         }
      }); // ajax call closing
      // console.log(json.innerHTML=JSON.stringify(data))
  }

  function validationfpwd(){
    var c  = fpwd.value;
    var strength = 0;
    var tip = "";
    let errorfMessagePwd = document.getElementById("errorfMessagePwd");
    if (c==""){
        errorfMessagePwd.style.display = "flex";
        errorfMessagePwd.innerHTML="Please Enter your password.";
      return false;
    }

    //  checking password length
    if (c.length<3){
        errorfMessagePwd.style.display = "flex";
      tip+="Make the password longer. ";
      errorfMessagePwd.innerHTML=tip;
      return false;
    } else {
      strength+=1;
    }

    //  checking upper and lowercase
    if(c.match(/[a-z]/) && c.match(/[A-Z]/)){
      strength+=1;
    } else {
        errorfMessagePwd.style.display = "flex";
      tip+="Use both lowercase and uppercase letters. ";
      errorfMessagePwd.innerHTML=tip;
      return false;
    }

    //  checking numbers
    if(c.match(/\d/)){
      strength+=1;
    } else {
        errorfMessagePwd.style.display = "flex";
      tip+="Include at least one number. ";
      errorfMessagePwd.innerHTML=tip;
      return false;
    }
    
    //  checking special characters
    if(c.match(/[^a-zA-Z\d]/)){
      strength+=1;
    } else {
        errorfMessagePwd.style.display = "flex";
      tip+="Include at least one special character. ";
      errorfMessagePwd.innerHTML=tip;
      return false;
    }
    // obtains input
    errorfMessagePwd.style.display = "none";
    errorfMessagePwd.innerHTML ="";
    return true;
  }

  function validationrfpwd(){
    var c  = fpwd.value;
    var d  = rfpwd.value;
    let errorrfMessageCpwd = document.getElementById("errorrfMessageCpwd");
    if (d==""){
        errorrfMessageCpwd.style.display = "flex";
        errorrfMessageCpwd.innerHTML ="Re-enter Your Password";
      return false;
    }
    if (c != d){
        errorrfMessageCpwd.style.display = "flex";
        errorrfMessageCpwd.innerHTML ="Passwords don't match";
      return false;
    }
    else{
        errorrfMessageCpwd.style.display = "none";
        errorrfMessageCpwd.innerHTML ="";
      return true;
    }
  }