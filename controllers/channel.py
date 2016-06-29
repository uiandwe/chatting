__author__ = 'hyeonsj'


def get_channel_all(dc):
    sql = "SELECT channel_title FROM channel;"
    cur = dc.find(sql)
    return_list = []
    for response in cur:
       return_list.append(response[0])

    return return_list