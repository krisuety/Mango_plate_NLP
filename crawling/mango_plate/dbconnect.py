import pymysql


def insertDB(dataDic):

    if '이름' in dataDic.keys():
        R_name = dataDic['이름']
    else:
        R_name = None

    if '주소' in dataDic.keys():
        addr = dataDic['주소']
        x = addr.split(' ')
        R_gu = x[1]
        R_dong = x[2]
    else:
        addr = None
        R_gu = None
        R_dong = None

    if '전화번호' in dataDic.keys():
        tel = dataDic['전화번호']
    else:
        tel = None

    if '음식종류' in dataDic.keys():
        kind = dataDic['음식종류']
    else:
        kind = None

    if '평점' in dataDic.keys():
        rating = dataDic['평점']
    else:
        rating = None

    if '영업시간' in dataDic.keys():
        open_time = dataDic['영업시간']
    else:
        open_time = None

    if '휴일' in dataDic.keys():
        holiday = dataDic['휴일']
    else:
        holiday = None

    if '리뷰' in dataDic.keys():
        review = dataDic['리뷰']
    else:
        review = None

    try:
        conn = pymysql.connect(host='127.0.0.1', user='',
                               password='', port=3306, db='', charset='utf8')
        with conn.cursor() as cursor:
            sql = 'INSERT INTO restaurants (R_name, R_gu, R_dong, addr, tel, kind, rating, open_time, holiday, review) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s)'
            cursor.execute(sql, (R_name, R_gu, R_dong, addr, tel,
                                 kind, rating, open_time, holiday, review))
            conn.commit()
    finally:
        conn.close()
