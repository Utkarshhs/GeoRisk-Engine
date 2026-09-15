import json
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

def connect_to_database():
    try:   
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASS"),
            database="georisk_db"

        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None


def insert_location(cursor, zone_name: str, latitude: float, longitude: float) -> int:
    try:
        query = "INSERT INTO locations (zone_name, latitude, longitude) VALUES (%s, %s, %s)"
        cursor.execute(query, (zone_name, latitude, longitude))
        return cursor.lastrowid
    except Error as e:
        print(f"Error while inserting location: {e}")
        return None

if __name__ == "__main__":
        connect = connect_to_database()
        connect = connect_to_database()
        if not connect:
            print("Pipeline aborted: Database offline.")
            exit()

        cursor = connect.cursor()
        with open("data/raw_sample.json", "r") as f:
            data= json.load(f)
            loc_id = insert_location(cursor, "bengaluru", data['latitude'], data['longitude'])
            hourly = data['hourly']
            times = hourly['time']
            temperatures = hourly['temperature_2m']
            precipitations = hourly['precipitation']
            wind_speeds = hourly['wind_speed_10m']

            query = """ 
            INSERT INTO environmental_metrics 
            (location_id, recorded_timestamp, temperature_c, precipitation_mm, wind_speed_kmh) 
            VALUES (%s, %s, %s, %s, %s)
        """
        for t, temp, precip, wind in zip(times, temperatures, precipitations, wind_speeds):
            cursor.execute(query, (loc_id, t, temp, precip, wind))

        connect.commit()
        cursor.close()
        connect.close()

        print(f"Successfully loaded weather data for Location ID {loc_id} into MySQL.")
        