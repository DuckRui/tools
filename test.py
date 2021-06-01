import struct

def main():

    li=[0x56,0x1e,0x01,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x03,'www',0x06,'google',0x03,'com',0x00,0x00,0x01,0x00,0x01] #待写入的数据
    with open("testfile","wb") as fp:
        for x in li:
            if isinstance(x,int):
                s = struct.pack('B',x)#转换为字节流字符串，B代表unsigned char
                fp.write(s)
            elif isinstance(x,str):
                fp.write(x.encode())
    return

if __name__ == '__main__':
    main()
