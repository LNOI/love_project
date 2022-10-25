var check_send = 0;


if((sessionStorage.getItem("username") == "thanhloi" || sessionStorage.getItem("username") == "ainhu"  ) && sessionStorage.getItem("password")=="23012001"){
   
} else{
  window.location.replace("/login");
}
$(".letter_check_accept").hide()
$(".card_noftication").hide();
$("#card-noti-close").click(function(e){
    $(".card_noftication").hide();
})
$(".message_for_you").click(function (e) { 
    e.preventDefault();
    const val_id = $(this).attr('id');
    var formdata= {
        id: val_id
    }
    $.ajax({
        method: "POST",
        url: "/get_one_message",
        dataType: "json",
        contentType: "application/json",
        data : JSON.stringify(formdata)
    }).done(function( data){
        console.log(data)
        $(".card_noftication").show();
        // console.log(data['thumbnail'])
        $('#card-noti-thumbnail').attr('src','static/img/'+data['thumbnail']);
        $('#card-noti-title').html(data['title'])
        $('#card-noti-text').html(data['content'])
        
    }).fail(function(){
        alert("Failure")
    })   
});

var content_main = NaN
var pre_content_main = 0
var after_content_main = NaN
var accept = 'Dong y'
$(".form-check-input").click(function(e){
    if($(".form-check-input:checked" ).val()=="yes"){
      accept = "Dong y";
    }else{
      accept = "Tu choi";
    }
})



$(".content-accept").hide()
$(".letter_main").hide()
$(".cursor").hide();
$("#noti-heart").click(function(e){
    $(".letter_main").show()
})

var check_send = 0;

var page_letter = 1;
$("#swipe_icon").click(function(e){
  page_letter+=1;
  if(page_letter < 4){
    $("#letter_img").attr('src', 'static/img/letter/'+page_letter+'.jpg');
  }
  else{
    if(check_send==0){
      page_letter=4
      $(this).attr('src','static/img/icon/letter_send.png');
      $("#letter_img").attr('src', 'static/img/letter/'+page_letter+'.jpg');
      $(".letter_check_accept").show()
      check_send =1;
    }else{
        $.ajax({
          method: "POST",
          url: "/write_accept",
          dataType: "json",
          contentType: "application/json",
            data : JSON.stringify({content:accept})
        }).done(function( data){
          $(".letter_main").hide();
          $("#noti-heart").hide();
        }).fail(function(){
            alert("Failure")
        }) 
    }
 
  }
})

