import socket

def get_remote_machine_info():
    remote_host = 'bi.dufe.edu.cn'
    try:
        print ("IP address: %s" %socket.gethostbyname(remote_host))
    except socket.error:
        print("%s" %remote_host)

if __name__ == '__main__':
    get_remote_machine_info()