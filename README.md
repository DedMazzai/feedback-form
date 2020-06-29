# feedback-form

Тест заполнения формы обратной связи на валидных данных.

Для запуска тестов на Ubuntu в браузере Chrome необходимо:
- установить Python версии 3.6... и выше
- установить пакеты из requirements.txt
- скачать драйвер для Chrome https://sites.google.com/a/chromium.org/chromedriver/downloads и распаковать.
- Переместить разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```bash
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
Запускать командой pytest из директории проекта.