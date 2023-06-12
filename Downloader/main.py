import os
import time
import requests as r
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def start_telegraph(url):
    html = r.get(url).text
    src = html.split("src=\"")
    del(src[0])
    p_i = 1
    p_v = 1
    for link in src:
        temp = link.split("\"")[0]
        temp_type = ""
        temp_url  = url.replace(url.split("/")[-1], "") + temp
        folder = "photo"
        if ".png" in temp:
            temp_type = ".png"
        elif ".jpg" in temp:
            temp_type = ".jpg"
        elif ".mp4" in temp:
            temp_type = ".mp4"
            folder = "video"
        elif ".gif" in temp:
            temp_type = ".gif"
            folder = "video"
        elif ".js" in temp:
            continue
        print(temp_url)
        temp_r = r.get(temp_url)
        temp_index = p_i if folder == "photo" else p_v
        open(f'{url.split("/")[-1]}/{folder}/{temp_index}{temp_type}', 'wb').write(temp_r.content)
        if folder == "video":
            p_v += 1
        elif folder == "photo":
            p_i += 1


def start_links(links):
    path = 'saved_' + links[0].split("/")[-1].replace("\n", "")
    try:
        os.mkdir(path)
        os.mkdir(f"{path}/photo")
        os.mkdir(f"{path}/video")
    except:
        pass
    i = 0
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    h  = {'User-Agent': ua,}
    for link in links:
        if link:
            print(link)
            temp = link.split("/")[-1]
            try:
                name = temp.split('.')[0]
            except:
                name = str(i)
            temp_type = ""
            folder = "photo"
            if ".png" in temp:
                temp_type = ".png"
            elif ".jpg" in temp:
                temp_type = ".jpg"
            elif ".mp4" in temp:
                temp_type = ".mp4"
                folder = "video"
            elif ".gif" in temp:
                temp_type = ".gif"
                folder = "video"
            elif ".js" in temp:
                continue
            try:
                chrome_options = Options()
                # chrome_options.add_argument("--headless")
                browser=webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
                browser.get(link)
                time.sleep(5)
                # html = browser.page_source
                # print(html)
                # time.sleep(10)
                # open(f'{path}/{folder}/{name}{temp_type}', 'wb').write(html)
                # temp_r = r.get(link)
                # browser.save_screenshot(f'{path}/{folder}/{name}{temp_type}')
                
                open(f'{path}/{folder}/{name}{temp_type}', 'wb').write(browser.find_element('xpath', '/html/body/img').screenshot_as_png)
                browser.quit()
                i += 1
            except Exception as e:
                print(e)
                print('Ссылки нету! ' + link)
            # return

if __name__ == "__main__":
    print('''Введите режим работы:
[1] - По ссылке телеграфа
[2] - По ссылкам из файла links.txt
    ''')
    try:
        mode = int(input('Введите число в []: '))
    except:
        exit('Error')

    if mode == 1:
        url = input("Введите ссылку: ")
        path = url.split("/")[-1]
        try:
            os.mkdir(path)
            os.mkdir(f"{path}/photo")
            os.mkdir(f"{path}/video")
        except:
            pass
        start_telegraph(url)
        input()
    elif mode == 2:
        try:
            links = open('links.txt', 'r', encoding='utf8').readlines()
        except:
            exit('Ошибка при открытии файла links.txt! Проверьте, есть ли он в папке скрипта')
        if not links:
            exit('Файл links.txt - пуст! Заполниите его')
        print('Начинаем скачивать...')
        start_links(links)
        print('Готово!')
        input()
    else:
        exit('Error')
