from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *
from bs4 import BeautifulSoup


def authorization(login, password): # Авторизация на сайте Сетевого города
    driver = webdriver.Chrome()
    driver.get('https://sgo1.edu71.ru') # Открыть браузер
    bt1 = driver.find_element(By.CLASS_NAME,"button").click()
    sleep(5)
    bt2 = driver.find_element(By.ID,'login').send_keys(login)
    bt3 = driver.find_element(By.ID,'password').send_keys(password)
    sleep(5)
    bt4 = driver.find_element(By.CSS_SELECTOR,"[class='plain-button plain-button_wide']").click()
    sleep(5)
    try:
        bt5 = driver.find_element(By.CSS_SELECTOR, "[title='Продолжить']").click()
        sleep(7)
        bt6 = driver.find_element(By.CSS_SELECTOR,
                                  "[ng-show='$ctrl.isVisible($ctrl.screenElementTypes.diary)']").click()
    except:
        sleep(5)
        bt6 = driver.find_element(By.CSS_SELECTOR,
                                  "[ng-show='$ctrl.isVisible($ctrl.screenElementTypes.diary)']").click()
    sleep(5)
    try:
        bt7 = driver.find_element(By.CSS_SELECTOR, "[class='subject ng-binding ng-scope']").click()
    except:
        sleep(5)
        bt8 = driver.find_element(By.CSS_SELECTOR, "[class='mdi mdi-arrow-left-bold']").click() #Last week
        sleep(5)
        bt7 = driver.find_element(By.CSS_SELECTOR, "[class='subject ng-binding ng-scope']").click()

    return [driver.page_source, driver]  # Получение HTML-страницы расписания и состояние браузера через переменную driver


def parse_1(page): # Разбор HTML-страницы и извлечение нужной информации
    soup = BeautifulSoup(page, 'html.parser')
    count = 0
    timetable = []
    t = []
    days = soup.find_all('tbody')
    for i in days:
        day = (''.join(i.text).split())
        day[0] = day[0].replace(',', '')
        if day[0] == 'Понедельник' or day[0] =='Вторник' or day[0] == 'Среда' or day[0] == 'Четверг' or day[0] =='Пятница' or day[0]  == 'Суббота':
            timetable.append(day)
    dict = {}
    tm_1 = {}
    days =[]
    for i in timetable:
        dict[i[0]]= elements(i)
    return dict


def elements(i): #Аххаха, оно зачем-то надо, и ладно...
    k = ''
    f = []
    x = len(i)-9
    for c in range(x):
        k = i[9+int(c)]
        f.append(k)
    return f


def sort(res): # Сортировка полученной информации путем разбиения на абзацы
    for day in res:
        for i in res[day]:
            if i in '1234567890':
                res[day][res[day].index(i)] = '  '+'\n'+i
            else:
                continue
    return res


def stop(driver):
    sleep(10)
    ex1 = driver.find_element(By.CSS_SELECTOR, "[title='Выход']").click()
    sleep(2)
    ex2 = driver.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']").click()
    sleep(2)
    driver.quit()


def start(login, password):
    list = authorization(login, password) #  Список с HTML-страницой рассписания и перменная driver со значением открытытого браузера
    page = list[0] # HTML-страница
    res1 = parse_1(page) # Разбор HTML-страницы и извлечение нужной информации
    res = sort(res1) # Сортировка полученной информации
    stop(list[1]) # Закрыть браузер
    return res # Отсоритрованный словарь с расписанием

