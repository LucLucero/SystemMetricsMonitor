import psutil
import time
import psycopg2
from psycopg2 import sql

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def get_disk_free():
    disk_info = psutil.disk_usage('/')
    return disk_info.free / disk_info.total * 100

def save_metrics_to_db(cpu_usage, memory_usage, disk_usage, disk_free):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="luciano",
            host="localhost",
            port="5432",
            database="monitor"
        )
        cursor = connection.cursor()
        
        insert_query = sql.SQL(
            "INSERT INTO system_metrics (cpu_usage, memory_usage, disk_usage, disk_free) VALUES (%s, %s, %s, %s)"
        )
        
        cursor.execute(insert_query, (cpu_usage, memory_usage, disk_usage, disk_free))
        connection.commit()
    except Exception as error:
        print(f"Erro ao inserir dados: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def main():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        disk_free = get_disk_free()
        
        save_metrics_to_db(cpu_usage, memory_usage, disk_usage, disk_free)
        
        time.sleep(5)

if __name__ == "__main__":
    main()
