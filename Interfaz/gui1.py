# -*- encoding:utf-8 -*-

# IMPORTAR LIBRERIAS
import os
import serial
import time
import signal
from gi.repository import Gtk
import threading

# Conectarse con Arduino
try:
    usbport = '/dev/ttyACM0'
except:
    usbport = '/dev/ttyACM1'  # TODO: Corregir error de Comunicación

# Set up serial baud rate
ser = serial.Serial(usbport, 9600, timeout=1)


# Enviar datos de movimiento de servo a Arduino
def move(servo, angle):
    if (0 <= angle <= 180):
        ser.write(chr(255))
        ser.write(chr(servo))
        ser.write(chr(angle))
    else:
        print('El ángulo del Servo debe ser un entero entre 0 y 180.\n')


# Inicializar Programa
def init():
    print('Posicionando servos...')
    move(1, 90)
    move(2, 90)
    # TODO: Definir movimiento inicial para los 6 servos


# ------------ INTERFAZ GRÁFICA ------------
class UI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.getcwd(), 'gui.ui'))
        self.window = self.builder.get_object('window1')
        self.lblEstado = self.builder.get_object('lblEstado')
        self.btnOn = self.builder.get_object('btnOn')
        self.btnOff = self.builder.get_object('btnOff')

        self.window.connect('delete-event', self.quit)
        self.btnOff.connect('clicked', self.apagarServo)
        self.btnOn.connect('clicked', self.encenderServo)
        self.window.show()

    # Botón Encender Servo
    def encenderServo(self, button):
            self.lblEstado.set_text("testing")  # Setear texto a Label
            print("En encenderServo")
            servoOn()

    # Botón apagar Servo
    def apagarServo(self, button):
        print('Volviendo a posición inicial...')
        servoOff()

    # Salir de Interfaz
    def quit(self, *args):
        Gtk.main_quit()


# Declaración de funciones asignadas a acciones de los servos
def servoOn():
    move(1, 80)
    print("En servo On")
    a = 0
    while a < 180:
        move(1, a)
        a = a + 10
        time.sleep(.5)


def servoOff():
    print("En servo Off")

# Multithreading
threads = list()

t = threading.Thread(target=servoOn())
threads.append(t)
t.start()

a = threading.Thread(target=servoOff())
threads.append(a)
a.start()


# Lanzar GUI
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    init()
    ui = UI()
    Gtk.main()
