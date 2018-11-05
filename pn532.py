from microbit import *

def connect():
    i2c.init(100000)

def scan_i2c():
    return i2c.scan()

def wait_ack(pn532_addr):
    while True:
        data = i2c.read(pn532_addr, 12)
        ack = str(data).replace('\\x', ' ').replace("b'", '').strip()
        if ack[0:11] == '01 00 00 ff':
            if ack[0:20] == '01 00 00 ff 00 ff 00':                
                return True
            else:                
                return False
        sleep(200)	

def read(addr, leng=30):
    rbytes = i2c.read(addr, leng)
    result = str(rbytes).replace('\\x', ' ').replace("b'", '').strip()    
    if result[0:11] == '01 00 00 ff':
        return rbytes
    else:
        return False

def write(addr, cmd):
        i2c.write(addr, cmd)
        sleep(100)
        if wait_ack(addr):
            return True
        else:
            return False

def get_version(addr):
    cmd_version = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x02\xFE\xD4\x02\x2A')
    try:
        connect()
    except Exception:
        display.show('Check i2c line')
        return False
    if write(addr, cmd_version):
        return read(addr)
        
def config_pn532(addr):
    cmd_config = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x05\xFB\xD4\x14\x01\x02\x01\x14')
    if write(addr, cmd_config):
        return True
    else:
        return False

def wait_card(addr):
    if not config_pn532(addr):
        return False
    cmd_waitcard = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x04\xFC\xD4\x4A\x01\x00\xE1')
    if write(addr, cmd_waitcard):
        while True:
            result = read(addr, leng=100)
            if result:
                card_num = ''
                ll = result[13]
                st = 0
                while st < ll:
                    card_num += str('%02x' % result[14+st])
                    st = st + 1
                return card_num
            sleep(200)
    else:
        return False
