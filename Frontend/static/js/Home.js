function openNav(){
    document.getElementById('sidebar').style.width="250px";
    document.getAnimations('main').style.marginLeft="250px"; 
}
function closeNav(){
  document.getElementById('sidebar').style.width = "0";
  document.getElementById('main').style.marginLeft= "0";
}

function logout(){
  localStorage.removeItem('access_token')
  window.location.href="../templates/Login.html"
  alert("Session ended")
}
