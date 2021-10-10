import pymysql
import pandas as pd


csv_file = '../data/bohaiwan2020_data2.csv'
df = pd.read_csv(csv_file, index_col='time')


def gen_sql_tuples(time):
    data = df.loc[time]
    time_str = time.replace('/', '-')
    l = []
    for sensor, val in data.items():
        tuple_str = f'(\'{time_str}\', \'{sensor}\', {val})'
        l.append(tuple_str)
    return ','.join(l)


def write_db(time):

    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='12345678',
                           database='bishe',
                           cursorclass=pymysql.cursors.DictCursor)

    with conn:
        with conn.cursor() as cursor:
            sql = f'INSERT INTO `data_manage_record` (`time`, `sensor`, `val`) VALUES {gen_sql_tuples(time)}'
            cursor.execute(sql)

        conn.commit()


for time, _ in df.iterrows():
    print('deal time: {}'.format(time))
    write_db(time)
    print('data in {} write into db success'.format(time))
