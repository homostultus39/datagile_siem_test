# Powershell - скрипт для мониторинга файлов с расширением .tmp в директории D:\Eltex\logs
## Принцип работы
В случае обнаружения данных файлов те удаляются с пометкой об удалении в журнале (C:\Users\Admin\Logs\clean.log)
Формат логирования:
```powershell
TimeStamp: “Eltex. Временные файлы очищены”
```
## Технологический стек:
- Powershell - создание автозапускаемого сервиса в рамках операционной системы, настройка Scheduler-а
- Python - взаимодействие с файловой системой, механизм проверки и удаления
## Руководство пользователя
Подтяните репозиторий к себе, это можно сделать следующей командой
```powershell
git clone https://github.com/homostultus39/datagile_siem_test.git
```
Выполните команды по созданию виртуального окружения и скачиванию всех библиотек
```powershell
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```
Далее откройте PowerShell, перейдите в директорию с проектом и введите следующую команду
```powershell
powershell.exe -ExecutionPolicy Bypass -File "<путь до ps-скрипта>"
```
