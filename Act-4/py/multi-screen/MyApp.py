# SCREEN MANAGER PY
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class MainScreen(Screen):
    pass

class ListScreen(Screen):
    def select_item(self, item_name):
        self.manager.get_screen("detail").item_name = item_name
        self.manager.current = "detail"

class DetailScreen(Screen):
    item_name = StringProperty("")
    def go_back(self):
        self.manager.current = "list"

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(ListScreen(name="list"))
        sm.add_widget(DetailScreen(name="detail"))
        return sm

if __name__ == "__main__":
    MyApp().run()