import os
import webbrowser
import time 

while True:
    version = input("서버 버전을 선택해주세요\n1.5.2~1.16.5 (1)\n1.17.1 (2)\n1.18.2~1.20.4 (3)\n1.20.5~1.21 (4)\n정수입력>")
    try:
        version = int(version)
        if version in [1, 2, 3]:
            if os.name == 'nt':
                os.system('cls')  
            else:
                os.system('clear') 

            break
        else:
            print("정확한 정수를 입력해주세요")
    except ValueError:
        print("정확한 정수를 입력해주세요")

while True:
    bukkit = input("사용할 버킷을 선택해주세요\nSpigot 중규모 서버에 추천 (1)\nPaper 대규모 서버 또는 최적화 필요 서버 추천 (2)\nCraftBukkit 소규모 서버 추천 (3)\n정수입력>")
    try:
        bukkit = int(bukkit)
        if bukkit in [1, 2, 3]:
            if os.name == 'nt':
                os.system('cls')  
            else:
                os.system('clear') 

            break
        else:
            print("정확한 정수를 입력해주세요")
    except ValueError:
        print("정확한 정수를 입력해주세요")

if version == 1:
    print("자바버전:","https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html\n")
    url = 'https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html'
    webbrowser.open(url)
elif version == 2:
    print("자바버전:","https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html\n")
    url1 = 'https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html'
    webbrowser.open(url1)
elif version == 3:
    print("자바버전:","https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html\n")
    url2 = 'https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html'
    webbrowser.open(url2)
elif version ==4:
    print("자바버전:","https://www.oracle.com/java/technologies/downloads/#java21\n")
    url3 = 'https://www.oracle.com/java/technologies/downloads/#java21'
    webbrowser.open(url3)

if bukkit == 1:
    print("버킷:","https://getbukkit.org/download/spigot")
    url4 = 'https://getbukkit.org/download/spigot'
    webbrowser.open(url4)
    print("위 링크에 들어가 다운 받아 주세요.(이 창은 15초 뒤에 꺼집니다.)")
    time.sleep(15)
    os.system(exit)
elif bukkit == 2:
    print("버킷:","https://papermc.io/downloads/all")
    url5 = 'https://papermc.io/downloads/all'
    webbrowser.open(url5)
    print("위 링크에 들어가 다운 받아 주세요.(이 창은 15초 뒤에 꺼집니다.)")
    time.sleep(15)
    os.system(exit)
elif bukkit == 3:
    print("버킷:","https://getbukkit.org/download/craftbukkit")
    url6 = 'https://getbukkit.org/download/craftbukkit'
    webbrowser.open(url6)
    print("위 링크에 들어가 다운 받아 주세요.(이 창은 15초 뒤에 꺼집니다.)")
    time.sleep(15)
    os.system(exit)
