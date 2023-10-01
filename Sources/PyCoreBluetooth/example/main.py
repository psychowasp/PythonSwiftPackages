
#from kivy.app import App
from kivymd.app import MDApp

from kivy.lang import Builder

from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDRaisedButton, MDFlatButton

from kivymd.uix.dialog import MDDialog
from kivy.properties import ListProperty, ObjectProperty, StringProperty, DictProperty, NumericProperty

from kivy.clock import Clock

from ble_datamodel import BT_Manager, CBPeripheral



### UI ###
class BTDeviceIcon(MDRaisedButton):
    peripheral: CBPeripheral
    app: MDApp = ObjectProperty(None)
    label = StringProperty("")
    rssi = NumericProperty(0)

    def __init__(self, **kwargs):
        if "peripheral" in kwargs:
            peripheral = kwargs.pop("peripheral")
            self.rssi = kwargs.pop("rssi")
           
            self.peripheral = peripheral
            self.label = str(peripheral)


        super(BTDeviceIcon, self).__init__(**kwargs)
        self.dialog = None
    
    def on_connect(self, wid):
        bt: BT_Manager = self.app.bluetooth
        peripheral = self.peripheral
        peripheral.delegate = bt.current_device_data.delegate
        bt.manager.connect(peripheral)
        self.dialog.dismiss()

        Clock.schedule_interval(lambda dt: self.peripheral.readRSSI(), 5)
    
    def close_dialog(self, wid):
        self.dialog.dismiss()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text=f"Connect to {self.peripheral.name} ?",
                buttons=[
                    MDFlatButton(
                        text="Cancel",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Connect",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.on_connect
                    ),
                ],
            )
        self.dialog.open()

class BTDeviceMainView(MDBoxLayout): ...

class BTDeviceView(MDScrollView): ...

class BTDeviceList(MDList):

    app = ObjectProperty(None)
    devices: list[BTDeviceIcon] = []#ListProperty([])

    _devices: dict[int,BTDeviceIcon] = {}

    def on_peripheral(self, _, state: bool, peripheral: CBPeripheral, rssi: int):
        if state:

            _devices = self._devices
            key = hash(peripheral)
            if key in _devices:
                _devices[key].rssi = rssi
            else:
                icon = BTDeviceIcon(peripheral=peripheral, rssi=rssi)
                self.add_widget(icon)
                _devices[key] = icon
                
        # if state:

        #     #if peripheral.name: # if name is None dont add label
        #     icon = BTDeviceIcon(peripheral=peripheral)
        #     self.add_widget(icon)
        #     self.devices.append(icon)

        #     self._devices.append(BTDeviceIcon(peripheral=peripheral
        # else:
        #     for icon in self.devices:
        #         _peripheral = icon.peripheral
        #         if _peripheral.name == peripheral.name:
        #             self.remove_widget(icon)
        #             self.devices.remove(icon)
        #             return

    def on_app(self, wid, app):
        print("on_app", app)
        app.bluetooth.bind(on_peripheral=self.on_peripheral)
        
### KV ###
Builder.load_string("""
<BTDeviceIcon>:
    app: app
    text: f"{self.label} - rssi: {self.rssi}"
    font_size: dp(24)
    size_hint_y: None
    height: dp(48)
    on_press: self.show_alert_dialog()
    #padding: 16,16,16,16

<BTDeviceList>:
    app: app
    devices: app.bluetooth.periphals
    spacing: 8

<BTDeviceView>:
    BTDeviceList:
        id: bt_list
        
        #adaptive_height: True
        #md_bg_color: "black"#app.theme_cls.primary_color

<BTDeviceMainView>:
    orientation: "vertical"
    md_bg_color: "black"#app.theme_cls.primary_color
    
    MDBoxLayout:
        size_hint_y: None
        height: dp(104)
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                font_size: dp(24)
                text: app.bluetooth.current_device_data.current_label
                theme_text_color: "Custom"
                text_color: "red"
            MDProgressBar:
                size_hint_y: None
                height: dp(24)
                max: 100
                value: app.bluetooth.current_device_data.current_battery_level
            

    
        MDLabel:
            theme_text_color: "Custom"
            text_color: "red"
            font_size: dp(48)
            size_hint: 0.1, None
            text: str(app.bluetooth.current_device_data.current_rssi)

    
    MDScrollView:    
        BTDeviceList
            
""")



class MyApp(MDApp):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.bluetooth = BT_Manager(self)

    def build(self):
        return BTDeviceMainView()


if __name__ == '__main__':
    MyApp().run()