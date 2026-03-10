import time
import random
from playwright.sync_api import sync_playwright, TimeoutError as PTimeoutError


def main():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
    )

    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
        locale="ru-RU",
    )

    page = context.new_page()

    page.goto(
        "https://spb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=54&region=2"
    )

    try:
        page.wait_for_selector("text=Показать ещё", state="visible", timeout=15000)
        print("Кнопка 'Показать ещё' появилась, начинаем цикл.")
    except PTimeoutError:
        print("Кнопка 'Показать ещё' не появилась, возможно результатов нет.")
        browser.close()
        playwright.stop()
        return

    while True:
        try:
            # Ждём и кликаем кнопку
            page.wait_for_selector("text=Показать ещё", state="visible", timeout=10000)
            page.locator("text=Показать ещё").click()
            print("Нажали кнопку 'Показать ещё'")
        except PTimeoutError:
            print("Кнопка 'Показать ещё' больше не появилась — выходим из цикла.")
            break

        delay = random.uniform(4, 6)
        print(f"Ждём {delay:.2f} секунд...")
        time.sleep(delay)

        cards_count = page.locator("article[data-name='CardComponent']").count()
        print(f"Текущее количество карточек: {cards_count}")

    print("Обход завершён.")

    input("Нажмите Enter для выхода...")

    browser.close()
    playwright.stop()


if __name__ == "__main__":
    main()