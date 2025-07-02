import psutil
import logging
import datetime

# Настройка логирования
logging.basicConfig(
    filename='disk_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_disk_space(path='/'):
    try:
        # Получаем статистику по диску
        disk = psutil.disk_usage(path)
        free_percent = (disk.free / disk.total) * 100
        
        # Логируем текущее состояние
        message = f"Свободно: {free_percent:.2f}% ({disk.free / (1024**3):.2f} GB из {disk.total / (1024**3):.2f} GB)"
        logging.info(message)
        print(message)
        
        # Проверяем, если свободно менее 20%
        if free_percent < 20:
            warning = f"ВНИМАНИЕ: Мало места на диске! Свободно только {free_percent:.2f}%"
            logging.warning(warning)
            print(warning)
            
    except Exception as e:
        error_message = f"Ошибка при проверке диска: {str(e)}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    check_disk_space()
