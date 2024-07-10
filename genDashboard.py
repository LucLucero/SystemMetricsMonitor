import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation


def fetch_data_from_db():
    try:
        connection = psycopg2.connect(
            user="",
            password="",
            host="",
            port="",
            database=""
        )
        query = "SELECT timestamp, cpu_usage, memory_usage, disk_usage, disk_free FROM system_metrics WHERE timestamp >= NOW() - INTERVAL '2 HOURS' ORDER BY timestamp DESC"
        data = pd.read_sql(query, connection)
        data = data.sort_values(by='timestamp')  # Ordenar os dados pelo timestamp
        return data
    except Exception as error:
        print(f"Erro ao buscar dados: {error}")
    finally:
        if connection:
            connection.close()


def update(frame):
    data = fetch_data_from_db()
    if data.empty:
        return

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(data['timestamp'], data['cpu_usage'], label='CPU Usage', color='k')
    ax1.set_xlabel('Time', fontsize=8)
    ax1.set_ylabel('CPU Usage (%)', fontsize=8)
    ax1.set_title('CPU Usage Over Time', fontsize=10)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))

    ax2.plot(data['timestamp'], data['memory_usage'], label='Memory Usage', color = 'b')
    ax2.set_xlabel('Time', fontsize=8)
    ax2.set_ylabel('Memory Usage (%)', fontsize=8)
    ax2.set_title('Memory Usage Over Time', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax2.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))

    ax3.plot(data['timestamp'], data['disk_usage'], label='Disk Usage', color = 'g')
    ax3.set_xlabel('Time', fontsize=8)
    ax3.set_ylabel('Disk Usage (%)', fontsize=8)
    ax3.set_title('Disk Usage Over Time', fontsize=10)    
    ax3.legend(loc='upper left', fontsize=10)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax3.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))

    ax4.plot(data['timestamp'], data['disk_free'], label='Disk Free', color = 'violet')
    ax4.set_xlabel('Time', fontsize=8)
    ax4.set_ylabel('Disk Free (%)', fontsize=8)
    ax4.set_title('Disk Free Over Time', fontsize=10)
    ax4.legend(loc='upper right', fontsize=10)
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax4.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))
    



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 6))

ani = FuncAnimation(fig, update, interval=5000)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.suptitle('System Metrics Over Time', fontsize=16)
plt.show()
