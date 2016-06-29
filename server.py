#coding: utf-8
#!/usr/bin/env python
import time, datetime
from threading import Thread
from flask import Flask, render_template, session, request, jsonify, redirect
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms, disconnect
import db
from controllers import joinRoom, chat, signUp, signIn, leaveRoom, channel
dc = db.Connect()


async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)


# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


def background_thread():
    count = 0
    while True:
        time.sleep(10)
        count += 1


@app.route('/', methods=['GET'])
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()
    if request.method == 'GET':
        if 'user_id' not in session:
            return render_template('signin.html')

    channel_list = channel.get_channel_all(dc)
    return render_template('index.html', user_id=session['user_id'], channel_list=channel_list)


#로그인
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        return_value = signIn.signin(dc, email, password)

        if type(return_value) is dict:
            return jsonify(results=return_value)
        else:
            session['user_id'] = return_value
            return redirect("/", code=302)

    else:
        return render_template('signin.html')


#회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        return_value = signUp.signup(dc, username, email, password)

        if type(return_value) is dict:
            return jsonify(results=return_value)

        session['user_id'] = return_value
        return redirect("/", code=302)
    else:
        return render_template('signup.html')

#퍼머링크
@app.route('/link/<id>', methods=['GET'])
def permalink(id):

    chatting_list = chat.permalink(dc, id)
    return render_template('permalink.html', chatting_list=chatting_list, permalink=1)



@socketio.on('my broadcast event', namespace='/spoqa')
def channel_broadcast_message(message):
    session['receive_cunt'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)

#채널 생성 or 들어가기
@socketio.on('join', namespace='/spoqa')
def join(message):
    room_title = message['room']

    user_id = session['user_id']

    return_room = joinRoom.join(room_title, dc, join_room, rooms, user_id)

    session['receive_count'] = session.get('receive_count', 0) + 1
    #join room 메시지
    emit('response',
         {'data': 'In rooms: ' + ', '.join(return_room),
          'count': session['receive_count']})
    #room 기존 메시지
    before_chat_list = chat.get_chat(dc, room_title, user_id)

    emit('response',
         {'data': before_chat_list,
          'type': 'before_chat'})

#채널 나가기
@socketio.on('leave', namespace='/spoqa')
def leave(message):
    leave_room(message['room'])

    room_title = message['room']
    user_id = session['user_id']

    leaveRoom.leave(dc, user_id, room_title)
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})

#채팅 입력
@socketio.on('chat insert', namespace='/spoqa')
def send_room_message(message):

    user_id = session['user_id']
    room_title = message['room']
    session['receive_count'] = session.get('receive_count', 0) + 1
    chat_id, pk_permalink = chat.chat_text(dc, room_title, message['data'], user_id)

    emit('response',
         {'data': {'comment': message['data'],
                   'created_at': datetime.datetime.now().strftime('%H:%M:%S'),
                   'user_id': user_id, 'chat_id': chat_id, 'permalink': pk_permalink},
          'count': session['receive_count'],
          'type': 'insert'},
         room=room_title)

@socketio.on('chat update', namespace='/spoqa')
def update_room_message(message):
    user_id = session['user_id']
    comment = message['data']
    room_title = message['room']

    chat_id = comment.split("!@!")[0]
    comment = comment.split("!@!")[1]

    chat.update_text(dc, comment, chat_id, user_id)

    emit('response',
         {'data': {'comment': comment,
                   'created_at': datetime.datetime.now().strftime('%H:%M:%S'),
                   'user_id': user_id, 'chat_id': chat_id},
          'type': 'update'},
         room=room_title)


@socketio.on('chat delete', namespace='/spoqa')
def delete_room_message(message):
    user_id = session['user_id']
    chat_id = message['data']
    room_title = message['room']

    chat.delete_text(dc, chat_id, user_id)

    emit('response',
         {'data': {'comment': '',
                   'created_at': datetime.datetime.now().strftime('%H:%M:%S'),
                   'user_id': user_id, 'chat_id': chat_id},
          'type': 'delete'},
         room=room_title)


@socketio.on('disconnect request', namespace='/spoqa')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/spoqa')
def spoqa_connect():
    emit('response', {'data': 'Connected', 'count': 0})



@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)