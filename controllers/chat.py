__author__ = 'hyeonsj'
import datetime,time
import hashlib


def chat_text(dc, room_title, text, user_id):

    sql = "select channel_id  from channel where channel_title = '"+room_title+"'"
    cur = dc.find(sql)
    for response in cur:
        #해당 방이 존재 한다면
        if int(response[0]) > 0:
            channel_id = response[0]

            sql = "insert into chatting(type, comment, channel_id, user_id, created_at) " \
                  "values('text', '"+text+"', "+str(channel_id)+", "+str(user_id)+", "+str(time.time())+"); "
            cur = dc.insert(sql)
            for chatting_id in cur:
                chat_id = chatting_id[0]
                if int(chat_id) > 0:

                    h = hashlib.sha1()
                    h.update(str(chat_id).encode('utf-8'))
                    pk_sha1 = h.hexdigest()
                    sql = "update chatting set permalink='"+pk_sha1+"' where chatting_id="+str(chat_id)+";"
                    cur = dc.update(sql)

                    return int(chat_id), pk_sha1
        else:
            pass


def get_chat(dc, room_title, user_id):
    sql = "select channel_id  from channel where channel_title = '"+room_title+"'"
    cur = dc.find(sql)
    for response in cur:
        #해당 방이 존재 한다면
        if int(response[0]) > 0:
            channel_id = response[0]

            sql = "select comment, user_id, type, created_at, chatting_id, permalink from chatting " \
                  "where channel_id = "+str(channel_id)+" "
            cur = dc.find(sql)
            return_list = []
            for comment in cur:
                user_check = 0
                if int(comment[1]) == int(user_id):
                    user_check = 1
                temp_comment_dict = {'comment': comment[0], 'user_id': comment[1], 'type': comment[2],
                                     'created_at':
                                         datetime.datetime.fromtimestamp(int(comment[3])).strftime('%H:%M:%S'),
                                     'self': user_check,
                                     'chat_id': comment[4],
                                     'permalink': comment[5]}
                return_list.append(temp_comment_dict)

            return return_list


def permalink(dc, id):
    #데이터 확인
    sql = "select chatting_id from chatting where permalink = '"+id+"'"
    cur = dc.find(sql)
    for response in cur:
        if int(response[0]) > 0:
            chatting_id = int(response[0])
            return_list = []
            sql = "select * from chatting where chatting_id <= "+str(chatting_id)+" order by chatting_id desc limit 5;"
            cur = dc.find(sql)
            for chatting in cur:

                temp_comment_dict = {'comment': chatting[1],
                                     'created_at':
                                         datetime.datetime.fromtimestamp(int(chatting[7])).strftime('%H:%M:%S'),
                                     }
                return_list.append(temp_comment_dict)
            return_list.reverse()
            sql = "select * from chatting where chatting_id > "+str(chatting_id)+" limit 5;"
            cur = dc.find(sql)
            for chatting in cur:
                temp_comment_dict = {'comment': chatting[1],
                                     'created_at':
                                         datetime.datetime.fromtimestamp(int(chatting[7])).strftime('%H:%M:%S'),
                                     }
                return_list.append(temp_comment_dict)

            return return_list

#채팅 수정
def update_text(dc, comment, chat_id, user_id):
    sql = "update chatting set comment='"+comment+"' where chatting_id="+str(chat_id)+" and user_id = "+str(user_id)+";"
    cur = dc.update(sql)


#채팅 삭제
def delete_text(dc, chat_id, user_id):
    sql = "delete from chatting  where chatting_id="+str(chat_id)+" and user_id = "+str(user_id)+";"
    cur = dc.update(sql)