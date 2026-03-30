# Weather CLI

Простой скрипт, который показывает текущую погоду в городе через OpenWeatherMap.

## Технологии
  - **Python 3.10**
  - **httpx 0.28.1:** Клиент.
  - **python-dotenv 1.2.2:** Для использования переменных окружения.

## Установка
1. **Клонируйте репозиторий**
```bash
git clone https://github.com/SergeyKurilko/lofty-weather.git
cd lofty-weather
```

2. **Создайте виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate      # Windows 
```

3. **Создайте файл .env и добавьте API-ключ**
Откройте файл .env в любом редакторе и вставьте туда ваш API-ключ:
```bash
OPEN_WEATHER_API_KEY=ваш_ключ_сюда
```
Получить бесплатный ключ можно на openweathermap.org.

4. **Установите зависимости**
```bash
pip install -r requirements.txt
```

## Запуск
```bash
python weather.py Moscow
```

### Примеры использования
```bash
python weather.py London
python weather.py Moscow
python weather.py Париж
```
