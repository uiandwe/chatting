import time


#채널 생성
def join(room_title, dc, join_room, rooms, user_id):
    join_room(room_title)
    sql = "select count(*) as cnt from channel where channel_title = '"+room_title+"'"
    cur = dc.find(sql)
    for response in cur:
        if int(response[0]) <= 0:
            sql = "insert into channel(channel_title) values('"+room_title+"');"
            cur = dc.insert(sql)

        #channel_id find
        sql = "select channel_id from channel where channel_title = '"+room_title+"'"
        cur = dc.find(sql)
        channel_id = 0
        for channel in cur:
            channel_id = int(channel[0])

        #channel_active_user 테이블에 user_id 저장
        sql = "select count(*) as cnt from channel_active_user " \
              "where channel_id = "+str(channel_id)+" and user_id = "+str(user_id)+""
        cur = dc.find(sql)
        for channel_active_user in cur:
            if int(channel_active_user[0]) <= 0:
                sql = "insert into channel_active_user(user_id, channel_id, created_at) " \
                      "values("+str(user_id)+", "+str(channel_id)+", "+str(time.time())+")"
                cur = dc.insert(sql)

    return rooms()
