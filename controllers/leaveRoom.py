__author__ = 'hyeonsj'


#채널 나가기
def leave(dc, user_id, room_title):
    sql = "select channel_id from channel where channel_title = '"+room_title+"'"
    cur = dc.find(sql)
    channel_id = 0
    for channel in cur:
        channel_id = int(channel[0])

    sql = "delete from channel_active_user where user_id = "+str(user_id)+" and channel_id = "+str(channel_id)+""
    cur = dc.delete(sql)

    sql = "select count(*) as cnt from channel_active_user where channel_id = "+str(channel_id)
    cur = dc.find(sql)
    for channel_active_user in cur:
        if int(channel_active_user[0]) <= 0:
            sql = "delete from channel where channel_id = "+str(channel_id)+""
            cur = dc.delete(sql)