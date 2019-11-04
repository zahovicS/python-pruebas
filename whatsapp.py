from selenium import webdriver
from time import sleep
import sys
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

#funciones
def enviar_Mensaje(msg,c):
    for i in range(c):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        print("Listo :)")

def enviar_Multimedia(btnAd,r,c):
    for i in range(c):
        btnAd.click()
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(r)
        sleep(8)
        btnEnviar=driver.find_element_by_xpath('//span[@data-icon="send-light"]')
        btnEnviar.click()
#funciones -- end  

print('¿Qué desea hacer?')
print('1 = Enviar un mensaje a una persona o grupo.\n2 = Enviar una imagen o un video.')
opcion=int(input())
nombre = input('Ingrese el nombre de usuario o el nombre del grupo: ')

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(nombre))
user.click()
if ojo =="si":
    if opcion == 1:
        #enviar un mensaje
        print('=== Haz elegido enviar un mensaje ===')
        mensaje = input('Ingrese el mensaje: ')
        count = int(input('Ingrese el numero de mensajes a enviar: '))
        msg_box = driver.find_element_by_class_name('_13mgZ')
        input('presione Enter despues de escanear el codigo QR')
        enviar_Mensaje(mensaje,count)
        
    elif opcion ==2:
        #enviar un archivo
        print('=== Haz elegido enviar un archivo de imagen/video ===')
        rutaArchivo = input('Ingrese la ruta del archivo a enviar(imagenes/video): ')
        count = int(input('Ingrese el numero de veces a enviar: '))
        btnAdjuntar = driver.find_element_by_xpath('//div[@title="Adjuntar"]')
        input('presione Enter despues de escanear el codigo QR')
        enviar_Multimedia(btnAdjuntar,rutaArchivo,count)
    else:
        Print('Error :(')
        sys.exit()
else:
    Print('Error :(')
