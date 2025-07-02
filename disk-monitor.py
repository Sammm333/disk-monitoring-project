import psutil
import logging
import time

logging.basicConfig(
    filename='disk_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_disk_space(path='/'):
    try:
        disk = psutil.disk_usage(path)
        free_percent = (disk.free / disk.total) * 100
        
        message = f"Свободно: {free_percent:.2f}% ({disk.free / (1024**3):.2f} GB из {disk.total / (1024**3):.2f} GB)"
        logging.info(message)
        print(message)
        
        if free_percent < 20:
            warning = f"ВНИМАНИЕ: Мало места на диске! Свободно только {free_percent:.2f}%"
            logging.warning(warning)
            print(warning)
            
    except Exception as e:
        error_message = f"Ошибка при проверке диска: {str(e)}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    while True:
        check_disk_space()
        time.sleep(60)  # ждем 60 секунд перед следующей проверкой

