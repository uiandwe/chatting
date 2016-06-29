$(document).ready(function(){



    namespace = '/spoqa'; // change to an empty string to use the global namespace
    var socket = io.connect('http://127.0.0.1:5000' + namespace);
    socket.on('response', function(msg) {
        if(msg.type == "before_chat"){/*이전 채팅 리스트*/
            beforeChat(msg)

        }
        else if(msg.type == "insert"){
            insertChat(msg)
        }
        else if(msg.type == "update"){
            updateChat(msg)
        }
        else if(msg.type == "delete"){
            deleteChat(msg)
        }
        else{

        }
    });


    function beforeChat(msg){
        data = msg.data;
        for (var i in data) {
            insertText(data[i].comment, data[i].created_at, data[i].user_id, data[i].self, data[i].chat_id, data[i].permalink)
        };
    }

    function insertText(text, created_at, user_id, self, chat_id, permalink){
        var append_str = '<li>';
        text = "<span class='comment' data-chat-id='"+chat_id+"'>"+text+"</span>"
        if(self == 1){
            append_str = "<li class='text-right'>"
            self = "<div class='tool-wrapper'><button type='button' class='btn_update' ><i class='ion-edit'></i></button><button type='button' class='btn_delete' ><i class='ion-close-round'></i></button></div>";
        }
        else{
            self = '';
        }
        $('#chat-ul').append( append_str + text+ "<span class='span-date'>"+created_at+"</span>" + self +"<i class='ion-ios-more' data-permalink='"+permalink+"'></i>"+'</li>');

    }

    function insertChat(msg){
        self = 0;
        if($("#user_id").val() == msg.data.user_id){
            self = 1;
        }
        insertText(msg.data.comment, msg.data.created_at, msg.data.user_id, self, msg.data.chat_id, msg.data.permalink);
    }

    function updateChat(msg){
        data = msg.data;
        $li_list = $("#chat-ul li");
        $li_list.each(function(index){
            if($(this).find("span").data("chat-id") == data.chat_id){
                $(this).find("span.comment").text(data.comment);
            }
        });

    }

    function deleteChat(msg){
        data = msg.data;
        $li_list = $("#chat-ul li");
        $li_list.each(function(index){
            if($(this).find("span").data("chat-id") == data.chat_id){
                $(this).remove();
            }
        });

    }

    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });


    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
    $('form#join').submit(function(event) {
        $("#room").val($('#join_room').val());
        socket.emit('join', {room: $('#join_room').val()});
        $("#chat-ul li").remove();
        return false;
    });
    $('form#leave').submit(function(event) {
        socket.emit('leave', {room: $('#leave_room').val()});
        return false;
    });
    $('form#send_room').submit(function(event) {
        if($('#room_data').val() == ""){

        }
        else{
            socket.emit('chat insert', {room: $('#room').val(), data: $('#room_data').val()});
        }

        return false;
    });
    $('form#close').submit(function(event) {
        socket.emit('close room', {room: $('#close_room').val()});
        return false;
    });
    $('form#disconnect').submit(function(event) {
        socket.emit('disconnect request');
        return false;
    });

    /*메시지 갱신*/
    $(document).on("click", ".btn_update", function(){
        $(".send-form-wrapper").css("display", "none");
        $(".update-form-wrapper").css("display", "block");
        $span = $(this).parents("li.text-right").find("span.comment");
        var text = $span.text();
        var chat_id = $span.data("chat-id");

        $("#update_message").val(text);
        $("input[name='chat_id']").val(chat_id);
    });

    $('form#update').submit(function(event) {
        socket.emit('chat update', {room: $('#room').val(), data: $("#update input[name='chat_id']").val()+"!@!"+$("#update_message").val() });
        $(".update-form-wrapper").css("display", "none");
        $(".send-form-wrapper").css("display", "block");
        return false;
    });

    /*메시지 삭제*/
    $(document).on("click", ".btn_delete", function(){
        $span = $(this).parents("li.text-right").find("span.comment");
        var chat_id = $span.data("chat-id");

        var position = $(this).offset();
        $(".delete-form-wrapper").css("display", "block");
        $(".delete-form-wrapper").css("top", position.top-35);
        $(".delete-form-wrapper").css("left", position.left);
        $("input[name='chat_id']").val(chat_id);
    });

    $('form#delete').submit(function(event) {
        socket.emit('chat delete', {room: $('#room').val(), data: $("#delete input[name='chat_id']").val() });
        $(".delete-form-wrapper").css("display", "none");
        return false;
    });

    $("#delete .close").on("click", function(){
        $(".delete-form-wrapper").css("display", "none");
    });

    $('#room_data').on('keyup', function(e) {
        if (e.which == 13 && ! e.shiftKey && $('#room_data').val() != '') {
            if($('#room_data').val().replace(/ /g, '').replace(/\r/g, "").replace(/\n/g, "") != '' && $('#room_data').val().replace(/ /g, '').replace(/\n/g, "").replace(/\r/g, "") != ' '){
                console.log("!");
                $('#send_room button').submit();
                $(this).val('');
            }
        }
    });

    $('#channel-list .channel').on('click', function(){
        var channel_title = $(this).data('channel');
        $("#join_room").val(channel_title);
        $('#channel-list .channel i').css("display", "none");
        $(this).find("i").css("display", "inline");
        $('form#join').submit();
    });

    /*퍼머링크*/
    $(document).on("click", "i.ion-ios-more", function(){
        $parmalink = $(this).data("permalink");
        alert("http://127.0.0.1:5000/link/"+$parmalink);
    });
});