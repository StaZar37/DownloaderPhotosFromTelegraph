Скрипт для скачивания фото и видео с telegra.ph

Есть два режима
1. По одной ссылке telegra.ph
2. По многим ссылкам telegra.ph из файла links.txt - НА НОВЫХ ВЕРСИЯХ SELENIUM НЕ РАБОТАЕТ! НУЖНО ПЕРЕПИСАТЬ НЕКОТОРЫЕ ФУНКЦИИ

Принцип работы
1. Создаётся эмулятор браузера (python selenium) и заходит на страницу телеграфа
2. Извлекается html код и далее из него извлекаются ссылки на фото и видео
3. Далее с помощью HTTP запросов (python requests) скрипт проходит по каждой ссылки на фото и видео
4. И всё скачивается в папку с названием ссылки (title страницы telegra.ph)




Используется эмулятор Google Chrome. По этому нужно следить чтобы версия chromedriver.exe подходила к версии вашего Chrome
Для скачивания Вам нужной версии нужно перейти на этот сайт https://chromedriver.chromium.org/downloads
И заменить файл в корневой папке

--------------------------------------------------------------------------------------

Script for downloading photos and videos from telegra.ph

There are two modes
1. One link telegra.ph
2. For many telegra.ph links from the links.txt file - ON NEW VERSIONS SELENIUM DOES NOT WORK! NEED TO REWRITE SOME FUNCTIONS

Principle of operation
1. A browser emulator is created (python selenium) and enters the telegraph page
2. The html code is extracted and then links to photos and videos are extracted from it
3. Next, using HTTP requests (python requests), the script goes through each link to the photo and video
4. And everything is downloaded to a folder with the name of the link (telegra.ph page title)

The Google Chrome emulator is used. Therefore, you need to make sure that the version of chromedriver.exe is suitable for the version of your Chrome
To download the version you need, go to this site https://chromedriver.chromium.org/downloads
And replace the file in the root folder