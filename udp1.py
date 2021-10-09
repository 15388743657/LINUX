import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('Bind UDP on 8088...')
while True:
      #接收数据                        
      addr,str1=s.recvfrom(1024)
      print('Received from %s:%s.'%str1)
      str2=str(str1,encoding='utf-8')
      print('I recieve a string is: ',str2)
      str3=str2.upper()
      s.sendto(str3.encode('utf-8'),str1)
s.close()
