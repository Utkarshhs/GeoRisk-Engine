CREATE DATABASE IF NOT EXISTS georisk_db;
USE georisk_db;

CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(64) NOT NULL,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL
);

CREATE TABLE IF NOT EXISTS environmental_metrics (
    record_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    recorded_timestamp DATETIME NOT NULL,
    temperature_c FLOAT NOT NULL,
    precipitation_mm FLOAT NOT NULL,
    wind_speed_kmh FLOAT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    INDEX idx_time_loc (location_id, recorded_timestamp)
);