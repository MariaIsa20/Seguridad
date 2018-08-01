from selenium import webdriver

# lectura del documento donde estan los datos
archivo = open("data.txt","r")
datos = archivo.readlines()

datos[0] = datos[0].split()[0]
usuario = datos[0]
password = datos[1]

#print(usuario,password)

# driver 
browser = webdriver.Chrome('C:/Users/isabel.vanegas/Downloads/chromedriver_win32/chromedriver.exe')
browser.get('http://www.wechall.net')

# entrada del username
userbox = browser.find_element_by_name('username')
userbox.send_keys(usuario)

# entrada del password
passbox = browser.find_element_by_name('password')
passbox.send_keys(password)

# click login
loginbutton = browser.find_element_by_name('login')
loginbutton.click()

# texto
#texto = browser.find_element_by_class_name('box_c')
texto = browser.find_element_by_xpath('//*[@id="page"]/div[2]/div')
print(texto.text)

# cerrar el archivo y el navegador
archivo.close()
browser.close()


