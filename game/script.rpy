# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define mainСharacterr = Character('[mainPerson]', color="#c8ffc8", image="Main")
define MrPython = Character('Mr. Python', color="#008B8B")
define MrMayor = Character('Владимир Олегович', color="#6A5ACD")
define MrPiter = Character('Питер', color="#556B2F")
define DataMark = Character('Марк', color='#90EE90')
define Sofia = Character('София', color='#BA55D3')
define AreaInkognito = Character('Незнакомец', color='#A9A9A9')

#Персонажи
image hero = "characters/Main.png"
image mayor = "characters/mayor.png"
image piter = "characters/Piter.png"
image mark = "characters/Mark.png"
image markWithBook = "characters/MarkWithBook.png"
image inkognito = "characters/inkognito.png"
image NoName = "characters/NoName.png"
image NoName1 = "characters/NoName.png"
image WebSofia = "characters/Sofia.png"

#Комната персонажа
image perspectiveScreen = "room/perspectiveScreen.png"
image roomFrom = "room/roomFrom.png"
image notification = "room/notification.png"
image notificationFromMrPython = "room/MrPython.png"
image teleportation = "room/teleportation.png"

#Виртуальный мир
image gates = "virtualWorld/gates.jpg"
image city = "virtualWorld/city.jpg"
image mainBuilding = "virtualWorld/mainBuilding.jpg"
image work = "PiterTask/work.png"
image completeWork = "PiterTask/CompleteWork.png"
image office = "PiterTask/office.png"

#Секретная комната
image secretRoom = "SecretRoom/secret_room.png"
image PitersOffice = "PitersOffice/office.jpg"

#DataCity
image dataCity = "MarkTasks/dataCity.jpg"
image data = "MarkTasks/data.jpg"
image heat = "MarkTasks/heat.png"
image try = "MarkTasks/Try.png"
image result = "MarkTasks/result.png"

#Старый район
image oldArea = "oldArea/oldArea.jpg"

#Web район
image WebArea = "WebArea/WebCity.png"

$ greenCount = 0

# Игра начинается здесь:
label start:
    scene roomFrom
    $ mainPerson = renpy.input('Придумай имя для главного героя (мужской пол)').capitalize()
    if mainPerson == '':
        $ mainPerson = "Миша"
    with dissolve
    scene roomFrom
    with dissolve
    mainСharacterr "{cps=*2}М-да, опять я поздно ложусь... {w}Когда я уже выберу чем хочу
    заниматься. Скоро ведь уже конец срока подачи документов. Кто вообще даёт
    такой выбор людям, только что закончившим школу?! Вот бы кто-то дал мне
    хоть какой-нибудь знак…{/cps}"

    with dissolve
    scene notification
    with dissolve
    mainСharacterr "Хм, кто бы мог написать мне в 3 часа ночи?"

    with fade
    scene notificationFromMrPython
    with dissolve
    MrPython "Ты амбициозен? Любишь решать нестандартные задачи?
    Обожаешь интересный опыт? Тогда скорее переходи по ссылке и погружайся в
    незабываемый мир программирования."

    with dissolve
    scene teleportation
    with dissolve
    mainСharacterr "О, это же полностью про меня, мельком посмотрю после чего уже
    точно пойду спать."

    with dissolve
    jump virtualWord
    return


label virtualWord:
    with fade
    scene gates
    show hero at left
    with dissolve
    mainСharacterr "Что это за безобразие?! {w}Где это я?"
    show mayor at right
    with dissolve
    MrMayor "Привет, меня зовут Владимир Олегович. Приветствую тебя в кодовой долине."
    with dissolve
    menu:
        "Вау, что это? Объясни, пожалуйста, поподробнее.":
            with dissolve
            MrMayor "Кодовая долина это место, где ты можешь реализовать всё что
                    захочешь, начиная с маленьких и красивых WEB-приложений и заканчивая
                    искусственным интеллектом."
        "Я где-то слышал про это. Скорее всего именно тут я смогу выбрать свою  будущую профессию!":
            with dissolve
            MrMayor "Да, ты совершенно прав."
    MrMayor "А сейчас нам нужно быстрее идти, нас уже ждут."
    hide mayor
    hide hero
    with fade
    scene city
    "Зайдя в город [mainPerson] увидел необычайно красивый, но странный город. Всё  в
    нем говорило о том что этот город был написан каким-то разработчиком, где-то
    были участки, которые были закомментированы, а где-то здания, которые держались на костылях."
    with fade
    scene mainBuilding
    show piter
    show mayor at right
    with dissolve
    MrMayor "Знакомься это представители наших районов."
    with dissolve
    mainСharacterr "Всем привет! Меня зовут [mainPerson]."
    with dissolve
    MrMayor "Сейчас иди с Питером ему нужна помощь. Он из района под название
            GameDev и ему срочно нужно дописать свой проект. Я думаю по пути он тебе
            всё расскажет, а мне и остальным пора бежать."
    hide mayor
    with dissolve
    MrPiter "Привет! Как ты мог услышать я Питер. Я отвечаю за игровой GameDev
            район. {w}В общем проблема такая. Скоро у меня срок сдачи проекта, а мне ужас
            как не хватает рук чтобы доделать детскую площадку."
    with dissolve
    mainСharacterr " Я бы с удовольствие помог, но я не умею строить площадки, да я
                    и не настолько физически сильный, так что вынужден отказать."
    MrPiter "Хах. Строить?! {w=1}Таким уже очень давно никто не занимается, откуда ты
            вообще такой взялся, что у вас там строят. {w=1}У нас не строят, у нас пишут всё в
            этом городе, начиная от зданий, заканчивая продуктами. Ты надеюсь слышал
            хотя бы когда-нибудь о Python?"
    menu:
        "Ну что-то слышал. Это какой-то один из множества языков программирования":
            jump ifDontKnow
        "Да, это один из самых популярных языков программирования, который может
        справляться совершенно с различными заданиями.":
            jump ifKnow
    return


label ifDontKnow:
    with dissolve
    MrPiter "Это не просто один из множества языков. Вот посмотри туда.{w=1}
     Видишь как это величественно и красиво? А это написал один из лучших
     работников города на этом твоём одном из множества языков."
    with dissolve
    mainСharacterr "Вау, и вправду красиво. Но я ничего не знаю об этом Python."
    with dissolve
    MrPiter "Не пережевай. Не смотря на то, что можно создавать вот такие
        шедевры, сам язык довольно прост."
    mainСharacterr "Хорошо, только научи меня пожалуйста."
    MrPiter "Конечно научу!"
    jump helpPiter
    return


label ifKnow:
    with dissolve
    MrPiter "О, а ты молодец, что интересуешься этим, тогда ты с легкостью справишься с моим заданием."
    with dissolve
    mainСharacterr "Хорошо, я готов тебе помочь!"
    jump helpPiter
    return


label helpPiter:
    with dissolve
    mainСharacterr "А как выбраться отсюда?"
    with dissolve
    MrPiter "Что? {w=1}Откуда отсюда?"
    with dissolve
    mainСharacterr "Да я просто пошутил. Ну так с чего начнём?"
    hide hero
    hide piter

    with fade
    scene work
    with dissolve
    show piter at right
    MrPiter "Давай попробуй, напиши свой код!"

    with fade
    scene time
    "какое-то время спустя..."
    scene completeWork
    with dissolve
    show piter at right
    MrPiter "Вау! У тебя отлично получилось. А это ведь ты всеголишь первый проект,
            тебя ждёт отличное будущее в нашем мире.{w=1} Пошли в главный офис нашего
            района, нужно отчитаться о проделанной работе."
    scene office
    show piter at right
    MrPiter "Ну вот и пришли, тут ты будешь работать если выберешь жить в нашем районе."
    mainСharacterr "А что это за кабинет куда вход строго запрещён?"
    MrPiter "Эм, это не важно пошли скорее дальше."
    menu:
        "Пойти дальше с Питером":
            jump stayWithPiter
        "Попробовать отстать от Питера и посмотреть, что находится в серкетной комнате.":
            jump checkSecretRoom
    return

label checkSecretRoom:
    $ greenCount = 1
    mainСharacterr " Ой, а можно я поговорю с другими сотрудниками, чтобы лучше узнать потенциальное место работы?"
    MrPiter "Да, конечно. Могу рассказать про все отделы."
    mainСharacterr"А можно ли без тебя? Просто боюсь, что работники могут сказать не то, что
    хотят при виде начальника."
    MrPiter "Хах, да, хорошо. Тогда жду у себя в кабинете."
    with fade
    scene secretRoom
    mainСharacterr "Так нужно быстро осмотреть комнату. Может тут будут какие-то подсказки как выбраться отсюда."
    MrPython "Что будем делать с нашим заключённым? Я считаю, что его нужно убарть ведь он единственный знает, что из нашего мира есть выход. Что думаешь ты?"
    mainСharacterr "Так значит способ всё же есть, но они скрывают его. Мне нужно срочно его найти. Но сейчас мне надо в офис к Питеру."
    jump stayWithPiter
    return

label stayWithPiter:
    with fade
    with dissolve
    scene PitersOffice
    show piter at left
    MrPiter "Ну что, как тебе пробный рабочий день у нас?"
    mainСharacterr "Вполне неплохо. Я так понимаю у вас весь город это игра, раз у вас все на питоне пишут?"
    MrPiter "Абсолютно нет. Как ты мог заметить наш город поделён на районы, каждый район это направление,
    которое можно реализовать на питоне. Но на самом деле на питоне можно сделать даже больше чем у нас районов.
    Просто мы пока что развиваемся, из-за чего у нас и нет представителей всех направлений."
    mainСharacterr "Вау, как круто. А есть ли ещё кому помочь чтобы больше узнать о возможностях Python?"
    MrPiter "Питер - Хм, сейчас спрошу.{w=2} Можешь пойти в Data район, там сейчас Марку не помешала бы помощь.  Вот тебе адрес его офиса, он тебя встретит"
    jump MarkTask
    return

label MarkTask:
    with fade
    scene dataCity
    with dissolve
    show mark at right
    DataMark "Привет, ты же [mainPerson]?"
    mainСharacterr " Да, знаю, знаю. Слышал ты  успешно справился с работой Питера. Если и дальше будешь так успешен во всех наших района,
    то есть большая вероятность попасть на работу в главный офис нашего города.{w} Ты ведь наверняка его видел, э
    то офис к которому идут провода от всех районов города."
    mainСharacterr "Звучит здорово. Ну так давай тогда не будем медлить, какая работа для меня тут есть?"
    DataMark "Cмотри, мой район занимается анализом различных данных, начиная от погодных и финансовых, заканчивая данными об успешности детского образования. В общем анализом любых данных."
    DataMark "Собственно мне бы не помешала помощь с анализом данных успеваемости моих сотрудников. Да, это довольно трудное задание, но раз ты так легко справился с задание у Питера, то возможно справишься и с этим."
    show markWithBook at right
    DataMark "Вот тебе вся нужная документация и книги с помощью которых ты можешь изучить как делать нашу работу. Если справишься сам, то я обязательно замолвлю за тебя словечко."
    mainСharacterr "Ну попробую. {w}Но можно сперва вопрос, что это за заброшенные здания там впереди?"
    with dissolve
    scene heat
    show mark at left
    DataMark "Не важно, это заброшенный район, там нет никого, да и вообще скоро мы его удалим, все равно от него одни проблемы. Давай меньше вопросов и скорее приступай к работе."
    "Хм, он явно что-то пытался скрыть, надо будет сходить туда, а пока что нужно разобраться как это делать, чтобы увеличить свои шансы на попадание в главный офис."
    with dissolve
    scene time
    "какое-то время спустя..."
    with fade
    scene try
    mainСharacterr "Так, ну вроде должно сработать."
    with dissolve
    scene result
    mainСharacterr "Вау, у меня получилось. Это даже оказалось легче чем я думал."
    with dissolve
    show mark at right
    DataMark "Ну что, не сделал? Так и знал, что тебе перехвалили..."
    mainСharacterr "Нет, вот, у меня всё готово!"
    DataMark "Ого, да ты и вправду похоже гений. Сейчас я напишу Софии, чтобы она тоже дала тебе какую-то работу. Если ты справишься и с ней, то считай, что ты уже получил своё место в главном офисе."
    jump choices
    return

label choices:
    with fade
    scene dataCity
    menu:
        "Может быть сходить, посмотреть, что находится в заброшенном районе..."
        "Пойти к Софии":
            jump SofiaTask
        "Пойти в Заброшенный район":
            jump checkOldArea
    return

label checkOldArea:
    $ greenCount = 1
    with fade
    scene oldArea
    mainСharacterr "М-да и зачем я сюда пришёл, похоже тут и вправду ничего нет. Нужно идти обратно."
    with dissolve
    show inkognito
    AreaInkognito "Ты кто такой и что тут забыл?"
    mainСharacterr "Я... Я [mainPerson] я и сам не знаю как сюда попал, я сидел дома, а потом..."
    AreaInkognito "Что?! Ты хочешь сказать что ты ещё один?"
    mainСharacterr " Ещё один кто?"
    AreaInkognito "Ещё один из тех, кто каким-то образом попал в этот виртуальный мир?"
    show NoName at right
    show NoName1 at left
    AreaInkognito "Нет... Мы находимся тут всё лето. Мы искали куда можно поступить, проклинали тех, кто решил,
    что люди только окончившие школу могут выбрать кем быть. Как вдруг нам пришло сообщение..."
    mainСharacterr "cообщение от какого-то Mr.Python?"
    AreaInkognito "Да. После чего мы и попали сюда. Спустя какое-то время я узнал, что кого-то тут держат взаперти..."
    AreaInkognito "Я надеялся, что возможно он мне сможет помочь, но я изучал только Pascal и ничего не хотел учить больше из-за чего я
    стал отбросом общества и мне пришлось убежать в этот заброшенный район."
    mainСharacterr "Я могу помочь нам всем. Если я сейчас успешно выполню 3 задание у Софии, то смогу попасть на работу в главный офис. Не знаешь где именно его держат?"
    AreaInkognito "Есть слухи, что он находиться на самом верхнем этаже офиса, над этажом мэра."
    mainСharacterr "Тогда я скорее пойду к Софии, если я узнаю как выбраться, то обязательно приду спасти вас!"
    jump SofiaTask
    return

label SofiaTask:
    with fade
    scene WebArea
    with dissolve
    show WebSofia
    mainСharacterr "Привет. Я слышал у тебя есть работа для меня."
    Sofia "Привет, есть. В общем в этом районе мы делаем различные WEB мероприятия. Но в нашем новом проекте завёлся один халтурщик, который ужас как плохо всё сделал. Мы как раз рядом, вот..."
    #картинка
    mainСharacterr "По моему тут всё шикарно или я что-то не понимаю?"
    Sofia "Это Front мы его заказываем из другой долины. А вот Back делаем мы и пошли посмотрим что он тут сделал."
    #картинка
    mainСharacterr "Да, он явно не старался. Ну ладно, давай книги или объясни как делать и я сделаю."
    Sofia "Нет, мне рассказали что ты уже сделал и куда метишь. Так что делай всё сам, а я побежала, пока мои ещё чего не испортили."
    scene time
    "какое-то время спустя..."
    #картинка
    mainСharacterr "Ну вот другое дело, у меня явно получилось исправить тот кошмар."
    Sofia "Ого, ты сам это сделал?! Это просто снос фляги, ты реально гений. Сейчас я напишу мэру и можешь идти в главный офис."
    Sofia "Всё, можешь идти он будет ждать тебя у входа в офис."
    jump Ending
    return

label Ending:
    with fade
    scene mainBuilding
    show mayor at right
    MrMayor "Приветствую тебя наш юный гений. Очень много слышал о твои результатах."
    mainСharacterr "Спасибо большое. Я очень старался, особенно после того как узнал, что можно попасть к вам в главный офис."
    MrMayor "Ну ты ещё не попал. Но перед тем как я расскажу, что тебе нужно сделать пошли ко мне в кабинет."
    #картинка
    MrMayor " Так, ну для начала давай я тебе расскажу чем мы тут занимаемся. Как ты мог видеть мы центральное звено всех офисов.
    Мы собираем и анализируем всю информацию от районов."
    #Звук
    "Звук падение чего-то с потолка в кабинете мэра."
    mainСharacterr "Что это было?"
    MrMayor "Не обращай внимание. Просто там выше служебный этаж лифта и прочего оборудования, видимо что-то упало просто."
    MrMayor "Ну, а также помогаем районам с их проектами, а также с их проблемами. Собственно твоя задача будет довольно проста."
    #картинка
    MrMayor "Видишь вон там заброшенный район?"
    MrMayor "Тебе нужно его просто удалить не оставив ни следа от него. Я думаю ты справишься если мне не наврали о тебе. {w}
    А я пока что уйду на обеденный перерыв, можешь садиться за мой стол и приступать к работе."
    return
