from pynetwork import *
from pyautogui import press, typewrite, hotkey

def key_callback(name, ident, buffer):

    if buffer:
        keys = from_bytes(DataType.string, buffer)
        safe_print('keys:',keys)
        typewrite(keys)
    return True

def key_eos(name):
    safe_print('key_eos reached')

if __name__ == '__main__':

    gateway_ip =  '192.168.0.107'
    controller = Controller(gateway_ip= gateway_ip, port=3357)
    safe_print('trying to connect to gateway..')
    with controller.get_client() as client1:
        safe_print('waiting for key callbacks from gateway')
        client1.get_subroutine_stream(name= 'bulk_keys',\
                                      callback= key_callback,\
                                      eos_callback= key_eos)
        safe_print('client is clossing..')
    controller.close_gateway()
