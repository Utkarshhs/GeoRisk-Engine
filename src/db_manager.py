import json
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:   
        connection = mysql.connector.connect(
            host="localhost",
            user="utkarsh",
            password="Utkarsh@123",
            database="georisk_db"

        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None


def insert_location(cursor, zone_name: str, latitude: float, longitude: float) -> int:
    try:
        query = "INSERT INTO locations (name, latitude, longitude) VALUES (%s, %s, %s)"
        cursor.execute(query, (zone_name, latitude, longitude))
        return cursor.lastrowid
    except Error as e:
        print(f"Error while inserting location: {e}")
        return None