import os
import time
import pyautogui
import psutil
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def find_and_terminate_process(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process_name in proc.info['name']:
            proc.terminate()


def common():
    current_user = os.getlogin()
    file_path = rf'C:\Users\{current_user}\Desktop\banana.url'
    os.startfile(r'ac.exe')
    print("PreStart | Запуск AutoClicker..")
    time.sleep(1)
    pyautogui.moveTo(1080, 411)
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.moveTo(1080, 411)
    pyautogui.mouseUp(button='left')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('1')
    print("Processing... ¦ Пишем 1 в окне Milisecounds")

    ###Click 1070 350
    pyautogui.moveTo(1070, 350)
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.moveTo(1070, 350)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(1070, 350)
    os.startfile(file_path)
    print("PreStart | Ожидаем запуск Banana...")
    pyautogui.moveTo(884, 612)
    time.sleep(9)
    print(Fore.BLUE + "Clicker | HotKey нажат!")
    pyautogui.press('f6')
    print("Processing...| Осталось 2 мин. 30 секунд")
    time.sleep(30)
    print("Processing...| Осталось 2 мин. 0 секунд")
    time.sleep(30)
    print("Processing...| Осталось 1 мин. 30 секунд")
    time.sleep(30)
    print("Processing...| Осталось 1 мин. 0 секунд")
    time.sleep(30)
    print("Processing...| Осталось 0 мин. 30 секунд")
    time.sleep(20)
    print("Processing...| Осталось 0 мин. 10 секунд")
    time.sleep(5)
    print("Processing...| Осталось 0 мин. 5 секунд")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 4 секунды")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 3 секунды")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 2 секунды")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 1 секунда")
    print(Fore.YELLOW + "Done | Программа завершенна! Бананы полученны, запустите программу через 3 часа")
    pyautogui.press('f6')
    print(Fore.BLUE + "Clicker | HotKey Выключен!")
    print("Done | Закрываем Banana и AutoClicker")  
    find_and_terminate_process("ac")
    find_and_terminate_process("Banana")

def rare():
    current_user = os.getlogin()
    file_path = rf'C:\Users\{current_user}\Desktop\banana.url'
    os.startfile(r'ac.exe')
    print("PreStart | Запуск AutoClicker..")
    time.sleep(1)
    pyautogui.moveTo(1080, 411)
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.moveTo(1080, 411)
    pyautogui.mouseUp(button='left')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write('1')
    print("Processing... ¦ Пишем 1 в окне Milisecounds")

    ###Click 1070 350
    pyautogui.moveTo(1070, 350)
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.moveTo(1070, 350)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(1070, 350)
    os.startfile(file_path)
    print("PreStart | Ожидаем запуск Banana...")
    pyautogui.moveTo(884, 612)
    time.sleep(9)
    print(Fore.BLUE + "Clicker | HotKey нажат!")
    pyautogui.press('f6')
    print("Processing...| Осталось 35 мин. 30 секунд")
    time.sleep(630)
    print("Processing...| Осталось 25 мин. 0 секунд")
    time.sleep(900)
    print("Processing...| Осталось 10 мин. 0 секунд")
    time.sleep(60)
    print("Processing...| Осталось 9 мин. 0 секунд")
    time.sleep(60)
    print("Processing...| Осталось 8 мин. 0 секунд")
    time.sleep(60)
    print("Processing...| Осталось 7 мин. 0 секунд")
    time.sleep(60)
    print("Processing...| Осталось 6 мин. 0 секунд")
    time.sleep(60)
    print("Processing...| Осталось 5 мин. 0 секунды")
    time.sleep(60)
    print("Processing...| Осталось 4 мин. 0 секунды")
    time.sleep(60)
    print("Processing...| Осталось 3 мин. 0 секунды")
    time.sleep(60)
    print("Processing...| Осталось 2 мин. 0 секунда")
    time.sleep(60)
    print("Processing...| Осталось 1 мин. 0 секунда")
    time.sleep(30)
    print("Processing...| Осталось 0 мин. 30 секунда")
    time.sleep(20)
    print("Processing...| Осталось 0 мин. 10 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 9 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 8 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 7 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 6 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 5 секунда")
    time.sleep(1)
    print("Processing...| Осталось 0 мин. 4 секунда")
    time.sleep(1)
    print(FORE.RED + "Processing...| Осталось 0 мин. 3 секунда")
    time.sleep(1)
    print(Fore.GREEN + "Processing...| Осталось 0 мин. 2 секунда")
    time.sleep(1)
    print(Fore.BLUE + "Processing...| Осталось 0 мин. 1 секунда")
    print(" ")
    print(Fore.YELLOW + "Done | Программа завершенна! Бананы полученны, запустите программу через 3 часа")
    pyautogui.press('f6')
    print(Fore.BLUE + "Clicker | HotKey Выключен!")
    print("Done | Закрываем Banana и AutoClicker")  
    find_and_terminate_process("ac")
    find_and_terminate_process("Banana")

print(Fore.YELLOW + r""""

██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗░█████╗░  
██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░██║██╔══██╗  
██████╦╝███████║██╔██╗██║███████║██╔██╗██║███████║  
██╔══██╗██╔══██║██║╚████║██╔══██║██║╚████║██╔══██║  
██████╦╝██║░░██║██║░╚███║██║░░██║██║░╚███║██║░░██║  
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  

░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
print(" ")
print(Fore.RED + "Autor - t.me/good2999k")
print(" ")
games = int(input(Fore.BLUE + "PreStart | Сколько раз должна запуститься программа: "))
print(" ")
print("PreStart | 1 - common, обычный, время ожидания 2 мин. 30 сек")
print("PreStart | 2 - rare, редкий, время ожидания 35 мин. 30 сек")
timeR = input(Fore.RED + "PreStart | Какой банан вы хотите: ")
if timeR == "1":
    for _ in range(games):
        common()
elif timeR == "2":
    for _ in range(games):
        rare()
print(r"""
░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░

░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝""")
time.sleep(180)
