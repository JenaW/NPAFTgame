import string
import random
from os import system
from typing import List, Any, Union

"""This is code for the name, place ... game. """

letter = random.choice(string.ascii_letters).upper()  # generates a random letter
let = letter.lower()  # ensures the letter is lowercase


def name1():  # selects a name randomly for CPU

    names: List[Union[str, Any]] = [("Adam"), ("Ben"), ("Cathy"), ("Derek"), ("Daniel"), ("Ed"), ("Edward"), ("Frank"),
            ("Frankenstein"),("George"),
             ("Hannah"), ("Isaac"), ("Ian"), ("John"), ("Josh"), ("Kate"), ("Katy"), ("Liam"), ("Lance"), ("Lisa"),
             ("Larry"),
             ("Matt"), ("Matthew"), ("Nicole"), ("Nickie"), ("Opal"), ("Oprah"), ("Queeley"), ("Richard"), ("Richy"),
             ("Steve"),
             ("Sarah"), ("Trish"), ("Tammy"), ("Tanner"), ("Uniqua"), ("Veronica"), ("Vanessa"), ("Will"), ("William"),
             ("Xavier"),
             ("Yannis"), ("Yannick"), ("Zoey"), ("Zaya")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(names) - 1)  # random number in the range of the size of the tuple
            names2 = names[num]  #
            let2 = names2[0]

            if letter == let2:  # Checks if name begins with the random letter
                name_ans = names[num]
                # print("Name: "+ name_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        name_ans = "No Answer"
        # print ("No answer")

    return name_ans


def name2():  # CPU generates a name

    names = [("Ashley"), ("Brad"), ("Brandon"), ("Blake"), ("Candice"), ("Cassy"), ("Dexter"), ("Evan"), ("Finn"),
             ("Fred"), ("Freddy"), ("Greg"), ("Grace"), ("Harry"), ("Harrison"), ("Isaac"), ("Isabella"), ("Jake"),
             ("Jack"), ("Lena"), ("Lawrence"), ("Lisa"), ("Mica"), ("Michael"), ("Mickey"), ("Nancy"), ("Noah"),
             ("Patricia"), ("Phillip"), ("Paul"), ("Perry"), ("Quinn"), ("Rick"), ("Ralph"), ("Rene"), ("Shannon"),
             ("Susy"), ("Shane"), ("Sheldon"), ("Ted"), ("Terry"), ("Toby"), ("Tony"), ("Ulysses"), ("Ursula"),
             ("Victoria"), ("Victoria"), ("Walter"), ("Wes"), ("Wilma"), ("Xander"), ("Ximena"), ("Yuri"),
             ("Yannis"), ("Zeda"), ("Zelda"), ("Zoey")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(names) - 1)  # random number in the range of the size of the tuple
            names2 = names[num]  #
            let2 = names2[0]

            if letter == let2:  # Checks if name begins with the random letter
                name2_ans = names[num]
                # print("Name: "+ name_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        name2_ans = "No Answer"
        # print ("No answer")

    return name2_ans


def name3():  # CPU generates a name

    names = [("Ashley"), ("Amanda"), ("Anne"), ("Anna"), ("AJ"), ("Bailey"), ("Billy"), ("Cathy"), ("Chase"), ("Dan"),
             ("Ed"), ("Eugene"), ("Ellen"), ("Enrique"), ("Esteban"), ("Finneas"), ("Faith"), ("Frances"), ("Greg"),
             ("Genesis"), ("Georgia"), ("Henry"), ("Harry"), ("Holly"), ("Hunter"), ("Inoa"), ("Ismael"), ("Isa"),
             ("Janice"), ("Jerimian"), ("Jean"), ("Jay"), ("Kacey"), ("Kate"), ("Kai"), ("Kala"), ("Kay"), ("Lawrence"),
             ("Leah"), ("Leila"), ("Lauren"), ("Mario"), ("Mariana"), ("Mason"), ("Marcy"), ("Monique"), ("Matt"),
             ("Michelle"), ("Noah"), ("Nadia"), ("Nish"), ("Nicholas"), ("Nicolas"), ("Nick"), ("Nancy"), ("Nico"),
             ("Owen"), ("Otis"), ("Otto"), ("Oscar"), ("Peter"), ("Patrick"), ("Princess"), ("Piper"), ("Poppy"),
             ("Penny"),
             ("Quinn"), ("Quincy"), ("Quinten"), ("Ruel"), ("Ramsey"), ("Rashard"), ("Raul"), ("Rick"), ("Reagan"),
             ("Sam"),
             ("Samantha"), ("Sadie"), ("Shane"), ("Samarth"), ("Sasha"), ("Steve"), ("Stephen"), ("Taylor"), ("Teresa"),
             ("Thea"), ("Thasher"), ("Tess"), ("Ted"), ("Ulma"), ("Usman"), ("Uma"), ("Uri"), ("Vaughn"), ("Vicky"),
             ("Violet"), ("Vivian"), ("Vinny"), ("Winnie"), ("Wavely"), ("Wynonna"), ("Will"), ("William"), ("Xavi"),
             ("Xavier"), ("Xochitl"), ("Yasmine"), ("Yas"), ("Yana"), ("Yousef"), ("Yohan"), ("Zac"), ("Zach"),
             ("Zara"),
             ("Zahara"), ("Zaya"), ("Zariah")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(names) - 1)  # random number in the range of the size of the tuple
            names2 = names[num]  #
            let2 = names2[0]

            if letter == let2:  # Checks if name begins with the random letter
                name3_ans = names[num]
                # print("Name: "+ name_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        name3_ans = "No Answer"
        # print ("No answer")

    return name3_ans


def name4():  # CPU generates a name

    names = [("Ava"), ("Amanda"), ("Arianna"), ("Anna"), ("Ajani"), ("Adrian"), ("Brandon"), ("Braidey"), ("Brandy"),
             ("Bernice"),
             ("Billy"), ("Cathy"), ("Chase"), ("Cat"), ("Cassidy"), ("Chastity"), ("Ducky"), ("Daniela"), ("Demi"),
             ("Delilah"),
             ("Dora"), ("Ethan"), ("Ellie"), ("Eli"), ("Emma"), ("Elias"), ("Elijah"), ("Francis"), ("Frankie"),
             ("Fiona"),
             ("Florenace"), ("Flora"), ("Finley"), ("Ford"), ("Fletcher"), ("Frankie"), ("Frank"), ("Glenn"), ("Gio"),
             ("Gray"),
             ("Grayson"), ("Georgina"), ("Hussey"), ("Hamaza"), ("Harvey"), ("Hawk"), ("Hayes"), ("Ismael"), ("Isa"),
             ("Indiana"), ("Irvin"), ("Immanuel"), ("Irma"), ("Jasmine"), ("Jaelyn"), ("Janae"), ("Jaziah"),
             ("Janice"), ("Jesus"), ("Jordyn"), ("Jordan"), ("Kenedy"), ("Kaelyn"), ("Koelyn"), ("Kaliyah"), ("Karen"),
             ("Lizzo"), ("Liza"), ("Leann"), ("Leon"), ("Leonard"), ("Leroy"), ("Lester"), ("Mario"), ("Matt"),
             ("Martin"), ("Mosiah"), ("Marcea"), ("Malik"), ("Malikay"), ("Maurice"), ("Maria"), ("Margot"),
             ("Maxwell"), ("Nyjah"),
             ("Nolan"), ("Nathan"), ("Nia"), ("Nora"), ("Nyla"), ("Nigel"), ("Nixon"), ("Neymar"), ("Nico"), ("Odessa"),
             ("Odin"),
             ("Olive"), ("Octavia"), ("Otto"), ("Ofelia"), ("Paxton"), ("Pamela"), ("Penelope"), ("Priscila"), ("Pam"),
             ("Pax"),
             ("Quintin"), ("Quindel"), ("Queena"), ("Raz"), ("Rosie"), ("Rose"), ("Rasheed"), ("Raymond"), ("Raphael"),
             ("Seth"),
             ("Serena"), ("Saphire"), ("Shensea"), ("Sabrina"), ("Skip"), ("Sergio"), ("Stephon"), ("Trip"), ("Tamir"),
             ("Tabitha"), ("Tyler"), ("Troye"), ("Teo"), ("Tauren"), ("Urma"), ("Ushelle"), ("Uri"), ("Vince"), ("Vic"),
             ("Victor"), ("Violetta"), ("Veder"), ("Viktor"), ("Wavely"), ("Wesley"), ("Warren"), ("Wade"), ("Willow"),
             ("Xavi"), ("Xiomara"), ("Xzavier"), ("Xaiden"), ("Yahir"), ("Yash"), ("Yolanda"), ("Yamila"), ("Zyla"),
             ("Zuri"),
             ("Zion"), ("Zola"), ("Zooey")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(names) - 1)  # random number in the range of the size of the tuple
            names2 = names[num]  #
            let2 = names2[0]

            if letter == let2:  # Checks if name begins with the random letter
                name4_ans = names[num]
                # print("Name: "+ name_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        name4_ans = "No Answer"
        # print ("No answer")

    return name4_ans


def place1():  # CPU generates a place

    places = [("America"), ("Australia"), ("Austria"), ("Bahamas"), ("Belgium"), ("Brazil"), ("Colombia"), ("China"),
              ("Chile"),
              ("Denmark"), ("Dominica"), ("Egypt"), ("Ecuador"), ("England"), ("France"), ("Germany"), ("Greece"),
              ("Guinea"), ("Haiti"), ("Hungary"), ("India"), ("Iran"), ("Iraq"), ("Italy"), ("Jamaica"), ("Japan"),
              ("Kenya"), ("Kosovo"), ("Latvia"), ("Liberia"), ("Libya"), ("Luxembourg"), ("Madagascar"), ("Mexico"),
              ("New Zealand"), ("North Korea"), ("Norway"), ("Oman"), ("Panama"),
              ("Peru"), ("Poland"), ("Portugal"), ("Qatar"), ("Russia"), ("South Korea"), ("Spain"), ("Sri Lanka"),
              ("Sweden"),
              ("Taiwan"), ("Turkey"), ("Ukraine"), ("United Kingdom"), ("United States of America"),
              ("Venezuela"), ("Yemen"), ("Zambia"), ]
    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(places) - 1)  # random number in the range of the size of the tuple
            places2 = places[num]
            let2 = places2[0]

            if letter == let2:  # Checks if name begins with the random letter
                place_ans = places[num]
                # print("Name: " + place_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        place_ans = "No Answer"
        # print ("No answer")
    return place_ans


def place2():  # CPU generates a place

    places = [("Argentina"), ("Australia"), ("Austria"), ("Azerbaijan"), ("Bahamas"), ("Bangladesh"), ("Belgium"),
              ("Belize"),
              ("Botswana"), ("Brazil"), ("Bulgaria"), ("China"), ("Colombia"), ("Costa Rica"), ("Cuba"),
              ("Denmark"), ("Dominican Republic"), ("Ecuador"), ("Egypt"), ("El Salvador"), ("Ethiopia"), ("Finland"),
              ("France"), ("Germany"), ("Grenada"), ("Guyana"), ("Haiti"), ("Hungary"), ("India"), ("Indonesia"),
              ("Iran"), ("Italy"), ("Jamaica"), ("Japan"), ("Kazakhstan"), ("Kenya"), ("Kosovo"), ("Laos"),
              ("Liberia"), ("Libya"), ("Luxembourg"), ("Madagascar"), ("Mexico"), ("Netherlands"), ("New Zealand"),
              ("Nigeria"),
              ("Norway"), ("Oman"),
              ("Paraguay"), ("Philippines"), ("Portugal"), ("Qatar"), ("Romania"), ("Russia"), ("Sierra Leone"),
              ("Singapore"), ("South Korea"), ("Sri Lanka"), ("Sweden"), ("Switzerland"), ("Taiwan"), ("Thailand"),
              ("Trinidad and Tobago"), ("Uganda"), ("United Arab Emirates"),
              ("United Kingdom"), ("Uzbekistan"),
              ("Venezuela"), ("Vietnam"), ("Yemen"), ("Zambia"), ("Zimbabwe")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(places) - 1)  # random number in the range of the size of the tuple
            places2 = places[num]
            let2 = places2[0]

            if letter == let2:  # Checks if name begins with the random letter
                place2_ans = places[num]
                # print("Name: " + place_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        place2_ans = "No Answer"
        # print ("No answer")
    return place2_ans


def place3():  # CPU generates a place

    places = [("Afghanistan"), ("Algeria"), ("Angola"), ("Antigua and Barbuda"),
              ("Armenia"), ("Austria"), ("Bahrain"), ("Bangladesh"),
              ("Barbados"), ("Belize"), ("Benin"), ("Bhutan"), ("Bolivia"),
              ("Botswana"), ("Bulgaria"), ("Cabo Verde"), ("Cambodia"),
              ("Cameroon"), ("Central African Republic"), ("Colombia"),
              ("Comoros"), ("Congo"), ("Costa Rica"), ("Czechia"),
              ("Denmark"), ("Dominica"), ("Dominican Republic"), ("Ecuador"), ("El Salvador"),
              ("Eswatini"), ("Ethiopia"), ("Fiji"), ("Finland"),
              ("Gabon"), ("Gambia"), ("Georgia"), ("Ghana"), ("Guinea"), ("Haiti"), ("Honduras"), ("Hungary"),
              ("Iceland"),
              ("Indonesia"), ("Iran"), ("Ireland"), ("Israel"), ("Jamaica"), ("Japan"), ("Jordan"), ("Kazakhstan"),
              ("Kiribati"), ("Kosovo"), ("Kuwait"), ("Kyrgyzstan"), ("Laos"), ("Latvia"), ("Lebanon"),
              ("Liberia"), ("Libya"), ("Lithuania"), ("Madagascar"), ("Malawi"), ("Maldives"), ("Mali"),
              ("Micronesia"), ("Moldova"), ("Monaco"), ("Mongolia"), ("Montenegro"), ("Morocco"), ("Namibia"),
              ("Nepal"), ("Netherlands"), ("Niger"), ("Nigeria"),
              ("North Macedonia"), ("Oman"), ("Pakistan"), ("Palau"), ("Palestine"), ("Panama"), ("Papua New Guinea"),
              ("Peru"), ("Philippines"), ("Poland"), ("Qatar"), ("Romania"), ("Russia"),
              ("Rwanda"), ("Saint Kitts and Nevis"), ("Saint Lucia"), ("Samoa"),
              ("Saudi Arabia"), ("Senegal"), ("Seychelles"), ("Sierra Leone"),
              ("Singapore"), ("Somalia"), ("South Sudan"), ("Sri Lanka"), ("Sudan"), ("Suriname"), ("Syria"),
              ("Tajikistan"), ("Tanzania"), ("Thailand"), ("Tonga"),
              ("Trinidad and Tobago"), ("Tunisia"), ("Turkmenistan"), ("Tuvalu"), ("Uganda"), ("United Arab Emirates"),
              ("Uzbekistan"), ("Vanuatu"), ("Vatican City"),
              ("Venezuela"), ("Yemen"), ("Zambia"), ("Zimbabwe"), ("Ivory Coast")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(places) - 1)  # random number in the range of the size of the tuple
            places2 = places[num]
            let2 = places2[0]

            if letter == let2:  # Checks if name begins with the random letter
                place3_ans = places[num]
                # print("Name: " + place_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        place3_ans = "No Answer"
        # print ("No answer")
    return place3_ans


def place4():  # CPU generates a place

    places = [("Afghanistan"), ("Angola"), ("Antigua and Barbuda"), ("Argentina"),
              ("Armenia"), ("Azerbaijan"), ("Bahamas"), ("Bahrain"), ("Bangladesh"), ("Barbados"),
              ("Belarus"), ("Belize"), ("Benin"), ("Bhutan"), ("Bolivia"), ("Bosnia and Herzegovina"),
              ("Botswana"), ("Brunei"), ("Burkina Faso"), ("Burundi"), ("Cabo Verde"),
              ("Cambodia"),
              ("Cameroon"), ("Central African Republic"), ("Chad"), ("Chile"), ("Colombia"),
              ("Comoros"), ("Congo"), ("Costa Rica"), ("Cote d'Ivoire"), ("Croatia"), ("Cyprus"), ("Czechia"),
              ("Djibouti"), ("Dominica"), ("Dominican Republic"), ("Ecuador"), ("El Salvador"),
              ("Equatorial Guinea"), ("Eritrea"), ("Estonia"), ("Eswatini"), ("Ethiopia"), ("Fiji"), ("Finland"),
              ("Gabon"), ("Gambia"), ("Georgia"), ("Grenada"), ("Guatemala"), ("Guinea"),
              ("Guinea-Bissau"), ("Guyana"), ("Haiti"), ("Honduras"), ("Hungary"), ("Iceland"), ("Indonesia"),
              ("Iraq"), ("Ireland"), ("Israel"), ("Ivory Coast"), ("Jamaica"), ("Jordan"), ("Kazakhstan"),
              ("Kiribati"), ("Kuwait"), ("Kyrgyzstan"), ("Laos"), ("Latvia"), ("Lebanon"), ("Lesotho"),
              ("Liberia"), ("Libya"), ("Liechtenstein"), ("Lithuania"), ("Madagascar"), ("Malawi"), ("Malaysia"),
              ("Maldives"), ("Mali"), ("Malta"), ("Marshall Islands"), ("Mauritania"), ("Mauritius"), ("Mexico"),
              ("Micronesia"),
              ("Moldova"), ("Monaco"), ("Mongolia"), ("Montenegro"), ("Mozambique"), ("Myanmar"), ("Namibia"),
              ("Nauru"), ("Nepal"), ("Nicaragua"), ("Niger"), ("Nigeria"),
              ("North Macedonia"), ("Norway"), ("Oman"), ("Pakistan"), ("Palau"), ("Palestine"),
              ("Papua New Guinea"), ("Paraguay"), ("Philippines"), ("Qatar"), ("Romania"), ("Russia"),
              ("Rwanda"), ("Saint Lucia"), ("Saint Vincent and the Grenadines"), ("Samoa"), ("San Marino"),
              ("Sao Tome and Principe"), ("Saudi Arabia"), ("Senegal"), ("Seychelles"),
              ("Singapore"), ("Slovakia"), ("Slovenia"), ("Solomon Islands"), ("Somalia"),
              ("South Sudan"), ("Sri Lanka"), ("Sudan"), ("Suriname"), ("Sweden"), ("Syria"),
              ("Tajikistan"), ("Tanzania"), ("Thailand"), ("Timor-Leste"), ("Togo"), ("Tonga"),
              ("Trinidad and Tobago"),
              ("Tunisia"), ("Turkmenistan"), ("Tuvalu"), ("Uganda"), ("Ukraine"), ("United Arab Emirates"),
              ("Uruguay"), ("Uzbekistan"), ("Vanuatu"), ("Vatican City"), ("Yemen"), ("Zambia"), ("Zimbabwe")]

    i = random.randint(0, 11)  # Gets a random name for CPU's answering probability
    a = 0

    if i < 9:  # Checks if the CPU will generate an answer

        while a == 0:
            num = random.randint(0, len(places) - 1)  # random number in the range of the size of the tuple
            places2 = places[num]
            let2 = places2[0]

            if letter == let2:  # Checks if name begins with the random letter
                place4_ans = places[num]
                # print("Name: " + place_ans)
                a = 1
            else:
                a = 0

    else:  # CPU does not generate an answer
        place4_ans = "No Answer"
        # print ("No answer")
    return place4_ans


def game():
    global CPU_name
    input("Welcome to THE game. Press enter to continue ... ")
    system('cls')

    """SELECTING A LEVEL"""
    check = 0
    while (check == 0):
        numCPU = input("Would you like to play at level 1, 2 or 3? Answer: ")
        system('cls')
        if numCPU == "1":
            check = 1
        elif numCPU == "2":
            check = 1
        elif numCPU == "3":
            check = 1
        else:
            check = 0
    """DONE SELECTING A LEVEL"""

    print("The letter is: " + letter)
    user_name = input("Enter a name starting with the letter " + letter + ": ")
    user_place = input("Enter a country starting with the letter " + letter + ": ")
    print("Press enter to continue ... ")
    system('cls')

    if numCPU == "1":
        CPU_name = name1()  # Assigns a name for CPU 1
        CPU_place = place1()  # Assigns a place for CPU 1
        print("")
        print("CPU 1 ANSWERS:")
        print("Name: " + CPU_name)
        print("Place: " + CPU_place)

        CPU2_name = name2()  # Assigns a name for CPU 2
        CPU2_place = place2()  # Assigns a place for CPU 2
        print("")
        print("CPU 2 ANSWERS:")
        print("Name: " + CPU2_name)
        print("Place: " + CPU2_place)

    elif numCPU == "2":
        CPU_name = name1()  # Assigns a name for CPU 1
        CPU_place = place1()  # Assigns a place for CPU 1
        print("")
        print("CPU 1 ANSWERS:")
        print("Name: " + CPU_name)
        print("Place: " + CPU_place)

        CPU2_name = name2()  # Assigns a name for CPU 2
        CPU2_place = place2()  # Assigns a place for CPU 2
        print("")
        print("CPU 2 ANSWERS:")
        print("Name: " + CPU2_name)
        print("Place: " + CPU2_place)

        CPU3_name = name3()  # Assigns a name for CPU 3
        CPU3_place = place3()  # Assigns a place for CPU 3
        print("")
        print("CPU 3 ANSWERS:")
        print("Name: " + CPU3_name)
        print("Place: " + CPU3_place)

    elif numCPU == "3":
        CPU_name = name1()  # Assigns a name for CPU 1
        CPU_place = place1()  # Assigns a place for CPU 1
        print("")
        print("CPU 1 ANSWERS:")
        print("Name: " + CPU_name)
        print("Place: " + CPU_place)

        CPU2_name = name2()  # Assigns a name for CPU 2
        CPU2_place = place2()  # Assigns a place for CPU 2
        print("")
        print("CPU 2 ANSWERS:")
        print("Name: " + CPU2_name)
        print("Place: " + CPU2_place)

        CPU3_name = name3()  # Assigns a name for CPU 3
        CPU3_place = place3()  # Assigns a place for CPU 3
        print("")
        print("CPU 3 ANSWERS:")
        print("Name: " + CPU3_name)
        print("Place: " + CPU3_place)

        CPU4_name = name4()  # Assigns a name for CPU 4
        CPU4_place = place4()  # Assigns a place for CPU 4
        print("")
        print("CPU 4 ANSWERS:")
        print("Name: " + CPU4_name)
        print("Place: " + CPU4_place)

    """This code ensures that the language the user entered is valid"""
    if user_name[0].lower() != let:
        user_name = "No Answer"

    language = [("Afrikaans"), ("Albanian"), ("Amharic"), ("Arabic"), ("Aramaic"), ("Armenian"),
                ("Assamese"), ("Aymara"), ("Azerbaijani"), ("Bahasa"), ("Balochi"), ("Bamanankan"),
                ("Bashkort"), ("Bashkir"), ("Basque"), ("Belarusan"), ("Bengali"), ("Bhojpuri"), ("Bislama"),
                ("Bosnian"), ("Brahui"), ("Bulgarian"), ("Burmese"), ("Cantonese"), ("Catalan"), ("Cebuano"),
                ("Chechen"),
                ("Cherokee"), ("Chinese"), ("Croatian"), ("Czech"), ("Dakota"), ("Danish"), ("Dari"), ("Dholuo"),
                ("Dutch"),
                ("English"), ("Esperanto"), ("Estonian"), ("Éwé"), ("Finnish"), ("French"), ("Georgian"), ("German"),
                ("Gikuyu"),
                ("Greek"), ("Guarani"), ("Gujarati"), ("Haitian Creole"), ("Hausa"), ("Hawaiian"), ("Hawaiian Creole"),
                ("Hebrew"), ("Hiligaynon"), ("Hindi"), ("Hungarian"), ("Icelandic"), ("Igbo"), ("Ilocano"),
                ("Indonesian"),
                ("Inuit"), ("Inupiaq"), ("Irish"), ("Gaelic"), ("Italian"), ("Japanese"), ("Jarai"), ("Javanese"),
                ("K’iche’"),
                ("Kabyle"), ("Kannada"), ("Kashmiri"), ("Kazakh"), ("Khmer"), ("Khoekhoe"), ("Kinyarwanda"), ("Korean"),
                ("Kurdish"),
                ("Kyrgyz"), ("Lao"), ("Latin"), ("Latvian"), ("Lingala"), ("Lithuanian"), ("Macedonian"), ("Maithili"),
                ("Malagasy"),
                ("Malay"), ("Malayalam"), ("Mandarin"), ("Marathi"), ("Mende"), ("Mongolian"), ("Nahuatl"), ("Navajo"),
                ("Nepali"),
                ("Norwegian"), ("Ojibwa"), ("Oriya"), ("Oromo"), ("Pashto"), ("Persian"), ("Polish"), ("Portuguese"),
                ("Punjabi"),
                ("Quechua"), ("Romani"), ("Romanian"), ("Russian"), ("Samoan"), ("Sanskrit"), ("Serbian"), ("Shona"),
                ("Sindhi"),
                ("Sinhala"), ("Slovak"), ("Slovene"), ("Somali"), ("Spanish"), ("Swahili"), ("Swedish"), ("Tachelhit"),
                ("Tagalog"),
                ("Tajiki"), ("Tamil"), ("Tatar"), ("Telugu"), ("Thai"), ("Tibetan"), ("Tigrigna"), ("Tok Pisin"),
                ("Turkish"),
                ("Turkmen"), ("Ukrainian"), ("Urdu"), ("Uyghur"), ("Uzbek"), ("Vietnamese"), ("Warlpiri"), ("Welsh"),
                ("Wolof"),
                ("Xhosa"), ("Yakut"), ("Yiddish"), ("Yoruba"), ("Yucatec"), ("Zapotec"), ("Zulu")]

    """
    #user_language = input("Enter a language beginning with the letter " + letter + ": ")
    num = 0
    for i in range(0, len(language)):  # Ensure user input can be found in the
        if user_language.lower() == language[i].lower():
            # i = len(language) + 1
            num = 1
    if num == 0:  # If the input was not valid the users answer is converted to "No Answer"
        user_language = "No Answer"
    """

    places = [("Afghanistan"), ("Albania"), ("Algeria"), ("Andorra"), ("Angola"), ("Antigua and Barbuda"),
              ("Argentina"),
              ("Armenia"), ("Australia"), ("Austria"), ("Azerbaijan"), ("Bahamas"), ("Bahrain"), ("Bangladesh"),
              ("Barbados"),
              ("Belarus"), ("Belgium"), ("Belize"), ("Benin"), ("Bhutan"), ("Bolivia"), ("Bosnia and Herzegovina"),
              ("Botswana"), ("Brazil"), ("Brunei"), ("Bulgaria"), ("Burkina Faso"), ("Burundi"), ("Cabo Verde"),
              ("Cambodia"),
              ("Cameroon"), ("Canada"), ("Central African Republic"), ("Chad"), ("Chile"), ("China"), ("Colombia"),
              ("Comoros"), ("Congo"), ("Costa Rica"), ("Cote d'Ivoire"), ("Croatia"), ("Cuba"), ("Cyprus"), ("Czechia"),
              ("Denmark"), ("Djibouti"), ("Dominica"), ("Dominican Republic"), ("Ecuador"), ("Egypt"), ("El Salvador"),
              ("England"),
              ("Equatorial Guinea"), ("Eritrea"), ("Estonia"), ("Eswatini"), ("Ethiopia"), ("Fiji"), ("Finland"),
              ("France"),
              ("Gabon"), ("Gambia"), ("Georgia"), ("Germany"), ("Ghana"), ("Greece"), ("Grenada"), ("Guatemala"),
              ("Guinea"),
              ("Guinea-Bissau"), ("Guyana"), ("Haiti"), ("Honduras"), ("Hungary"), ("Iceland"), ("India"),
              ("Indonesia"),
              ("Iran"), ("Iraq"), ("Ireland"), ("Israel"), ("Italy"), ("Jamaica"), ("Japan"), ("Jordan"),
              ("Kazakhstan"),
              ("Kenya"), ("Kiribati"), ("Kosovo"), ("Kuwait"), ("Kyrgyzstan"), ("Laos"), ("Latvia"), ("Lebanon"),
              ("Lesotho"),
              ("Liberia"), ("Libya"), ("Liechtenstein"), ("Lithuania"), ("Luxembourg"), ("Madagascar"), ("Malawi"),
              ("Malaysia"),
              ("Maldives"), ("Mali"), ("Malta"), ("Marshall Islands"), ("Martinique"), ("Mauritania"), ("Mauritius"),
              ("Mexico"), ("Micronesia"),
              ("Moldova"), ("Monaco"), ("Mongolia"), ("Montenegro"), ("Montserrat"), ("Morocco"), ("Mozambique"),
              ("Myanmar"), ("Namibia"),
              ("Nauru"), ("Nepal"), ("Netherlands"), ("New Zealand"), ("Nicaragua"), ("Niger"), ("Nigeria"),
              ("North Korea"),
              ("North Macedonia"), ("Norway"), ("Oman"), ("Pakistan"), ("Palau"), ("Palestine"), ("Panama"),
              ("Papua New Guinea"),
              ("Paraguay"), ("Peru"), ("Philippines"), ("Poland"), ("Portugal"), ("Qatar"), ("Romania"), ("Russia"),
              ("Rwanda"),
              ("Saint Kitts and Nevis"), ("Saint Lucia"), ("Saint Vincent and the Grenadines"), ("Samoa"),
              ("San Marino"),
              ("Sao Tome and Principe"), ("Saudi Arabia"), ("Senegal"), ("Serbia"), ("Seychelles"), ("Sierra Leone"),
              ("Singapore"), ("Slovakia"), ("Slovenia"), ("Solomon Islands"), ("Somalia"), ("South Africa"),
              ("South Korea"),
              ("South Sudan"), ("Spain"), ("Sri Lanka"), ("Sudan"), ("Suriname"), ("Sweden"), ("Switzerland"),
              ("Syria"),
              ("Taiwan"), ("Tajikistan"), ("Tanzania"), ("Thailand"), ("Timor-Leste"), ("Togo"), ("Tonga"),
              ("Trinidad and Tobago"),
              ("Tunisia"), ("Turkey"), ("Turkmenistan"), ("Tuvalu"), ("Uganda"), ("Ukraine"), ("United Arab Emirates"),
              ("United Kingdom"), ("United States of America"), ("Uruguay"), ("Uzbekistan"), ("Vanuatu"),
              ("Vatican City"),
              ("Venezuela"), ("Vietnam"), ("Yemen"), ("Zambia"), ("Zimbabwe"), ("Ivory Coast"), ("America")]

    # user_places = input("Enter a country beginning with the letter " + letter + ": ")
    num = 0
    for i in range(0, len(places)):
        if user_place.lower() == places[i].lower():
            i = len(places) + 1
            num = 1
    if num == 0:
        user_place = "No Answer"
    """END OF VALIDATING USER'S ANSWER"""

    """CALCULATES THE SCORE FOR  LEVEL 1"""
    CPU = 0
    CPU2 = 0
    CPU3 = 0
    CPU4 = 0
    user = 0

    """Calculates score from name"""
    if CPU_name == user_name == CPU2_name:  # checks if they are all the same, that means no points given
        print("")


    elif CPU_name == "No Answer" and CPU2_name == "No Answer":
        user = user + 10

    elif CPU_name == "No Answer":  # checks if CPU 1 has an answer or not
        if CPU2_name == user_name:  # checks if CPU 2 and the user have the same answer
            CPU2 = CPU2 + 5
            user = user + 5
        else:  # here CPU 2 and the user are awarded points
            CPU2 = CPU2 + 10
            user = user + 10

    elif CPU2_name == "No Answer":  # checks if CPU 2 has no answer
        if CPU_name == user_name:  # checks if CPU 1 and the user have the same answer
            CPU = CPU + 5
            user = user + 5
        else:  # both CPU 1 and the user have unique answers
            CPU = CPU + 10
            user = user + 10
            """
            if user_name == "":
                user = user - 10
            """

    else:
        if user_name == CPU_name and CPU2_name != CPU_name:  # checks if user and the CPU 1 have the same answer
            CPU = CPU + 5
            CPU2 = CPU2 + 10
            user = user + 5

        elif user_name == CPU2_name and user_name != CPU_name:  # checks if user and the CPU 2 have the same answer
            CPU = CPU + 10
            CPU2 = CPU2 + 5
            user = user + 5
        elif CPU_name == CPU2_name and user_name != CPU_name:  # checks if CPU 1 and CPU 2 have the same answer
            CPU = CPU + 5
            CPU2 = CPU2 + 5
            user = user + 10
        else:  # this is where their answers are all unique
            CPU = CPU + 10
            CPU2 = CPU2 + 10
            user = user + 10


    """Calculates score from place"""
    if CPU_place.lower() == user_place and CPU2_place.lower() == user_place.lower():  # checks if they are all the same, that means no points given
        print("")

    elif CPU_place == "No Answer" and CPU2_place == "No Answer":
        user = user + 10

    elif CPU_place == "No Answer":  # checks if CPU 1 has an answer or not
        if CPU2_place.lower() == user_place.lower():  # checks if CPU 2 and the user have the same answer
            CPU2 = CPU2 + 5
            user = user + 5
        else:  # here CPU 2 and the user are awarded points
            CPU2 = CPU2 + 10
            user = user + 10

    elif CPU2_place == "No Answer":  # checks if CPU 2 has no answer
        if CPU_place.lower() == user_place.lower():  # checks if CPU 1 and the user have the same answer
            CPU = CPU + 5
            user = user + 5
        else:  # both CPU 1 and the user have unique answers
            CPU = CPU + 10
            user = user + 10
            """
            if user_name == "":
                user = user - 10
            """

    else:
        if user_place == CPU_place and CPU2_name != CPU_name:  # checks if user and the CPU 1 have the same answer
            CPU = CPU + 5
            CPU2 = CPU2 + 10
            user = user + 5

        elif user_place == CPU2_place and user_place != CPU_place:  # checks if user and the CPU 2 have the same answer
            CPU = CPU + 10
            CPU2 = CPU2 + 5
            user = user + 5
        elif CPU_place == CPU2_place and user_place != CPU_place:  # checks if CPU 1 and CPU 2 have the same answer
            CPU = CPU + 5
            CPU2 = CPU2 + 5
            user = user + 10
        else:  # this is where their answers are all unique
            CPU = CPU + 10
            CPU2 = CPU2 + 10
            user = user + 10

    if user_place == "No Answer":  # Ensures user enters a valid answer
        user = user - 10
    if user_name == "No Answer":
        user = user - 10

    print("")
    print("User Score: ", user)
    print("CPU 1 Score: ", CPU)
    print("CPU 2 Score: ", CPU2)
    print("")
    if user == CPU == CPU2:
        print("It's a tie!")

    elif user == CPU:
        if CPU2 > user:
            print("You Lose!")
            print("CPU 2 wins!")
        else:
            print("It's a tie!")
            print("You and CPU 1 win!")

    elif user == CPU2:
        if CPU > user:
            print("You Lose!")
            print("CPU 1 wins!")
        else:
            print("It's a tie!")
            print("You and CPU 2 win!")

    elif CPU == CPU2:
        if user > CPU:
            print("You win!")
        else:
            print("You Lose!")
            print("CPU 1 and 2 win!")

    elif user < CPU < CPU2:
        print("You Lose!")
        print("CPU 2 wins!")

    elif user < CPU2 < CPU:
        print("You Lose!")
        print("CPU 1 wins!")

    elif CPU < user < CPU2:
        print("You Lose!")
        print("CPU 2 wins!")

    elif CPU2 < user < CPU:
        print("You Lose!")
        print("CPU 1 wins!")

    elif CPU < CPU2 < user:
        print("You win!")

    elif CPU2 < CPU < user:
        print("You win!")

    print(user_name, user_place)


game()
print("")
input("Click enter to exit")
system("cls")
# begin.extend(int) #adds intermediate stuff to the beginners list

# give opportunity for computer to give no result, e.g. 1-30 names, if num 30- 35 no answer from compute.. do in loop
# make functions for begin, int and adv
