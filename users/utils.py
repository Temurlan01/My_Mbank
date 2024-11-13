import requests
from django.conf import settings


def get_usd_to_kgs_rate():
    api_key = settings.FREE_FOREX_API_KEY  # Получаем API ключ из настроек
    url = f"https://www.freeforexapi.com/api/live?pairs=USDKGS&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP ошибки

        # Разбираем ответ в формате JSON
        data = response.json()

        # Проверка наличия нужных данных в ответе
        if "rates" in data and "USDKGS" in data["rates"]:
            rate = data["rates"]["USDKGS"]["rate"]  # Получаем курс обмена
            return rate
        else:
            print("Ошибка: Неверный формат данных от API.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка при обработке данных: {e}")
        return None