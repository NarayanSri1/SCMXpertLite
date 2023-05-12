// Assigning varibales to HTML input fields
  // --onclick() function
    let emailid =  document.getElementById("email")
    let password = document.getElementById("pwd")
    // var json = document.getElementById("json")
    
    let captchaText = document.querySelector('#captcha');
    var ctx = captchaText.getContext("2d");
    ctx.font = "30px Roboto";
    ctx.fillStyle = "#08e5ff";

    let userText = document.querySelector('#textBox');
    let submitButton = document.querySelector('#submitButton');
    let output = document.querySelector('#output');
    let refreshButton = document.querySelector('#refreshButton');
    let loginButton = document.querySelector('#btn');
    let alphaNums = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let emptyArr = [];

    function captcha(){
      userText.value = "";
      let refreshArr = [];
      for (let j = 1; j <= 7; j++) {
        refreshArr.push(alphaNums[Math.floor(Math.random() * alphaNums.length)]);
      }
      ctx.clearRect(0, 0, captchaText.width, captchaText.height);
      c = refreshArr.join('');
      ctx.fillText(refreshArr.join(''),captchaText.width/4, captchaText.height/2);
      output.innerHTML = "";
      loginButton.style.display="none";
    }

    for (let i = 1; i <= 7; i++) {
        emptyArr.push(alphaNums[Math.floor(Math.random() * alphaNums.length)]);
        }
        
        var c = emptyArr.join('');
        ctx.fillText(emptyArr.join(''),captchaText.width/4, captchaText.height/2);
  
        userText.addEventListener('keyup', function(e) {
          // Key Code Value of "Enter" Button is 13
          if (e.keyCode === 13) {
            if (userText.value === c) {
              output.classList.add("correctCaptcha");
              output.innerHTML = "";
            } else {
              output.classList.add("incorrectCaptcha");
              output.innerHTML = "Incorrect, please try again";
            }
          }
          });
          submitButton.addEventListener('click', function() {
            if (userText.value === c) {
              output.classList.add("correctCaptcha");
              output.innerHTML = "";
              loginButton.style.display="initial";
            } else {
              output.classList.add("incorrectCaptcha");
              output.innerHTML = "Incorrect, please try again.";
              loginButton.style.display="none";
            }
            });
          refreshButton.addEventListener('click', function() {
              userText.value = "";
              let refreshArr = [];
              for (let j = 1; j <= 7; j++) {
              refreshArr.push(alphaNums[Math.floor(Math.random() * alphaNums.length)]);
              }
              ctx.clearRect(0, 0, captchaText.width, captchaText.height);
              c = refreshArr.join('');
              ctx.fillText(refreshArr.join(''),captchaText.width/4, captchaText.height/2);
              output.innerHTML = "";
              });
    
    

    function clearinput(){
      emailid.value=""
      password.value=""
    }

    function loadinput(){
      if(validationEmail()==true &&
      validationPwd()==true){
        dataload();
        clearinput();
      }
      else{
        validation();
      }
    } 
    
    function validation(){
      validationEmail();
      validationPwd();
    }

    function dataload(){
        var data = {
            "emailid": emailid.value,
            "password": password.value,
          }
          $.ajax({
            url: "http://"+window.location.hostname+":8000/login", 
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (result) {
              // alert("User is Present!")
              console.log(result.access_token)
              localStorage.setItem("access_token", result.access_token)
    
              // for local
            // redirecting to Dashboard
            window.location.href = "../../Frontend/templates/Dashboard.html"

            // for cloud
            // window.location.href="/templates/Dashboard.html"

             },
             error: function(xhr) {
              let emailErrorMsg = document.getElementById("errorMessageEmail")
              let pwdErrorMsg = document.getElementById("errorMessagePwd")
              if(xhr.responseJSON.detail=="Email not found."){
                emailErrorMsg.style.display="flex";
                emailErrorMsg.innerHTML="Email not found.";
                captcha();
                return false
              }
              else if(xhr.responseJSON.detail=="Incorrect Password."){
                pwdErrorMsg.style.display="flex";
                pwdErrorMsg.innerHTML="Incorrect Password.";
                captcha();
                return false
              }
              else{
                emailErrorMsg.innerHTML ="";
                pwdErrorMsg.innerHTML="";
                return true;
              }
             // check the err for error details
             }
          }); // ajax call closing
          // console.log(json.innerHTML=JSON.stringify(data))
      }

      function validationEmail(){
        var a = emailid.value;
        let emailErrorMsg= document.getElementById("errorMessageEmail")
        if (a==""){
          emailErrorMsg.style.display="flex";
          emailErrorMsg.innerHTML ="Please Enter Your Registered Email Address";
          return false;
        }
        else{
          emailErrorMsg.style.display="none";
          emailErrorMsg.innerHTML ="";
          return true;
        }
      }

      function validationPwd(){
        var b = password.value;
        let pwdErrorMsg= document.getElementById("errorMessagePwd");
        if(b==""){
          pwdErrorMsg.style.display="flex";
          pwdErrorMsg.innerHTML ="Please Enter Your Password";
          return false;
        }
        else{
          pwdErrorMsg.style.display="none";
          pwdErrorMsg.innerHTML ="";
          return true;
        }
      }

