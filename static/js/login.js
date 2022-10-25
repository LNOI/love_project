
$(".signin-button").click(function (e) { 
    const username = $(".user-input").val();
    const password = $(".pass-input").val();
    var formdata= {
        username: username,
        password:password
    }
    $.ajax({
        method: "POST",
        url: "/login_love",
        dataType: "json",
        contentType: "application/json",
        data : JSON.stringify(formdata)
    }).done(function( data){
        console.log(data)
        if(data.success ==true){
            sessionStorage.setItem("username",formdata.username);
            sessionStorage.setItem("password",formdata.password);
            window.location.replace("/love");
        }
    }).fail(function(){
        alert("Failure")
    })   
});

