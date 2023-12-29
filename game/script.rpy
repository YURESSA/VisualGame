# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
define mainСharacterr = Character('[mainPerson]', color="#c8ffc8", image="Main")
define MrPython = Character('Mr. Python', color="#008B8B")
define MrMayor = Character('Владимир Олегович', color="#6A5ACD")
define MrPiter = Character('Питер', color="#556B2F")
define DataMark = Character('Марк', color='#90EE90')
define Sofia = Character('София', color='#BA55D3')
define AreaInkognito = Character('Незнакомец', color='#A9A9A9')
define AreaPrisoner = Character('Заключённый', color='#A9A9A9')

#Персонажи
image hero = "characters/Main.png"
image mayor = "characters/mayor.png"
image mayorWithHand = "characters/mayorWithHand.png"
image mayorSurprise= "characters/mayorSurprise.png"

image piter = "characters/Piter.png"
image piterSad = "characters/PiterSad.png"
image piterCheerfull = "characters/PiterCheerfull.png"
image piterSurprise = "characters/PiterSurprise.png"
image piterLaugh = "characters/PiterLaugh.png"


image mark = "characters/Mark.png"
image markWithBook = "characters/MarkWithBook.png"
image markShiny = "characters/MarkShiny.png"
image markSurprise = "characters/MarkSurprise.png"
image markSmile = "characters/MarkSmile.png"

image inkognito = "characters/inkognito.png"
image NoName = "characters/NoName.png"
image NoName1 = "characters/NoName.png"

image WebSofia = "characters/Sofia.png"
image WebSofiaForMenu = "characters/SofiaForMenu.png"
image WebSofiaSmile = "characters/SofiaSmile.png"
image WebSofiaSurprise = "characters/SofiaSurprise.png"
image WebSofiaWithPhone = "characters/SofiaWithPhone.png"

image Prisoner = "characters/Prisoner.png"

#Комната персонажа
image perspectiveScreen = "room/perspectiveScreen.png"
image roomFrom = "room/roomFrom.png"
image notification = "room/notification.png"
image notificationFromMrPython = "room/MrPython.png"
image teleportation = "room/teleportation.png"

#Виртуальный мир
image gates = "virtualWorld/gates.png"
image city = "virtualWorld/city.png"
image mainBuilding = "virtualWorld/mainBuilding.jpg"
image work = "PiterTask/work.png"
image completeWork = "PiterTask/CompleteWork.png"
image GameDev = "PiterTask/GameDev.png"
image office = "PiterTask/office.png"

#Секретная комната
image secretRoom = "SecretRoom/secret_room.png"
image RedRoom = "SecretRoom/RedRoom.png"
image PitersOffice = "PitersOffice/office.jpg"

#DataCity
image dataCity = "MarkTasks/dataCity.jpg"
image data = "MarkTasks/data.jpg"
image heat = "MarkTasks/heat.png"
image try = "MarkTasks/Try.png"
image result = "MarkTasks/result.png"

#Старый район
image oldArea = "oldArea/oldArea.png"
image Punch = "oldArea/Punch.png"
image oldHouse = "oldArea/oldHouse.png"

#Web район
image WebCity = "SofiaTask/WebCity.png"
image Task = "SofiaTask/Task.png"
image CompleteTask = "SofiaTask/CompleteTask.png"
image Example = "SofiaTask/Example.png"


image mayorOffice = "MayorTask/mayorOffice.png"
image mayorTask = "MayorTask/Task.png"
image completeTask = "MayorTask/completeTask.png"
image atTheTable = "MayorTask/atTheTable.png"
image Title = "MayorTask/Тitle.png"

#Prisiner Task
image Jail = "PrisonerTasks/Jail.png"
image WithoutHandcuffs = "PrisonerTasks/WithoutHandcuffs.png"
image EmptyOffice = "PrisonerTasks/EmptyOffice.png"
image Ladder = "PrisonerTasks/Ladder.png"
image MainHeroWithPrisoner = "PrisonerTasks/MainHeroWithPrisoner.png"
image Portal = "PrisonerTasks/portal.png"
image SaveFromHouse = "PrisonerTasks/SaveFromHouse.png"
image SaveSolo = "PrisonerTasks/SaveSolo.png"
image SaveWithPeople = "PrisonerTasks/SaveWithpeople.png"
image teleport = "PrisonerTasks/teleport.png"
image WithoutHandcuffs = "PrisonerTasks/WithoutHandcuffs.png"
image MainHeroWithPrisoner = "PrisonerTasks/MainHeroWithPrisoner.png"

#Ending
image end = "ending/end.png"

define greenCount = 0
define oldArea = 0
define secretRoom = 0
define keys = 0
define audio.notification = "notifyFromVK.mp3"
define audio.mouseClick = "mouseClick1.mp3"
define audio.portal = "portal.mp3"
define audio.writeCode = "writeCode.mp3"
define audio.sucess = "sucess.mp3"
define audio.goWithPiter = "goWithPiter.mp3"
define audio.gameZone = "gameZone.mp3"
define audio.forTitles = "forTitles.mp3"
define audio.enterMessage = "enterMessage.mp3"
define audio.walkOldArea = "walkOldArea.mp3"
define audio.catch = "catch.mp3"
define audio.fallOfHeap = "fallOfheap.mp3"
define audio.getKey = "getKey.mp3"
define audio.walkToNextFloor = "walkToNextFloor.mp3"
define audio.startSound = "startSound.mp3"
define audio.musicSpeed = "musicSpeed.mp3"
define audio.musicNormal = "musicNormal.mp3"
define audio.FreePrisoner = "FreePrisoner.mp3"
define audio.sit = "sit.mp3"
define audio.sit = "sleep.mp3"
define redRoom = "redRoom.mp3"
define oldMusic = "oldArea.mp3"

# Игра начинается здесь:
label start:
    play music startSound
    scene roomFrom
    $ mainPerson = renpy.input('Придумай имя для главного героя (мужской пол)').capitalize()
    if mainPerson == '':
        $ mainPerson = "Миша"
    with dissolve
    scene roomFrom
    with dissolve
    mainСharacterr "М-да, опять я поздно ложусь... {w}Когда я уже выберу чем хочу
    заниматься. Скоро ведь уже конец срока подачи документов. Кто вообще даёт
    такой выбор людям, только что закончившим школу?! Вот бы кто-то дал мне
    хоть какой-нибудь знак…"
    play sound notification
    with dissolve
    scene notification
    with dissolve
    mainСharacterr "Хм, кто бы мог написать мне в 3 часа ночи?"
    play sound mouseClick
    with dissolve
    scene notificationFromMrPython
    with dissolve
    MrPython "Ты амбициозен? Любишь решать нестандартные задачи?
    Обожаешь интересный опыт? Тогда скорее переходи по ссылке и погружайся в
    незабываемый мир программирования."
    mainСharacterr "О, это же полностью про меня, мельком посмотрю после чего уже точно пойду спать."
    with dissolve
    scene teleportation
    with dissolve
    play sound portal
    with dissolve
    jump virtualWord
    stop music fadeout 1
    return


label virtualWord:
    play music musicSpeed
    with fade
    scene gates
    mainСharacterr "Что это за безобразие?! {w}Где это я?"
    show mayor at right
    with dissolve
    MrMayor "Привет, меня зовут Владимир Олегович. Я являюсь мэром Кодовой долины. Приветсвую тебя!"
    with dissolve
    mainСharacterr"Вау, что это? Объясни, пожалуйста, поподробнее."
    with dissolve
    MrMayor "Кодовая долина это место, где ты можешь реализовать всё что
    захочешь, начиная с маленьких и красивых WEB-приложений и заканчивая
    искусственным интеллектом."
    MrMayor "А сейчас нам нужно быстрее идти, нас уже ждут."
    hide mayor
    hide hero
    with fade
    scene city
    "Зайдя в город, [mainPerson] увидел необычайно красивый, но странный город. Всё  в
    нем говорило о том, что этот город был написан каким-то разработчиком."
    "Где-то были участки, которые были закомментированы, а где-то здания, которые держались на костылях."
    with fade
    scene mainBuilding
    show piter at right

    show WebSofiaForMenu at left
    show mark:
        xalign 0.15
        yalign 0.9
    show mayorWithHand:
        xalign 0.6
        yalign 0.9
    with dissolve
    MrMayor "Знакомься это представители наших районов."
    with dissolve
    mainСharacterr "Всем привет! Меня зовут [mainPerson]."
    with dissolve
    MrMayor "Сейчас иди с Питером ему нужна помощь. Он из района под название
            GameDev и ему срочно нужно дописать свой проект. Я думаю по пути он тебе
            всё расскажет, а мне и остальным пора бежать."
    hide mayor
    scene GameDev
    show piter:
        xalign 0.6
        yalign 0.99
    with dissolve
    MrPiter "Привет! Как ты мог услышать я Питер. Я отвечаю за GameDev район."
    hide piter
    show piterSad:
        xalign 0.6
        yalign 0.99
    extend " В общем проблема такая. Скоро у меня срок сдачи проекта, а мне ужас
            как не хватает рук чтобы доделать детскую площадку."
    with dissolve
    mainСharacterr "Я бы с удовольствие помог, но я не умею строить площадки, да я
                    и не настолько физически сильный, так что вынужден отказать."
    hide piterSad
    show piterLaugh:
        xalign 0.6
        yalign 0.99
    MrPiter "Хах. Строить?! {w=1}Таким уже очень давно никто не занимается, откуда ты
            вообще такой взялся, что у вас там строят."
    MrPiter "У нас не строят, у нас пишут всё в этом городе, начиная от зданий, заканчивая продуктами.
    Ты, надеюсь, слышал хотя бы когда-нибудь о Python?"
    menu:
        "Ну что-то слышал. Это какой-то один из множества языков программирования":
            jump ifDontKnow
        "Да, это один из самых популярных языков программирования, который может
        справляться совершенно с различными заданиями.":
            jump ifKnow
    return


label ifDontKnow:
    hide piterLaugh
    show piter
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
    hide piterLaugh
    show piter
    with dissolve

    MrPiter "О, а ты молодец, что интересуешься этим, тогда ты с легкостью справишься с моим заданием."
    with dissolve
    mainСharacterr "Хорошо, я готов тебе помочь!"
    jump helpPiter
    return


label helpPiter:
    with dissolve
    mainСharacterr "А как выбраться отсюда?"
    hide piter
    show piterSurprise
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
    play music writeCode
    scene time
    pause 1.5
    scene completeWork
    stop music fadeout 1
    play music musicSpeed
    play sound gameZone
    show piter at right
    MrPiter "Вау! У тебя отлично получилось. А ведь это твой первый проект!
            Тебя ждёт отличное будущее в нашем мире.{w=1} Пошли в главный офис нашего
            района, нужно отчитаться о проделанной работе."
    scene office
    show piter at right
    MrPiter "Ну вот и пришли, тут ты будешь работать, если выберешь жить в нашем районе."
    mainСharacterr "А что это за кабинет куда вход строго запрещён?"
    MrPiter "Эм, это не важно... {w=1} Пошли скорее дальше."
    menu:
        "Пойти дальше с Питером.":
            jump stayWithPiter
        "Попробовать отстать от Питера и посмотреть, что находится в серкетной комнате.":
            jump checkSecretRoom
    return

label checkSecretRoom:
    $ greenCount = 1
    $ secretRoom = 1
    mainСharacterr "Ой, а можно я поговорю с другими сотрудниками, чтобы лучше узнать потенциальное место работы?"
    MrPiter "Да, конечно. Могу рассказать тебе про все отделы."
    mainСharacterr"А можно ли без тебя? Просто боюсь, что работники могут сказать не то, что
    хотят при виде начальника."
    hide piter
    show piterLaugh at right
    MrPiter "Хах, да, хорошо. Тогда жду у себя в кабинете."
    with fade
    play music redRoom
    scene secretRoom
    mainСharacterr "Так нужно быстро осмотреть комнату. Может тут будут какие-то подсказки как выбраться отсюда."
    scene RedRoom
    MrPython "Что будем делать с нашим заключённым? Я считаю, что его нужно убрать ведь он единственный, кто знает, что из нашего мира есть выход. Что думаешь ты?"
    mainСharacterr "Так значит способ всё же есть, но они скрывают его. Мне нужно срочно его найти. Но сейчас мне надо в офис к Питеру."
    jump stayWithPiter
    stop music fadeout 1
    return

label stayWithPiter:
    play music startSound
    with fade
    scene PitersOffice
    show piter at left
    MrPiter "Ну что, как тебе пробный рабочий день у нас?"
    mainСharacterr "Вполне неплохо. Я так понимаю у вас весь город это игра, раз у вас все на питоне пишут?"
    MrPiter "Абсолютно нет. Как ты мог заметить наш город поделён на районы, каждый район это направление,
    которое можно реализовать на питоне."
    MrPiter "Но на самом деле на питоне можно сделать даже больше чем у нас районов.
    Просто мы пока что развиваемся, из-за чего у нас и нет представителей всех направлений."
    mainСharacterr "Вау, как круто. А есть ли ещё кому помочь чтобы больше узнать о возможностях Python?"
    MrPiter "Хм, сейчас спрошу.{w=2}"
    play sound enterMessage
    extend " Можешь пойти в Data район, там сейчас Марку не помешала бы помощь. Я дам тебе адрес его офиса, он тебя встретит."
    jump MarkTask
    return

label MarkTask:
    play music musicNormal
    with fade
    scene dataCity
    with dissolve
    show mark at right
    DataMark "Привет, ты же [mainPerson]?"
    mainСharacterr "Привет, да. Я попросил Питера узнать, есть ли ещё какая-то работа, чтобы узнать о возможностях Python."
    hide mark
    show markSmile at right
    DataMark "Да, знаю, знаю. Слышал ты успешно справился с работой Питера. Если и дальше будешь так успешен во всех наших районах,
    то есть большая вероятность попасть на работу в главный офис нашего города."
    DataMark "Ты ведь наверняка его видел, это офис, к которому идут провода от всех районов города."
    mainСharacterr "Звучит здорово. Ну так давай тогда не будем медлить, какая работа для меня тут есть?"
    DataMark "Ну смотри, мой район занимается анализом различных данных, начиная от погодных и финансовых, заканчивая данными об успешности детского образования. В общем анализом любых данных."
    DataMark "Собственно мне бы не помешала помощь с анализом данных успеваемости моих сотрудников. Да, это довольно трудное задание, но раз ты так легко справился с задание у Питера, то возможно справишься и с этим."
    hide makrSmile
    hide mark
    show markWithBook at right
    DataMark "Вот тебе вся нужная документация и книги, с помощью которых ты сможешь изучить как делать нашу работу. Если справишься сам, то я обязательно замолвлю за тебя словечко."
    mainСharacterr "Ну, попробую. {w}Но можно сперва вопрос, что это за заброшенные здания там впереди?"
    with dissolve
    scene oldArea
    show markShiny at left
    DataMark "Не важно, это заброшенный район, там нет никого, да и вообще скоро мы его удалим, все равно от него одни проблемы. Давай меньше вопросов и скорее приступай к работе."
    with dissolve
    scene dataCity
    "Хм, он явно что-то пытался скрыть, надо будет сходить туда, а пока что нужно разобраться как это делать, чтобы увеличить свои шансы на попадание в главный офис."
    with dissolve
    scene time
    stop music fadeout 1
    play music writeCode
    pause 1.5
    with fade
    stop music fadeout 1
    play music musicNormal
    scene try
    mainСharacterr "Так, ну вроде должно сработать."
    with dissolve
    scene result
    play sound sucess
    mainСharacterr "Вау, у меня получилось. Это даже оказалось легче чем я думал."
    with dissolve
    show markSmile at right
    DataMark "Ну что, не сделал? Так и знал, что тебе перехвалили..."
    mainСharacterr "Нет, вот, у меня всё готово!"
    hide markSmile
    show markSurprise at right
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
    play music walkOldArea
    $ greenCount = 1
    $ oldArea = 1
    with fade
    scene oldArea
    mainСharacterr "М-да, и зачем я сюда пришёл, похоже тут и вправду ничего нет. Нужно идти обратно."
    stop music fadeout 1
    play music oldMusic
    with fade
    scene Punch
    play sound catch
    mainСharacterr "Чт-то происходит?"
    scene oldHouse
    with dissolve
    show inkognito
    AreaInkognito "Ты кто такой?"
    mainСharacterr "Я... Я [mainPerson]."
    AreaInkognito "И что ты тут забыл, [mainPerson]?"
    mainСharacterr "Я и сам не знаю как сюда попал, я сидел дома, а потом..."
    AreaInkognito "Что?! Ты хочешь сказать что ты ещё один?"
    mainСharacterr " Ещё один кто?"
    AreaInkognito "Ещё один из тех, кто каким-то образом попал в этот виртуальный мир?"
    with dissolve
    show NoName at right
    show NoName1 at left
    AreaInkognito "Нет... Мы находимся тут всё лето. Мы искали куда можно поступить, проклинали тех, кто решил,
    что люди только окончившие школу могут выбрать кем быть. Как вдруг нам пришло сообщение."
    mainСharacterr "Сообщение от какого-то Mr.Python?"
    AreaInkognito "Да. После чего мы и попали сюда. Спустя какое-то время я узнал, что мэр держит кого-то взаперти..."
    AreaInkognito "Я надеялся, что возможно он мне сможет помочь, но я изучал только Pascal и ничего не хотел учить больше из-за чего я
    стал отбросом общества, и мне пришлось убежать в этот заброшенный район."
    mainСharacterr "Я могу помочь нам всем. Если я сейчас успешно выполню третье задание у Софии, то смогу попасть на работу в главный офис. Не знаешь где именно его держат?"
    AreaInkognito "Есть слухи, что он находиться на самом верхнем этаже офиса, над этажом мэра."
    mainСharacterr "Тогда я скорее пойду к Софии, если я узнаю как выбраться, то обязательно приду спасти вас!"
    jump SofiaTask

label SofiaTask:
    play music startSound
    with fade
    scene WebCity
    with dissolve
    show WebSofiaForMenu
    mainСharacterr "Привет. Я слышал у тебя есть работа для меня."
    Sofia "Привет, есть. В общем в этом районе мы делаем различные WEB мероприятия. Но в нашем новом проекте завёлся один халтурщик,
    который ужас как плохо всё сделал. Мы как раз рядом, вот..."
    scene Example
    show WebSofiaForMenu at right
    mainСharacterr "По моему тут всё шикарно или я что-то не понимаю?"
    Sofia "Это Front мы его заказываем из другой долины. А вот Back делаем мы и пошли посмотрим что он тут сделал."
    scene Task
    mainСharacterr "Да, он явно не старался. Ну ладно, давай книги или объясни как делать и я сделаю."
    hide WebSofia
    with dissolve
    show WebSofiaSmile at right
    Sofia "Нет, мне рассказали что ты уже сделал и куда метишь. Так что делай всё сам, а я побежала, пока мои ещё чего не испортили."
    with dissolve
    play music writeCode
    scene time
    pause 1.5
    stop music fadeout 1
    play music startSound
    with fade
    scene CompleteTask

    play sound gameZone
    mainСharacterr "Ну вот другое дело, у меня явно получилось исправить тот кошмар."
    show WebSofiaSurprise at right
    Sofia "Ого, ты сам это сделал?! Это просто снос бошки, ты реально гений. Сейчас я напишу мэру и можешь идти в главный офис."
    hide WebSofiaSurprise
    show WebSofiaWithPhone at right
    play sound enterMessage
    pause 0.25
    Sofia "Всё, можешь идти он будет ждать тебя у входа в офис."
    jump Ending
    return

label Ending:
    with fade
    scene mainBuilding
    show mayorWithHand at right
    MrMayor "Приветствую тебя, наш юный гений! Очень много слышал о твои результатах."
    mainСharacterr "Спасибо большое. Я очень старался, особенно после того как узнал, что можно попасть к вам в главный офис."
    MrMayor "Ну ты ещё не попал. Но перед тем как я расскажу, что тебе нужно сделать, пошли ко мне в кабинет."
    with fade
    scene mayorOffice
    show mayor at right
    MrMayor " Так, ну для начала давай я тебе расскажу чем мы тут занимаемся. Как ты мог видеть мы центральное звено всех офисов.
    Мы собираем и анализируем всю информацию от районов."
    play sound fallOfHeap
    pause 0.25
    hide mayor
    show mayorSurprise at right
    mainСharacterr "Что это было?"
    MrMayor "Не обращай внимание. Просто там выше служебный этаж лифта и прочего оборудования, видимо что-то упало просто."
    hide mayorSurprise
    show mayor at right
    MrMayor "Ну, а также помогаем районам с их проектами и проблемами. Собственно твоя задача будет довольно проста."
    with fade
    scene mayorTask
    show mayor at right
    MrMayor "Видишь вон там заброшенный район?"
    MrMayor "Тебе нужно его просто удалить не оставив ни следа от него. Я думаю ты справишься, если мне не наврали о тебе."
    with fade
    scene mayorOffice
    show mayor at right
    MrMayor "А я пока что уйду на обеденный перерыв. Можешь садиться за мой стол и приступать к работе."
    if greenCount:
        menu:
            "Взять ключи":
                $ keys = 1
                play sound getKey
                jump GoToPrisoner
            "Пойти на этаж выше":
                jump GoToPrisoner
            "Делать задание мэра":
                jump MayorsTask
    else:
        jump MayorsTask
    return

label MayorsTask:
    scene atTheTable
    play sound sit
    mainСharacterr "Пора приступать к заданию!"
    scene time
    play music writeCode
    pause 1.5
    stop music fadeout 1
    play music musicNormal
    scene completeTask
    show mayor at right
    MrMayor "Ооо, я смотрю ты уже сделал моё задание!"
    MrMayor "Поздравляю! Теперь ты часть нашей команды!"
    jump Titles
    return

label GoToPrisoner:
    with fade
    scene Ladder
    play music walkToNextFloor
    pause 2
    stop music fadeout 1
    jump Prisoner
    return

label Prisoner:
    play music redRoom
    with fade
    scene Jail
    mainСharacterr "Ты тот, кто знает, как можно выбраться отсюда?"

    AreaPrisoner "Что!? Ты настоящий человек?! Господи, я не видел живой души уже несколько лет. Да, я знаю как можно выбраться из этого мира,
    за это меня и держат в заточении."
    AreaPrisoner "Чтобы выбраться из этого мира также как и во всём тут нужно использовать Python, есть функция под названием ComeBackToReal,
    и если её вызвать, то ты и все те, кто будет рядом с тобой из настоящих людей вернутся в реальную жизнь."
    AreaPrisoner "Я помог тебе, а теперь мне нужна твоя помощь, у тебя есть способ спасти меня?"
    if keys:
        jump SafePrisoner
    else:
        jump DontSafePrisoner
    return

label SafePrisoner:
    mainСharacterr "Я взял какую-то связку ключей. Сейчас попробую."
    play music FreePrisoner
    with dissolve
    scene WithoutHandcuffs
    stop music fadeout 1
    play music musicNormal
    show Prisoner at right
    AreaPrisoner "Спасибо тебе большое, а теперь нужно как можно быстрее вызвать эту функцию."
    if oldArea:
        jump SafeAnother
    else:
        jump Safe
    return

label Safe:
    mainСharacterr "Мэра сейчас нет в своём офисе, скорее бежим туда пока он не вернулся!"
    AreaPrisoner "Всё, готово. Наконец-то спустя столько лет я увижу реальный мир!"
    extend " Спасибо тебе [mainPerson]!"
    play sound portal
    with dissolve
    scene Portal
    pause 1
    with dissolve
    scene EmptyOffice
    MrMayor "Вот чёрт, не успел..."
    jump Titles
    return

label SafeAnother:
    mainСharacterr "Я не могу просто так уйти. В заброшенном районе есть люди как мы, и я обещал спасти их."
    AreaPrisoner "Дело твоё, беги и спасай их. А я, после стольких лет заключения, лучше точно спасусь сам."
    play music walkOldArea
    with dissolve
    scene Ladder
    pause 1
    with dissolve
    scene WebCity
    pause 1
    with dissolve
    pause 1
    scene oldArea
    with dissolve
    pause 1
    scene MainHeroWithPrisoner
    stop music fadeout 1
    play music musicNormal
    scene SaveFromHouse
    mainСharacterr "Я НАШЁЛ! {w=1}Я нашёл способ спастись, скорее все ко мне!"
    play sound portal
    with dissolve
    scene SaveWithPeople
    pause 3
    play music musicNormal
    jump Teleport
    return

label Teleport:
    play sound sleep
    scene end
    mainСharacterr "Да уж, вот это сон. Надо наверное и вправду поступать туда где учат Python разработчиков,
     ведь всё правда как во сне, на питоне можно многое реализовывать, а главное он легче чем многие другие языки."
    mainСharacterr "Надо будет запомнить, вдруг когда я поступлю надо будет сделать визуальную новеллу. А у меня уже готовый сюжет будет."
    jump Titles
    return

label DontSafePrisoner:
    scene Jail
    mainСharacterr "Прости, но я не знаю как тебе помочь..."
    AreaPrisoner "Эх, жаль... {w=1} Ну тогда скорее беги отсюда и не смей возвращаться спасать меня, иначе и тебя могут поймать"
    mainСharacterr "Хорошо, я понял тебя, спасибо тебе большое. Прости, что никак не могу спасти тебя..."
    if oldArea:
        jump GoToSafeAnother
    else:
         jump GoToSafe
    return

label GoToSafeAnother:
    play music walkOldArea
    with dissolve
    scene Ladder
    pause 1
    with dissolve
    scene WebCity
    pause 1
    with dissolve
    scene oldArea
    pause 1
    with dissolve
    scene MainHeroWithPrisoner
    stop music fadeout 1
    play music musicNormal
    scene SaveFromHouse
    mainСharacterr "Я НАШЁЛ! {w=1} Я нашёл способ спастись, скорее все ко мне!"
    play sound portal
    with dissolve
    scene SaveWithPeople
    pause 3
    play music musicNormal
    jump Teleport
    return

label GoToSafe:
    pause 0.5
    scene SaveSolo
    pause 0.5
    play sound portal
    scene teleport
    pause 1.5
    scene EmptyOffice
    MrMayor "Вот чёрт, не успел..."
    jump Teleport
    return

label Titles:
    play music forTitles
    scene Title
    pause 999999
    return
