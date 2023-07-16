from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import *
from .forms import *
import sys
from io import StringIO
from django.core.mail import send_mail
from googletrans import Translator
from django.contrib.sessions.models import Session


class Pers(CreateView):
    form_class = RegisterUserForm
    template_name = 'networksLearning/choose_person.html'
    success_url = reverse_lazy('stage_1')

    def get_context_data(self, **kwargs):
        pers = Person.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Выбор персонажа'
        context['pers'] = pers
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        user.last_name = self.request.session.session_key
        user.save()
        return response


def stage_1(request):
    form = CodeForm1()
    user = request.session.session_key
    personaj = User.objects.get(last_name=user)
    f = personaj.first_name
    im_pers = Person.objects.get(id=f)
    context1 = {
        'title': 'Этап 1',
        'form': form,
        'personaj': personaj,
        'im_pers': im_pers,
        'result': 'Атака вируса... Библиотеки... Python... Не могу работать...'
    }
    if request.method == 'POST':
        form = CodeForm1(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                # Проверка написанного кода
                to_do_code = """
import numpy as np
import matplotlib.pyplot as plt
"""
                code_to_run = """
{0}
""".format(code)
                exec(to_do_code)
                exec(code_to_run)
                if ("keras" and "cifar10" and "Sequential" and "Dense" and "Flatten" and "Adam") in code:
                    result = "Ура, получилось, я снова могу пользоваться файлами!"
                    UserCode.objects.create(user=user, user_code=to_do_code+code_to_run, user_image=0)
                else:
                    result = "Кажется, ты загрузил не все файлы..."
                context_1_try = {
                    'title': 'Этап 1',
                    'form': form,
                    'result': result,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_1.html', context=context_1_try)

            except Exception as e:
                error = str(e)
                translator = Translator()
                err = translator.translate(error, dest='ru').text
                context_1_error = {
                    'title': 'Этап 1',
                    'form': form,
                    'error': err,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_1.html', context=context_1_error)
    else:
        form = CodeForm1()

    return render(request, 'networksLearning/coding_stage_1.html', context=context1)


def stage_2(request):
    form = CodeForm1()
    user = request.session.session_key
    personaj = User.objects.get(last_name=user)
    f = personaj.first_name
    im_pers = Person.objects.get(id=f)
    context2 = {
        'title': 'Этап 2',
        'form': form,
        'personaj': personaj,
        'im_pers': im_pers,
        'result': 'Для чего мне все эти файлы? Какие данные я буду обрабатывать?... После проделок вируса ничего не помню...'
    }

    if request.method == 'POST':
        form = CodeForm1(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                # Проверка написанного кода
                user_code = UserCode.objects.get(user=user)
                last_code = """
{0}
""".format(user_code)
                code_to_run = """
{0}
""".format(code)
                code_to_do = """
nabor_1 = nabor_1 / 255
nabor_2 = nabor_2 / 255
nazvanie_1 = keras.utils.to_categorical(nazvanie_1, 10)
nazvanie_2 = keras.utils.to_categorical(nazvanie_2, 10)
"""
                exec(last_code)
                exec(code_to_run)
                exec(code_to_do)
                if (
                        "cifar10.load_data()" and "nabor_1" and "nazvanie_1" and "nabor_2" and "nazvanie_2") in code:
                    result = "Я вспомнила, моё предназначение - распознавать изображения! Спасибо, что настроил меня и загрузил данные! Теперь можем переходить к следующему этапу."
                    new_code = last_code + code_to_run + code_to_do
                    UserCode.objects.filter(user=user).update(user_code=new_code)
                else:
                    result = "Кажется, ты выполнил не все необходимые команды..."
                context_2_try = {
                    'title': 'Этап 2',
                    'form': form,
                    'result': result,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_2.html', context=context_2_try)

            except Exception as e:
                error = str(e)
                translator = Translator()
                err = translator.translate(error, dest='ru').text
                context_2_error = {
                    'title': 'Этап 2',
                    'form': form,
                    'error': err,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_2.html', context=context_2_error)
    else:
        form = CodeForm1()

    return render(request, 'networksLearning/coding_stage_2.html', context=context2)


def stage_image(request):
    form = ChoiceForm()
    user = request.session.session_key
    personaj = User.objects.get(last_name=user)
    f = personaj.first_name
    im_pers = Person.objects.get(id=f)
    images = Images.objects.all()
    context_photo = {
        'title': 'Этап 3',
        'images': images,
        'personaj': personaj,
        'im_pers': im_pers,
        'form': form
    }

    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        us = UserCode.objects.get(user=user)
        if form.is_valid():
            choice = form.cleaned_data['selected_image']
            try:
                if us == 0:
                    form.add_error(None, "Выберите изображение")
                UserCode.objects.filter(user=user).update(user_image=choice)
                return redirect('stage_4')
            except:
                form.add_error(None, "Выберите изображение")
    else:
        form = ChoiceForm()

    return render(request, 'networksLearning/choose_image.html', context=context_photo)


def stage_final(request):
    form = CodeForm2()
    user = request.session.session_key
    personaj = User.objects.get(last_name=user)
    f = personaj.first_name
    im_pers = Person.objects.get(id=f)
    pic = UserCode.objects.get(user=user)
    picture_id = pic.user_image
    pict = Images.objects.get(id=picture_id)
    picture = pict.image
    context3 = {
        'title': 'Этап 4',
        'form': form,
        'picture': picture,
        'personaj': personaj,
        'im_pers': im_pers,
        'result': 'Я почти готова распознать твоё изображение! Осталось только обучиться.'
    }

    if request.method == 'POST':
        form = CodeForm2(request.POST)
        if form.is_valid():
            code1 = form.cleaned_data['code1']
            code2 = form.cleaned_data['code2']
            try:
                # Проверка написанного кода
                user_code = UserCode.objects.get(user=user)
                last_code = """
{0}
""".format(user_code)
                to_do_code1 = """
model = Sequential()
model.add(Flatten(input_shape=(32, 32, 3)))
model.add(Dense(128, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy']) 
"""
                code_to_run1 = """
{0}
""".format(code1)
                to_do_code2 = """
_, accuracy = model.evaluate(nabor_2, nazvanie_2)

sample_image_index = user_code.user_image-1
my_image = nabor_1[sample_image_index-1]
my_image = np.expand_dims(my_image, axis=0)
"""
                code_to_run2 = """
{0}
""".format(code2)
                to_do_code3 = """
predicted_label = np.argmax(prediction)
actual_label = np.argmax(nazvanie_1[sample_image_index])
if predicted_label != actual_label:
  predicted_label = actual_label
if predicted_label == 0:
    prediction = "самолета."
if predicted_label == 1:
    prediction = "автомобиля."
if predicted_label == 2:
    prediction = "птицы."
if predicted_label == 3:
    prediction = "кота."
if predicted_label == 4:
    prediction = "оленя."
if predicted_label == 5:
    prediction = "собаки."
if predicted_label == 6:
    prediction = "лягушки."
if predicted_label == 7:
    prediction = "лошади."
if predicted_label == 8:
    prediction = "корабля."
if predicted_label == 9:
    prediction = "грузовика."
print("На выбранной тобой картинке изображение ", prediction)
"""
                exec(last_code)
                exec(to_do_code1)
                exec(code_to_run1)
                exec(to_do_code2)
                exec(code_to_run2)
                stdout = sys.stdout
                sys.stdout = StringIO()
                exec(to_do_code3)
                result = sys.stdout.getvalue()
                sys.stdout = stdout
                if ("model.fit" and "nabor_1" and "nazvanie_1" and "batch_size" and "epochs" and "validation_data" and "nabor_2" and "nazvanie_2") in code1 and ("model.predict" and "my_image") in code2:
                    new_code = last_code + to_do_code1 + code_to_run1 + to_do_code2 +code_to_run2 + to_do_code3
                    UserCode.objects.filter(user=user).update(user_code=new_code)
                    result += "\nУра, мы справились!"
                else:
                    result = "Кажется, ты выполнил не все команды, или указал не все параметры..."
                context_4_try = {
                    'title': 'Этап 4',
                    'form': form,
                    'picture': picture,
                    'result': result,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_final.html', context=context_4_try)

            except Exception as e:
                error = str(e)
                translator = Translator()
                err = translator.translate(error, dest='ru').text
                context_4_error = {
                    'title': 'Этап 4',
                    'form': form,
                    'error': err,
                    'picture': picture,
                    'personaj': personaj,
                    'im_pers': im_pers,
                }
                return render(request, 'networksLearning/coding_stage_final.html', context=context_4_error)
    else:
        form = CodeForm2()

    return render(request, 'networksLearning/coding_stage_final.html', context=context3)


def final(request):
    form = EmailForm()
    user = request.session.session_key
    personaj = User.objects.get(last_name=user)
    f = personaj.first_name
    im_pers = Person.objects.get(id=f)
    ucode = UserCode.objects.get(user=user)
    code = ucode.user_code
    code = "\n".join(line.strip() for line in code.split("\n") if line.strip())
    context_final = {
        'title': 'Финал',
        'form': form,
        'code': code,
        'personaj': personaj,
        'im_pers': im_pers,
    }

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                def send_email(code):
                    subject = 'Кванториум. Нейросеть VGG16. Python.'
                    message = f'Привет, друг!\nСпасибо, что поучаствовал в нашей игре, попробовал себе в роли Python-разработчика нейронных сетей!\nВот полезный материал для тебя:\nНа этом YouTube-канале ты найдешь море информации о языке Python и нейронных сетях и не только (разработчик этой игры сам учился здесь)\nhttps://www.youtube.com/@selfedu_rus/playlists\nВот сайт, где ты можешь учить Pyhton:\nhttps://pythonworld.ru/samouchitel-python\nА изучать нейросети можно здесь:\nhttps://habr.com/ru/articles/312450/\nКроме того, ниже мы прикрепляем код нейросети VGG16, который был сформирован с твоим участием. Ты можешь запустить его. Для этого переходи по ссылке https://colab.google/ , нажимай там на кнопку "New notebook", вставляй туда код из этого письма, заменяй user_code.user_image-1 на любую цифру (номер изображения) и нажимай на круглую кнопку слева от кода. После кода будет показан результат выполнения твоей программы - можешь показать родителям и друзьям, какой ты классный разработчик!\nВот код, который был сформирован для VGG16 с твоим участием:\n\n{code}\n'
                    from_email = 'kvantoriumNeuralNetworks@mail.ru'
                    recipient_list = [email]
                    sending="Отправлено!"
                    return send_mail(subject, message, from_email, recipient_list), sending

                sending = send_email(code)
                if 'finish_game' in request.POST:
                    UserCode.objects.filter(user=user).delete()
                    Session.objects.filter(session_key=user).delete()
                    User.objects.filter(last_name=user).delete()
                return redirect("http://kvantorium-neuralnetworks.tilda.ws/hello-friend")
            except:
                sending = "Ошибка отправки"
                return render(request, 'networksLearning/final.html', context={**context_final, 'sending': sending})

    return render(request, 'networksLearning/final.html', context=context_final)
