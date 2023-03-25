// Assigning varibales to HTML input fields

    var username =  document.getElementById("uname")
    var email =  document.getElementById("semail")
    var password = document.getElementById("spwd")
    var cpassword = document.getElementById("scpwd") 
    var json = document.getElementById("jsons")
   
    function getinput(){
      dataload();
      // if(validationuser()==true &&
      // validationemail()==true &&
      // validationpwd()==true &&
      // validationcpwd()==true){
      //   dataload();
      // }
      // else{
      //   validation();
      // }
    }

    function validation(){
      validationuser();
      validationemail();
      validationpwd();
      validationcpwd();
    }

    function dataload(){
      var data = {
          "username":username.value,
          "emailid":email.value,
          "password":password.value,
        }
        $.ajax({
          url: "http://127.0.0.1:8000/signup", 
          type: "POST",
          dataType: "json",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function (result) {
            alert("Registered Successfully")
            // console.log("Registered Successfully")
              // when call is sucessfull
           },
           error: function (xhr) {
             console.log(xhr.responseJSON.detail)
           // check the err for error details
             if (xhr.responseJSON.detail=="Invalid Password."){
              validationpwd(xhr.responseJSON.detail);
             }
           }
        }); // ajax call closing
        console.log(json.innerHTML=JSON.stringify(data))
    }

    // ajax function to remove all 

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

    function validationpwd(value){
      var c  = password.value;
      var strength = 0;
      var tip = "";
      let pwdErrorMsg = document.getElementById("errorMessagePwd");
      if (c==""){
        pwdErrorMsg.style.display = "flex";
        pwdErrorMsg.innerHTML =value;
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

    // *additional code and comments*

    // function hideErrorMsg(){
    //   document.getElementById("errorMessageUserName").style.display = "none";
    //   document.getElementById("errorMessageEmail").style.display = "none";
      
    // }

    // bt.addEventListener("click", function(){  
    //   var data = {
    //     "Email Id":email.value,
    //     "Password":pwd.value
    //   }
    //   console.log(json.innerHTML=JSON.stringify(data))
    // })

    // function getinput(){
      // console.log(Array)
    //   let einput=String(document.getElementById("semail").value);
    //   let ninput=String(document.getElementById("uname").value);
    //   let pinput=String(document.getElementById("spwd").value);
    //   let cpinput=String(document.getElementById("scpwd").value);
    //   console.log(ninput+einput+pinput+cpinput);
    // }

     // function signup(form){
    //   var uname = form.username.value;
    //   var xmlHTTP = new XMLHttpRequest();
    //   xmlHTTP.open("post","Login",true);
    //   xmlHTTP.onreadystatechange = function(){
    //     if(xmlHTTP.readyState == 4 && xmlHTTP.status == 200){
    //       results();
    //     }
    //   }
    // }