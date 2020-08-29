# language-cheker
### Задание: запуск автотестов для разных языков интерфейса

##### Как проверить задание (взято со траницы описания задания):
1. Тест в репозитории можно запустить командой `pytest --language=es`, тест успешно проходит.
2. Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду **time.sleep(30)** сразу после открытия ссылки. Запустите тест с параметром **--language=fr** и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: **"Ajouter au panier"**.
3. Браузер должен объявляться в фикстуре **browser** и передаваться в тест как параметр.
4. В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. Есть **assert**.
5. Название тестового метода внутри файла test_items.py соответствует задаче. Название test_something не удовлетворяет требованиям.
