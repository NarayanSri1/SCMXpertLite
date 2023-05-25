// Assigning varibales to HTML input fields
    var username =  document.getElementById("uname")
    var email =  document.getElementById("semail")
    var password = document.getElementById("spwd")
    var cpassword = document.getElementById("scpwd") 
    var urole = document.getElementById("urole") 
    var json = document.getElementById("jsons")
    
    function getinput(){
      if(validationuser()==true &&
      validationemail()==true &&
      validationpwd()==true &&
      validationcpwd()==true){
        dataload();
      }
      else{
        validation();
      }
    }

    function validation(){
      validationuser();
      validationemail();
      validationpwd();
      validationcpwd();
    }

    function clearinput(){
      username.value=""
      email.value=""
      password.value=""
    }

    function dataload(){
      var data = {
          "username":username.value,
          "emailid":email.value,
          "password":password.value,
          "role":urole.value
        }
        $.ajax({
          url: "http://"+window.location.hostname+":8000/signup", 
          type: "POST",
          dataType: "json",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function (result) {
            clearinput();
            console.log(result)
            // for local
            window.location.href = "../../Frontend/templates/Login.html"

            // for cloud
            // window.location.href="../templates/Login.html"
           },
           error: function(xhr) {
             console.log(xhr.responseJSON.detail)
           // check the err for error details
             let emailErrorMsg = document.getElementById("errorMessageEmail");
             let pwdErrorMsg = document.getElementById("errorMessagePwd");
             if(xhr.responseJSON.detail=="User already exists."){
              emailErrorMsg.style.display = "flex";
              emailErrorMsg.innerHTML ="User already exists.";
             return false
             }

             if(xhr.responseJSON.detail=="Password doesn't follow pattern."){
              pwdErrorMsg.style.display = "flex";
              pwdErrorMsg.innerHTML = "Password doesn't follow pattern.";
             }

          //  else if (xhr.responseJSON.detail=="Invalid Password."){
          //    validationpwd(xhr.responseJSON.detail);
          //    }
           }
        }); // ajax call closing
        console.log(json.innerHTML=JSON.stringify(data))
    }

    function validationuser(){
      var a  = username.value;
      let userErrorMsg = document.getElementById("errorMessageUserName");
      if (a ==""){
        userErrorMsg.style.display = "flex";
        userErrorMsg.innerHTML ="Please Enter Your Name";
        return false;
      }
      if (a.length<3 || a.length>20){
        userErrorMsg.style.display = "flex";
        userErrorMsg.innerHTML ="Username must have 3-20 characters";
        return false;
      }
      if (a.startsWith('_')||a.endsWith('_')){
        userErrorMsg.style.display = "flex";
        userErrorMsg.innerHTML ="Username shouldn't start or end with '_'";
        return false;
      }
      else{
        userErrorMsg.style.display = "none";
        userErrorMsg.innerHTML ="";
        return true;
      }
    }

    function validationemail(){
      var b  = email.value;
      let emailErrorMsg = document.getElementById("errorMessageEmail");
      if (b==""){
        emailErrorMsg.style.display = "flex";
        emailErrorMsg.innerHTML ="Please Enter Your Email Address";
        return false;
      }
      else{
        emailErrorMsg.style.display = "none";
        emailErrorMsg.innerHTML ="";
        return true;
      }
    }

    function validationpwd(){
      var c  = password.value;
      var strength = 0;
      var tip = "";
      let pwdErrorMsg = document.getElementById("errorMessagePwd");
      if (c==""){
        pwdErrorMsg.style.display = "flex";
        pwdErrorMsg.innerHTML="Please Enter your password.";
        return false;
      }

      //  checking password length
      if (c.length<3){
        pwdErrorMsg.style.display = "flex";
        tip+="Make the password longer. ";
        pwdErrorMsg.innerHTML=tip;
        return false;
      } else {
        strength+=1;
      }

      //  checking upper and lowercase
      if(c.match(/[a-z]/) && c.match(/[A-Z]/)){
        strength+=1;
      } else {
        pwdErrorMsg.style.display = "flex";
        tip+="Use both lowercase and uppercase letters. ";
        pwdErrorMsg.innerHTML=tip;
        return false;
      }

      //  checking numbers
      if(c.match(/\d/)){
        strength+=1;
      } else {
        pwdErrorMsg.style.display = "flex";
        tip+="Include at least one number. ";
        pwdErrorMsg.innerHTML=tip;
        return false;
      }
      
      //  checking special characters
      if(c.match(/[^a-zA-Z\d]/)){
        strength+=1;
      } else {
        pwdErrorMsg.style.display = "flex";
        tip+="Include at least one special character. ";
        pwdErrorMsg.innerHTML=tip;
        return false;
      }
      // obtains input
      pwdErrorMsg.style.display = "none";
      pwdErrorMsg.innerHTML ="";
      return true;
    }

    function validationcpwd(){
      var c  = password.value;
      var d  = cpassword.value;
      let cpwdErrorMsg = document.getElementById("errorMessageCpwd");
      if (d==""){
        cpwdErrorMsg.style.display = "flex";
        cpwdErrorMsg.innerHTML ="Re-enter Your Password";
        return false;
      }
      if (c != d){
        cpwdErrorMsg.style.display = "flex";
        cpwdErrorMsg.innerHTML ="Passwords don't match";
        return false;
      }
      else{
        cpwdErrorMsg.style.display = "none";
        cpwdErrorMsg.innerHTML ="";
        return true;
      }
    }