$(document).ready(function(){


    $(document).on("click", ".menu", function(){
        $(".channel-wrapper").css("display","inline");
        $(".background").css("display","block");

    });


    $(document).on("click", ".ion-close", function(){
        $(".channel-wrapper").css("display","none");
        $(".background").css("display","none");

    });

    $(document).on("click", ".background", function(){
        $(".channel-wrapper").css("display","none");
        $(".background").css("display","none");

    });

});


