from pynetwork import *

def send_key_stream():

    keys = ''
    while '?exit' not in keys.lower():
        keys = input('Enter keys to send=')
        yield  0, to_bytes(DataType.string, keys)
    yield -1, None

if __name__ =='__main__':

    gw = Gateway(port= 3357)
    gw.add_subroutine(name = 'bulk_keys', subroutine= send_key_stream)
    gw.start(blocking= True)


