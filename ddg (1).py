import sys
import csv
from asyncio import sleep
import time
import json


nameplayer = ''
gender = ''
age = ''
data = {
    "nameplayer": nameplayer,
    "gender":gender,
    "age":age
       }

def savejson():
    with open('myjson.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def out_Black(text):
    print("\033[30m {}" .format(text))
def out_red(text):
    print("\033[31m {}" .format(text))
def out_Green(text):
    print("\033[32m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
def out_Purple(text):
    print("\033[35m {}" .format(text))
def out_Turquoise(text):
    print("\033[36m {}" .format(text))
def out_white(text):
    print("\033[37m {}" .format(text))
ploho = ["Вы навсегда остаетесь без шанса на спасение. Вам все равно на происходящее, и вы отстраняетесь от свой судьбы в своих фантазиях.", 
           "Вы теряете самообладание и в следствии рассудок.\nВы начинаете проклинать все сущное и свое существование.\nВы не находите лучшего выхода как упасть вниз.\nВ процессе падения вы ломаете все кости и умираете в муках.",
           "Вы бессмысленно продолжаете плутать по абсолютной пустоши. Вы ничего не изменили, а лишь потеряли.\n Ваши опасения были верны, и вы навсегда застряли нигде.\nВы не чувствуете боли, но ваша рана на руке становится все хуже и вы умираете от потери крови.",
           "Вы погружаетесь в вечный и приятный сон. В нем есть все, о чем вы мечтали.\nЭтот сон никогда не закончится, но и вы никогда не сможете узнать правду.",
           "В трансе вы понимаете, что, чтобы выбраться из ничего, вам необходимо освободится от физической сущности и отбросить ваше прошлое, имя, возраст и прочие фантазии, что сковывали вас здесь.\nОсвободившись, вы обретаете небывалую свободу и возвращаетесь в реальный мир.\nТам вы просыпаетесь и понимаете, что проспали несколько месяцев и это все был просто дурной сон.",
           "Ваш разум оказался слишком слаб для такой задачи. Поэтому вы погружаетесь в вечный и приятный сон. В нем есть все, о чем вы мечтали.\nЭтот сон никогда не закончится, но и вы никогда не сможете узнать правду.",
           "Ваш разум оказался слишком слаб для такой задачи. Он не справляется с задачей, и вы сходите с ума, теряя рассудок.",
           "Вы бессмысленно продолжаете плутать по абсолютной пустоши. Вы ничего не изменили, а лишь потеряли.\nВаши опасения были верны, и вы навсегда застряли нигде. "
           ]
gender_dict = {0: 'муж',
               1: 'жен'}
title = "Новелла"
out_red(f"Название игры: {title}\n")
out_yellow("Внимание! Прочтите перед началом игры.\nЕсли вы выберете действие, которого не будет в перечне, то игра просто закроется, и все придется делать с самого начала\n")
def Description():
    out_white("Вы навсегда остаетесь без шанса на спасение. Вам все равно на происходящее, и вы отстраняетесь от свой судьбы в своих фантазиях.")
    out_white("Вы теряете самообладание и в следствии рассудок.\nВы начинаете проклинать все сущное и свое существование.\nВы не находите лучшего выхода как упасть вниз.\nВ процессе падения вы ломаете все кости и умираете в муках.")
    out_white("Вы бессмысленно продолжаете плутать по абсолютной пустоши. Вы ничего не изменили, а лишь потеряли.\n Ваши опасения были верны, и вы навсегда застряли нигде.\nВы не чувствуете боли, но ваша рана на руке становится все хуже и вы умираете от потери крови.")
    out_white("Вы погружаетесь в вечный и приятный сон. В нем есть все, о чем вы мечтали.\nЭтот сон никогда не закончится, но и вы никогда не сможете узнать правду.")
    out_white("В трансе вы понимаете, что, чтобы выбраться из ничего, вам необходимо освободится от физической сущности и отбросить ваше прошлое, имя, возраст и прочие фантазии, что сковывали вас здесь.\nОсвободившись, вы обретаете небывалую свободу и возвращаетесь в реальный мир.\nТам вы просыпаетесь и понимаете, что проспали несколько месяцев и это все был просто дурной сон.")
    out_white("Ваш разум оказался слишком слаб для такой задачи. Поэтому вы погружаетесь в вечный и приятный сон. В нем есть все, о чем вы мечтали.\nЭтот сон никогда не закончится, но и вы никогда не сможете узнать правду.")
    out_white("Ваш разум оказался слишком слаб для такой задачи. Он не справляется с задачей, и вы сходите с ума, теряя рассудок.")
    out_white("Вы бессмысленно продолжаете плутать по абсолютной пустоши. Вы ничего не изменили, а лишь потеряли.\nВаши опасения были верны, и вы навсегда застряли нигде.")


out_Purple("Итак, меня зовут: ")
name = input()


out_red(f"Погна, {name}?")
data['nameplayer'] = name
out_white("Не знаю сколько точно, но все время, что себя помню, я здесь.")
out_white("Здесь нет ничего.\nНет ни звуков, ни других существ.")
out_white("Есть только я и эта лестница.")
out_white("У нее нет ни начала, ни конца.\nПо крайней мере, я еще не доходил до них.")
out_white("\n")

out_white("Я не помню сколько мне лет.")
while True:
    try:
        age = int(input("Допустим мне "))
        data['age'] = age
        break
    except ValueError:
        print("Так...")
        continue
out_red("выбор пола:")
out_white("0-муж, 1-жен")
gender_selected = int(input())

out_red(f"Отлично, {gender_dict[gender_selected]}?")

data['gender'] = gender_dict[gender_selected]
savejson()
out_white("Я могу двигаться лишь вверх и вниз.\nКуда мне пойти? ")
while True:
    try:
        answerPath = int (input("1. Вверх\n2. Вниз\n"))
        break
    except ValueError:
        out_red("Может еще подумать...")
        continue
if answerPath == 1:
    out_red("Пойду наверх.")
elif answerPath == 2:
    out_red("Пойду вниз.")
else:
    out_red("Используйте только те команды, которые есть в списке действий. ")
    exit()
print("\n")

print("Из-за постоянного движения я неосознанно задумываюсь.")
print("Я стараюсь отвлечься от всего и представить что-нибудь.")
print("Допустим, сейчас я ...")
while True:
    try:
        answer = int (input("1. Представлю, как я выберусь отсюда и что буду делать.\n2. Представлю, как за мной кто-нибудь придет и спасет меня.\n3. Останусь тут навсегда.\n"))
        break
    except ValueError:
        print("Вcе же надо о чем-то подумать.")
        continue
if answer == 1:
    print("*Надеюсь на лучшее и продолжаю путь*")
elif answer == 2:
    print("*А может никто и не придет..?*")
elif answer == 3:
    print("*Отчаяние*")
else:
    print("Используйте только те команды, которые есть в списке действий. ")
    exit()
print("\n")

print("А что если я все таки заточен здесь навсегда?\nЗачем тогда это нужно?\nМожет забить на все и остановится?")
while True:
    try:
        answer = int (input("1. Нет, нелья так. Откину все плохие мысли\n2. ДА ЗАЧЕМ Я ЭТО ВСЕ ДЕЛАЮ???\n"))
        break
    except ValueError:
        print("Нужно принять решение.")
        continue
if answer == 1:

    print("Нужно успокоится и двигаться дальше. Всегда так было и всегда так будет. В любом случае куда-нибудь да приду.")
elif answer == 2:

    print("Все, довольно. Не могу так. Нужно сменить обстановку.")
    while True:
        try:
            answer = int (input("1. Пойду вверх.\n2. Пойду вниз.\n"))
            break
        except ValueError:
            print("Нужно принять решение.")
            continue
    if answerPath == 1 and answer == 1:
    
        print("Иду вверх!")
    elif answerPath == 1 and answer ==2 :
        
        print("Иду вниз!")
    elif answerPath == 2 and answer == 1:
     
        print("Иду вверх!")
    elif answerPath == 2 and answer == 2:
        
        print("Иду вниз!")
    else:
        print("Используйте только те команды, которые есть в списке действий. ")
        exit()
else:
    print("Используйте только те команды, которые есть в списке действий. ")
    exit()
print("\n")

print("Единственное воспоминание, которое у меня было - моя внешность.\nЗдесь нет зеркал и нет никаких отражающих поверхностей.")
print("Но даже его я потерял. Со временем оно настолько искозилось, что теперь даже кажеться нереальным.")
print("Иногда я думаю, что это лишь сон, и за границами этого сна другая жизнь.")
print("У меня там есть реальное имя, возраст, воспоминания, цели.\nВсе то, чего у меня нет здесь.")
print("...")
while True:
    try:
        answer = int (input("1. Надо продолжать свой путь.\n2. Закончить.\n"))
        break
    except ValueError:
        print("Нужно принять решение.")
        continue
if answer == 1:

    print("В конце еще меньше смысла, чем в прибывании здесь.\nЛишаться того, что есть хотя бы сейчас будет глупостью.")
    print("Буду продолжать свой путь.")
elif answer == 2:
    
    Description()
    print("Вы прошли на 2-ую плохую концовку.")
    exit()
else:
    print("Используйте только те команды, которые есть в списке действий. ")
    exit()
print("\n")

print("Время идет. Ничего не меняется.\nРастет лишь количество ступеней, которые я прошел.")
print("Вдруг я случайно очнулся от своих мыслей.")
print("Ступень, на которую я наступил не была \"обычной\"")
print("До этого я даже не обращал на это внимания, но эта ступень почему-то сильно бросилась мне в глаза.")
while True:
    try:
        answer = int (input("1. Подойти посмотреть.\n2. Проигнорировать\n"))
        break
    except ValueError:
        print("Нужно принять решение.")
        continue
if answer == 1:
 
    print("Подойду, посмотрю.")
    print("Когда я подошел ближе, то я заметил, что изменилась не только она, но и все окружение.")
    print("Все долгое время я находился в своих мыслях и никак не обращал внимания на происходящее вне своей головы.")
    print("Не могу даже представить чтобы было, если бы я так и не вышел из своих раздумий.")
    print("\n")

    print("Я подошел ближе и пригляделся.\nУ этой ступени была большая трещина.\nНо не достаточно большая, чтобы разгядеть, что скрывается за ней.") 
    def Description():
        print("Вы сваливаетесь в оставленную дыру и начинаете падать.")
        print("Вас полность поглащает темнота, и уже не остаеться и мелкого очертания лестницы, на которой вы пробыли вечность.")
        print("Некоторе время вы в панике падаете в неизвестную пропасть.\nНо через небольшой промежуток времени приземляетесь в никуда.")
        print("Вы нигде. Рядом с вами ничего нет. Ни свет, ни звук сюда не проникают.")
        print("Вы не получаете ни травм от падения, ни эмоций, которые вас так сильно охватывали несколько мнгновений назад.")
        print("Вы можете двигаться, но вы никогда не узнаете куда пошли.\nВы можете кричать, но ващи возгласы никем не будут услышаны.")
        print("Что же мне делать?")

    while True:
        try:
            chtocdelat = int (input("1. Расковырять рукой.\n2. Пнуть ногой.\n"))
            break
        except ValueError:
            print("Нужно принять решение.")
            continue
    if chtocdelat == 1:
        print("\n")
        print("Сквозь боль вы медленно расширяете трещину так, что теперь видите что находится ща лестницей.")
        print("Вы исцарапали ваши кисти и руки, почти ничего не осталось от ногтей.\nВсе руки в крови, но останавливаться уже поздно.")
        print("Вы пытаетесь взгянуть внутрь, но там настолько темно, что вы решаете полность разобрать остатки и пролесть туда сами.")
        print("\n")
        Description()
        answer = int (input("1. Начать свой новый путь.\n2. Войти в транс, ведь смысла идти больше нет\n"))
        if answer == 1:
            Description()
            print("Вы прошли на 3-ью плохую концовку.")
            exit()
        elif answer == 2:
            print("Вы попадаете в транс и пытаетесь решить все не физически, как делали ранее, а установить порядок хотя бы в своих мыслях.")
            while True:
                try:
                    koncovka = int (input("1. Смирится с судьбой и навечно заснуть.\n2. Продолжить искать выход в рамках своего разума.\n"))
                    break
                except ValueError:
                    print("Нужно принять решение.")
                    continue
            if koncovka == 1:
                Description()
                print("Вы прошли на хорошую концовку.")
                exit()
            elif koncovka == 2:
                Description()
                print("Вы прошли на плохую концовку.")
                exit()
            else:
                print("Используйте только те команды, которые есть в списке действий. ")
                exit()

    elif chtocdelat == 2:
        print("\n")
        print("Вы в тупую бьете ногами по трещине, и в итоге она сокрушается.")
        print("Вы пытаетесь взгянуть внутрь, но там настолько темно, что вы решаете полность разобрать остатки и пролесть туда сами.")
        print("\n")
        Description() 
        answer = int (input("1. Начать свой новый путь.\n2. Войти в транс, ведь смысла идти больше нет\n"))
        if answer == 1:
            print(ploho[7]) 
            print("Вы прошли на 5-ую плохую концовку.")
            exit()
        elif answer == 2:
            print("Вы попадаете в транс и пытаетесь решить все не физически, как делали ранее, а установить порядок хотя бы в своих мыслях.")
            while True:
                try:
                    koncovka = int (input("1. Смирится с судьбой и навечно заснуть.\n2. Продолжить искать выход в рамках своего разума.\n"))
                    break
                except ValueError:
                    print("Нужно принять решение.")
                    continue
            if koncovka == 1:
                print(ploho[3]) 
                print("Вы прошли на 1-ую среднюю концовку.")
                exit()
            elif koncovka == 2:
                print(ploho[6]) 
                print("Вы прошли на 4-ую плохую концовку.")
                exit()
            else:
                print("Используйте только те команды, которые есть в списке действий. ")
                exit()
        else:
            print("Используйте только те команды, которые есть в списке действий. ")
            exit()
    else:
        print("Используйте только те команды, которые есть в списке действий. ")
        exit()
elif answer == 2:
    
    print("Зачем она мне вообще нужна. Ступень как ступень")
    print(ploho[0])
    print("Вы прошли на 1-ую плохую концовку.")
    exit()
else:
    print("Используйте только те команды, которые есть в списке действий. ")
    exit()

