import mysql.connector as connection
import pandas as pd
import warnings
import config

warnings.filterwarnings('ignore')

db_name = 'flights'


def get_airports(latitude_min, longitude_min, latitude_max, longitude_max):
    """ Возвращает DataFrame аэропортов между указанными координатами """
    try:
        db = connection.connect(host=config.host, database=db_name, user=config.user, passwd=config.password, use_pure=True)
        query = f"SELECT * FROM airports WHERE "\
                f"latitude BETWEEN {latitude_min} AND {latitude_max} AND "\
                f"longitude BETWEEN {longitude_min} AND {longitude_max};"
        res = pd.read_sql(query, con=db)
        db.close()
        return res[['airport', 'city', 'country', 'latitude', 'longitude']]
    except Exception as e:
        print(str(e))


def get_routes(firsth_city, second_city):
    """ Возравщает DataFrame c маршрутами запрашиваемых городов """
    try:
        db = connection.connect(host=config.host, database=db_name, user=config.user, passwd=config.password, use_pure=True)
        query = f"SELECT * FROM routes WHERE "\
                f"src_airport_id IN (SELECT id FROM airports WHERE city = '{firsth_city}') AND "\
                f"dst_airport_id IN (SELECT id FROM airports WHERE city = '{second_city}');"
        res = pd.read_sql(query, con=db)
        db.close()
        return res[['src_airport', 'dst_airport', 'airplane']]
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # get_db(0, 1, 0, 10)
    # get_routes('Beloyarsky', 'Moscow')
    get_routes('New York', 'Boston')
