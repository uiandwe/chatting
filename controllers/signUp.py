import hashlib


#회원가입
def signup(dc, username, email, password):
    if username is '' or email is '' or password is '':
        return_json = {'status': "success", 'data': "error", 'message': "칸을 모두 넣어주세요"}
        return return_json

    if len(username) > 45:
        return_json = {'status': "success", 'data': "error", 'message': "유저의 이름길이를 초과하였습니다."}
        return return_json

    if len(email) > 100:
        return_json = {'status': "success", 'data': "error", 'message': "email의 최대 길이를 초과하였습니다."}
        return return_json

    if len(password) > 45:
        return_json = {'status': "success", 'data': "error", 'message': "패스워드의 최대 길이를 초과하였습니다."}
        return return_json


    sql = "select count(user_id) as cnt from user where username = '"+username+"' or email = '"+email+"'"
    cur = dc.find(sql)
    for response in cur:
        if int(response[0]) <= 0:
            h = hashlib.sha1()
            h.update(str(password).encode('utf-8'))
            password = h.hexdigest()

            sql = "insert into user(username, email, password) values('"+username+"', '"+email+"', '"+password+"');"
            cur = dc.insert(sql)

            sql = "select user_id from user where username = '"+username+"' and email = '"+email+"'"
            cur = dc.find(sql)
            for user_id in cur:
                if int(user_id[0]) > 0:
                    return int(user_id[0])
        else:
            return_json = {'status': "success", 'data': "", 'message': "이미 있는 아이디 입니다."}
            return return_json

