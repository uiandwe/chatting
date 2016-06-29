#로그인
def signin(dc, email, password):
    if email is '' or password is '':
        return_json = {'status': "success", 'data': "error", 'message': "칸을 모두 넣어주세요"}
        return return_json


    sql = "select count(user_id) as cnt from user where password = '"+password+"' and email = '"+email+"'"
    cur = dc.find(sql)
    for response in cur:
        if int(response[0]) <= 0:
            return_json = {'status': "success", 'data': "", 'message': "email나 아이디이 비번이 잘못 입력되었습니다."}
            return return_json

        else:
            sql = "select user_id from user where password = '"+password+"' and email = '"+email+"'"
            cur = dc.find(sql)
            for user_id in cur:
                if int(user_id[0]) > 0:
                    return int(user_id[0])

