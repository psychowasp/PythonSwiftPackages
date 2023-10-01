from corebluetooth import CBCentralManager, CBPeripheral, CBService, CBUUID
from corebluetooth import PyCBPeripheralDelegate, CBL2CAPChannel, CBCharacteristic, CBDescriptor

from kivy.event import EventDispatcher,Observable
from kivy.properties import ListProperty, NumericProperty, StringProperty, ObjectProperty
from typing import Optional

from threading import current_thread
# get the main thread


class CBDeviceDataModel(EventDispatcher):
    
    

    delegate: PyCBPeripheralDelegate # wrap of class in swift that has CBPeripheralDelegate
    current_battery_level = NumericProperty(0)
    current_label = StringProperty('')
    current_rssi = NumericProperty(0)
    

    def __init__(self) -> None:
        super(CBDeviceDataModel, self).__init__()
        
        self.delegate = PyCBPeripheralDelegate(self)
        
    


    def didDiscoverServices(self, peripheral: CBPeripheral, error: Optional[str]):
        for service in peripheral.services:
            uuid = service.uuid
            service_name = str(uuid) # uses the __str__ from the swift class (.description)
            print(service_name)
            if service_name == "Battery":
                print(f"didDiscoverServices: {service_name} / {uuid.uuidString}")
                peripheral.discoverCharacteristics(None,service)

    def didDiscoverCharacteristics(self, peripheral: CBPeripheral, service: CBService, error: Optional[str]):
        #called when device asks for services
        characteristics = service.characteristics
        #print(f"didDiscoverCharacteristics:", characteristics)

        for characteristic in characteristics:
            peripheral.setNotifyValue(True, characteristic)
            peripheral.readCharacteristic(characteristic)


    def didUpdateValueForCharacteristic(self, peripheral: CBPeripheral, characteristic: CBCharacteristic, error: Optional[str]):
        value: bytes = characteristic.value
        if value:
            self.current_battery_level = value[0]
            self.current_label = f"{peripheral.name}'s battery level is {value[0]}%"
            print(self.current_label)

    def peripheralDidUpdateName(self, peripheral: CBPeripheral):
        ...

    def peripheralIsReady(self, peripheral: CBPeripheral):
        ...

    def didDiscoverDescriptors(self, peripheral: CBPeripheral, characteristic: CBCharacteristic, error: Optional[str]):
        ...

    def didDiscoverIncludedServices(self, peripheral: CBPeripheral, service: CBService, error: Optional[str]):
        ...

    def didReadRSSI(self, peripheral: CBPeripheral, RSSI: int, error: Optional[str]):
        print("didReadRSSI", peripheral.name, RSSI)
        self.current_rssi = RSSI
        


    def didOpenChannel(self, peripheral: CBPeripheral, channel: Optional[CBL2CAPChannel], error: Optional[str]):
        ...

    def didModifyServices(self, peripheral: CBPeripheral, invalidatedServices: list[CBService]):
        ...

    def didUpdateNotificationState(self, peripheral: CBPeripheral, characteristic: CBCharacteristic, error: Optional[str]):
        print("didUpdateNotificationState", characteristic)

    def didWriteValueForCharacteristic(self, peripheral: CBPeripheral, characteristic: CBCharacteristic, error: Optional[str]):
        ...

    def didWriteValueForDescriptor(self, peripheral: CBPeripheral, descriptor: CBDescriptor, error: Optional[str]):
        ...

    def didUpdateValueForDescriptor(self, peripheral: CBPeripheral, descriptor: CBDescriptor, error: Optional[str]):
        print("didUpdateValueForDescriptor", descriptor)

    
class BT_Manager(EventDispatcher):

    manager: CBCentralManager
    current_device_data: CBDeviceDataModel
    periphals: list[CBPeripheral] = ListProperty([])

    __events__ = ["on_peripheral"]

    #new_peripheral: CBPeripheral = ObjectProperty(None)
    
    def __init__(self, app) -> None:
        super(BT_Manager, self).__init__()
        self.app = app
        manager = CBCentralManager()
        self.manager = manager
        manager.py_callback = self
        self.current_device_data = CBDeviceDataModel()

    #callback


    def didDiscover(self, peripheral: CBPeripheral, rssi: int):
        self.dispatch("on_peripheral",True,peripheral,rssi)

    #callback
    def remove_peripheral(self, peripheral: CBPeripheral):
        #print("remove_peripheral", peripheral.name)
        self.dispatch("on_peripheral",False,peripheral, 0)
    
    #callback

    def did_connect(self, peripheral: CBPeripheral):
        peripheral.discoverServices(None)


    def connect_status(self, status: bool):
        print("connect_status",status)

    def on_peripheral(self,wid,peripheral,rssi): ...
    