import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def generate_chrome_options():
    chrome_options = Options()

    # Удаляем "--headless", чтобы окно браузера отображалось
    # chrome_options.add_argument("--headless")  # Эту строку убираем

    # Маскировка под обычного пользователя через user-agent
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Отключение режима автоматизации
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Отключение всплывающих окон "Chrome is being controlled by automated test software"
    chrome_options.add_argument("--disable-infobars")

    # Отключение всплывающих окон и уведомлений
    chrome_options.add_argument("--disable-notifications")

    # Отключение проверки SSL сертификатов
    chrome_options.add_argument("--ignore-certificate-errors")

    # Открытие браузера в максимальном режиме (опционально)
    chrome_options.add_argument("--start-maximized")

    return chrome_options


# Пример использования
if __name__ == "__main__":
    path_to_driver = r'C:\Users\Bafer\PycharmProjects\chromedriver-win64\chromedriver.exe'
    chrome_options = generate_chrome_options()

    headers = {
        ":authority": "www.tbank.ru",
        ":method": "GET",
        ":path": "/mybank/",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "__P__wuid=7a62d461bfb33db31cefd093285c3dcf; _t_modern=true; stDeIdU=7a62d461bfb33db31cefd093285c3dcf; userType=Visitor; dco.id=; mediaInfo={%22width%22:1920%2C%22height%22:945%2C%22isTouch%22:false%2C%22displayMode%22:%22browser%22%2C%22retina%22:false}; vIdUid=fc197b5f-1f3f-4d20-9da2-75ed004692f0; stSeStTi=1726217878677; twt_ccs_d=done-1; dsp_click_id=no%20dsp_click_id; pageLanding=https%3A%2F%2Fwww.tbank.ru%2Fauth%2Flogin%2F; __P__wuid_visit_id=v1%3A0000001%3A1726217878684%3A7a62d461bfb33db31cefd093285c3dcf; __P__wuid_visit_persistence=1726217878684; api_session_csrf_token_af195f=65178801-209c-4627-83f2-28b9ab81ee77.1726217877; api_session=oHmbjxkwJJSWKx19QawXf40N12kCMq25.ix-prod-api61; __P__wuid_last_update_time=1726217878684; _ym_uid=1726217879733135110; _ym_d=1726217879; _ym_isad=2; api_session_csrf_token_783562=be0828f5-1815-4453-8e17-6d0517e18a8f.1726217877; api_sso_id=9d618ffadf47e332278872b7c5071238; sso_used=true; junior_flg=false; isIBAuthorized=true; sso_api_session=t.kp518cqAdzV6eQuPZjpYvhs9cIW93sv6bnhzLQk7PijUvBaBEcs7lOm8P_gdVUA980ga0mqQaD6NDw2xCkKwoQ; psid=oHmbjxkwJJSWKx19QawXf40N12kCMq25.ix-prod-api61; pcId=76363742; stLaEvTi=1726218208692",  # Ваши куки
        "referer": "https://www.tbank.ru/auth/?state=78356224-...",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Создаем экземпляр веб-драйвера с использованием selenium-wire
    driver = webdriver.Chrome(service=Service(path_to_driver), options=chrome_options)
    driver2 = webdriver.Chrome(service=Service(path_to_driver), options=chrome_options)

    # Передача заголовков перед выполнением запроса
    driver.request_interceptor = lambda request: request.headers.update(headers)

    # Переход на нужную страницу
    url = "https://www.tbank.ru/mybank/"
    driver.get(url)
    driver2.get("https://github.com/Alouettesu/Phone")
    # Оставляем окно браузера открытым для проверки
    input("Нажмите Enter, чтобы закрыть браузер...")

    # Закрываем браузер после завершения
    driver.quit()

    # Окно браузера останется открытым, пока не закроете его вручную
