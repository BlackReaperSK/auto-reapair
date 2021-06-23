from requests import get,post;import os;from time import sleep;import json
comando = os.system

#Instalando Ou Verificando ADB-TOOLS

def LookAndInstall():
    try:
        fastboot = os.popen('fastboot -help').readlines(); fastboot[0]
        print('[V] ADB-Tools already installed....')
    except:
        try:
            print('[V] Installing ADB-Tools and our dependencies...')
            sleep(1.5)
            comando('sudo apt install android-tools-adb;sudo apt install android-tools-fastboot')
            fastboot = os.popen('fastboot -help').readlines(); fastboot[0]
            comando('clear')
            print("[ADB-Tools] Successfully installed!")   
        except:
            print("[X] An error occurred installing ADB-Tools, try again")
            exit()


#Achando a ROM para o dispositivo

def FindRom(dispositivo):
    dispositivo = dispositivo.upper()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = '{"action":"get","search":{"href":"/firmware/","pattern":"'+ dispositivo +'","ignorecase":true}}'
    req = post('https://mirrors.lolinet.com/firmware/?', headers=headers, data=data)
    a = json.loads(req.text)
    txt_brt = a['search']
    for versao in txt_brt:
        ultima_versao = versao
    arquivo_para_baixar = ultima_versao['href']
    arquivo = arquivo_para_baixar.split(f"{dispositivo}",1)[1];arquivo = dispositivo + arquivo
    try:
        comando(f'sudo wget https://mirrors.lolinet.com{arquivo_para_baixar}')
        diretorio_arquivo = arquivo.replace('.zip', '')
        comando(f'sudo unzip {arquivo}; cd {diretorio_arquivo}')
        print('[V] ROM successfully downloaded and uncompressed!')
        sleep(0.5)
    except:
        print('[X] An error occurred while downloading/decompressing the ROM')
        exit()
    

#Detectando e instalando 

def Detect_And_Install():
    try:
        fastboot = os.popen('fastboot devices').readlines()
    except:
        print('[X] There was an error in the installation process, try again')
    if 'fastboot' in fastboot:
        a = 0
        os.system('clear')
        print("[V] Aparelho Detectado!")
        print('[V] Inserindo a rom....')
        sleep(2)
        comando('fastboot oem fb_mode_set')
        sleep(0.3)
        comando('fastboot flash partition gpt.bin')
        comando('fastboot flash bootloader bootloader.img')
        comando('fastboot flash logo logo.bin')
        comando('fastboot flash boot boot.img')
        comando('fastboot flash recovery recovery.img')
        comando('fastboot flash dsp adspso.bin')
        comando('fastboot flash oem oem.img')
        while a <= 11:
            comando(f'fastboot flash system system.img_sparsechunk.{a}')
            a += 1
        comando('fastboot flash modem NON-HLOS.bin')
        comando('fastboot erase modemst1')
        comando('fastboot erase modemst2')
        comando('fastboot flash fsg fsg.mbn')
        comando('fastboot erase cache ')
        comando('fastboot erase userdata')
        comando('fastboot erase customize')
        comando('fastboot erase clogo')
        comando('fastboot oem fb_mode_clear')
        comando('fastboot flash logo logo.bin')
        comando('fastboot reboot')
        comando('clear')
        print('[V] Restarting device....')
        sleep(3)
        print('[V] ROM successfully installed!')
    else:
        print("[X] Please connect your device in FastBoot mode.")
        exit()


#Func Main

def Main():
    LookAndInstall()
    q = input('[|] Do you want to download an appropriate ROM for your device? [Y/N]: ')
    if 'Y' in q or 'y' in q:
        try:
            dispositivo = input('[V] Please, enter your device: ')
            FindRom(str(dispositivo))
            Detect_And_Install()
        except:
            print('Error.')
    elif 'N' in q or 'n' in q:
        Detect_And_Install()
    else:
        print('[X] Just answer with Y or N')
Main()
