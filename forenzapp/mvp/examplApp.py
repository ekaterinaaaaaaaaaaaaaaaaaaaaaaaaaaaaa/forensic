import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
import design as design
from page_naming import *
import json
import shutil

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):  
        self.data = {}
        super().__init__()
        self.setupUi(self)  
        self.LoadDumpPage.clicked.connect(self.load_dump_navigate)
        self.WatchDumpPage.clicked.connect(self.watch_dump_navigate)
        self.CreateDumpPage.clicked.connect(self.create_dump_navigate)
        self.openFolderButton_2.clicked.connect(self.handle_open_folder_button)
        self.historyTreeWidget.itemClicked.connect(self.on_item_clicked)
        

    def create_dump_navigate(self):
        self.stackedWidget.setCurrentIndex(CREATE_PAGE)  

    def on_item_clicked(self, item, column):
        """Обработчик клика по элементу"""
        url = item.data(0, Qt.ItemDataRole.UserRole)
        if url:
            print("Клик по URL:", url)  # Проверяем, было ли клик по URL
            QDesktopServices.openUrl(QUrl(url))
        else:
            print("Клик по элементу без URL")

    def load_dump_navigate(self):
        self.stackedWidget.setCurrentIndex(DOWNLOAD_DUMP_PAGE)  

    def handle_open_folder_button(self):
        """
        Открывает диалоговое окно для выбора файла и сохраняет его в папку 'services'.
        """
        # Открываем диалоговое окно для выбора файла
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файлв"
        )

        if not file_path:
            QtWidgets.QMessageBox.information(self, "Отмена", "Файл не был выбран.")
            return

        # Папка назначения
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)  # Получаем родительский каталог
        services_dir = os.path.join(parent_dir, "services")

        # Проверяем, существует ли папка, если нет — создаем
        if not os.path.exists(services_dir):
            os.makedirs(services_dir)

        # Формируем путь для копии файла
        file_name = os.path.basename(file_path)  # Имя файла
        destination_path = os.path.join(services_dir, file_name)

        try:
            # Копируем файл
            shutil.copy(file_path, destination_path)
            QtWidgets.QMessageBox.information(
                self, "Успех", f"Файл сохранен в: {destination_path}"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить файл: {str(e)}"
            )

    def watch_dump_navigate(self):
        self.stackedWidget.setCurrentIndex(CHECK_DUMP_PAGE)  
        self.load_json_file("services/history.json")
        self.populate_browser_combo()
        self.browserComboBox.currentTextChanged.connect(self.load_history)
        self.load_history()

    def populate_browser_combo(self):
        """
        Заполняет ComboBox браузерами из данных JSON.
        """
        self.browserComboBox.clear()
        browsers = self.data.get("browsers", {}).keys()
        self.browserComboBox.addItems(browsers)

    def load_history(self):
    # Очищаем дерево
        self.historyTreeWidget.clear()

        # Получаем выбранный браузер
        browser = self.browserComboBox.currentText()
        if not browser:
            return

        # Загружаем данные для выбранного браузера
        browser_data = self.data["browsers"].get(browser, {})
        for date, times in browser_data.items():
            # Создаём родительский элемент для даты
            date_item = QTreeWidgetItem([date, ""])
            self.historyTreeWidget.addTopLevelItem(date_item)

            # Добавляем элементы времени, заголовка, URL и дополнительные данные
            for time, details in times.items():
                # Время
                time_item = QTreeWidgetItem([time, ""])
                date_item.addChild(time_item)

                # Вложенный блок Title и URL
                title_item = QTreeWidgetItem([f"Title, {details.get("title", "No Title")}"])
                url_item = QTreeWidgetItem([f"URL, {details.get("url", "No URL")}"])
                url_item.setData(0, Qt.ItemDataRole.UserRole, details.get("url", ""))
                time_item.addChild(title_item)
                time_item.addChild(url_item)

                # Добавляем Cookies
                cookies = details.get("cookies", [])
                if cookies:
                    cookies_item = QTreeWidgetItem(["Cookies", ""])
                    time_item.addChild(cookies_item)
                    for cookie in cookies:
                        cookie_item = QTreeWidgetItem([
                            f"Имя: {cookie['name']}, Значение: {cookie['value']}"
                        ])
                        cookies_item.addChild(cookie_item)

                # Cache
                cache = details.get("cache", {})
                if cache:
                    cache_item = QTreeWidgetItem(["Кэш", ""])
                    time_item.addChild(cache_item)

                    # Добавляем размер кэша
                    size_item = QTreeWidgetItem([f"Размер: {cache.get('size', 'Unknown')} KB"])
                    cache_item.addChild(size_item)

                    # Добавляем срок действия
                    expires_item = QTreeWidgetItem([f"Срок действия {cache.get('expires', 'Unknown')}"])
                    cache_item.addChild(expires_item)

    # Добавляем файлы из кэша
                    # Display cached files
                    files = cache.get("files", [])
                    if files:
                        files_item = QTreeWidgetItem(["Файлы", ""])
                        cache_item.addChild(files_item)
                        for file in files:
                            file_item = QTreeWidgetItem([f"URL, {file}"])
                            file_item.setData(0, Qt.ItemDataRole.UserRole, details.get("url", ""))
                            files_item.addChild(file_item)

    def load_json_file(self, file_path):
        """
        Загружает JSON данные из файла в переменную self.data.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
                print("JSON данные успешно загружены!")
        except FileNotFoundError:
            print(f"Ошибка: Файл {file_path} не найден.")
        except json.JSONDecodeError as e:
            print(f"Ошибка парсинга JSON: {e}")
