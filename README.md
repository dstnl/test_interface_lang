# test_interface_lang
Stepik course > 3.6.9

- `pytest test_items.py -v --browser_name=firefox --language=es`
- `pytest test_items.py -v --browser_name=firefox --language=fr`
- `pytest test_items.py -v --browser_name=chrome --language=es`
- `pytest test_items.py -v --browser_name=chrome --language=fr`

### Ваше решение будет проверяться по следующим критериям:

- Тест в репозитории можно запустить командой pytest `--language=es`, тест успешно проходит.
- Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду `time.sleep(30)` сразу после открытия ссылки. Запустите тест с параметром `--language=fr` и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
- Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
- В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. Есть assert.
- Название тестового метода внутри файла test_items.py соответствует задаче.
- Название test_something не удовлетворяет требованиям.