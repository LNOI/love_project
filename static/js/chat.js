$.ajax({
    method: "GET",
    url: "/get_chat",
}).done(function( data){
    if(data.success ==true){
        window.location.replace("/love");
    }
}).fail(function(){
    alert("Failure")
})