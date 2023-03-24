// async function checkValidity(){
//     await $.ajax({
//         url: "http://127.0.0.1:8000/dashboard", 
//         type: "GET",
//         headers: {"Authorization":'Bearer' + localStorage.getItem('access_token')},
//         success: function(result){
//             // console.log("Value obtained" + result.)
//         }
//     })
// }



async function checkValidity(){
    await $.ajax({
     
            url:"http://"+"127.0.0.1"+":8000/dashboard",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token')},
            success:function(result) {
                return{result}
            }
            // error: function(xhr, ajaxOptions, thrownError){                    
              
            // }
    })
}