function showHelpers(id) {
    var output = document.getElementById("output");
    if (id === 1) {
        output.innerHTML = "Для подключения библиотек используй команды:\nimport название_библиотеки\n from имя_библиотеки import имя_файла.\nКаждая команда должна начинаться с новой строки.";
    }
    if (id === 2) {
        output.innerHTML = "Если ты получаешь непонятные ошибки, то проверь, что нигде не поставил лишних отступов перед каждой строчкой кода (это важно!).";
    }
    if (id === 3) {
        output.innerHTML = "Что ж, если совсем ничего не получается, то я поделюсь с тобой рабочим кодом:\nimport keras\nfrom keras.datasets import cifar10\nfrom keras.models import Sequential\nfrom keras.layers import Dense, Flatten\nfrom keras.optimizers import Adam\nТолько тсссс, это по секрету, никому не показывай";
    }
    if (id === 4) {
        output.innerHTML = "Для загрузки данных из CIFAR-10 используй команду:\n(переменная_1_набора, перменная_названия_1_набора), (переменная_2_набора, переменная_названия_2_набора) = имя_файла.load_data()";
    }
    if (id === 5) {
        output.innerHTML = "Здесь имя_файла - cifar10. Проверь, что нигде нет лишних отступов, таких как пробел или enter. Пиши всю команду в одну строку";
    }
    if (id === 6) {
        output.innerHTML = "Что ж, если и тут ничего не выходит, то я открою тебе ещё один секрет: ответ на задание - это:\n(nabor_1, nazvanie_1), (nabor_2, nazvanie_2) = cifar10.load_data()";
    }
    if (id === 7) {
        output.innerHTML = "Хе-хе, а самому подумать?";
    }
    if (id === 8) {
        output.innerHTML = "Ладно, чтобы тренировать нейросеть, используй команду (перепиши на язык Питон):\nнейросеть.тренируйся(набор_1, названия_1, batch_size=32, epochs=число_просмотров_картинок, validation_data=(набор_2, названия_2))";
    }
    if (id === 9) {
        output.innerHTML = "Чтобы попросить нейросеть предсказать картинку, используй команду:\nprediction = model.predict(my_image)";
    }
    if (id === 10) {
        output.innerHTML = "Что ж, мой друг, держи ответ. В первое окно напиши команду:\nmodel.fit(nabor_1, nazvanie_1, batch_size=32, epochs=5, validation_data=(nabor_2, nazvanie_2))\nВо второе окно напиши:\nprediction = model.predict(my_image)";
    }
}
