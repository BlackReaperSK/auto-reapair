#include <stdio.h>  
#include <stdlib.h>
#include <string.h> 
#include <unistd.h> 

// Verifica o comando fastboot 
int Retorno_Verf(void){
    FILE *cmd = popen("fastboot -help", "r");
    int retorno;
    char str_detect[6] = "--help";
    char result[500]={0x0};

    while (fgets(result, sizeof(result), cmd) !=NULL)
    system("clear");
    retorno = strncmp(result, str_detect, 6);
    return retorno;
}

// Instalando Ou Verificando ADB-TOOLS
int LookAndInstall(void){

    if (Retorno_Verf() > -15){
        printf("[V] ADB-Tools já instalado....\n");
        return 0;
    }
    else
        printf("[V] Instalando ADB-Tools e suas dependencias...\n");
        sleep(3);
        system("sudo apt install android-tools-adb;sudo apt install android-tools-fastboot");
        system("clear");
        printf("[V] Verificando Instalação.....\n");
        if (Retorno_Verf() > -15){
            printf("[ADB-Tools] Instalado com exito!\n");
            sleep(1.5);
            return 0;
        }
        else{
            printf("[X] Ocorreu um erro.\n");
            exit(0);
        }
}


// Olhando para o comando de dispositivos
int Devices_Look(){

    FILE *cmd = popen("fastboot devices", "r");
    char str_detect[6] = "0000";
    int retorno;
    char result[500]={0x0};
    while (fgets(result, sizeof(result), cmd) !=NULL)
    sleep(0.5);
    retorno = strncmp(result, str_detect, 6);
    return retorno;
}

// Detectando dispositivos conectados
int Detect(){
    if (Devices_Look() > 1){
        printf("[V] Dispositivo Detectado!\n");     
       return 1;
    } else {
        printf("[X] Por favor, conecte seu dispositivo em modo Fastboot.\n");
        while(Devices_Look() < 0){
            if (Devices_Look() > 0){
                break;
            }
        }
        printf("[V] Dispositivo Detectado!\n");
    }
}

// Instalando a rom
// (Certifique-se de que está sendo executado na mesma pasta em que a rom descompactada se localiza)
int Install(){
    Detect();
    printf("[V] Instalando ROM.....\n");
    printf("[|] Tenha certeza que o script está na mesma pasta que a ROM.....\n");    
    sleep(4.5);
    system("fastboot oem fb_ mode_set");
    sleep(2); // Previnir Erros.
    system("fastboot flash partition gpt.bin");
    system("fastboot flash bootloader bootloader.img");
    system("fastboot flash logo logo.bin");
    system("fastboot flash boot boot.img");
    system("fastboot flash recovery recovery.img");
    system("fastboot flash dsp adspso.bin");
    system("fastboot flash oem oem.img");
    int a = 0;
    while (a <= 11){
        char comando[70];
        char string[50] = "fastboot flash system system.img_sparsechunk.";
        sprintf(comando,"%s%d", string, a);
        system(comando);
        a += 1; 
    }
    sleep(1); // Previnir Erros.
    system("fastboot flash modem NON-HLOS.bin");
    system("fastboot erase modemst1");
    system("fastboot erase modemst2");
    system("fastboot flash fsg fsg.mbn");
    system("fastboot erase cache");
    system("fastboot erase userdata");
    system("fastboot erase customize");
    system("fastboot erase clogo");
    system("fastboot oem fb_mode_clear");
    system("fastboot flash logo logo.bin");
    system("fastboot reboot");
    system("clear");
    printf("[V] Reiniciando dispositivo....\n");
    sleep(4); // Previnir do script atrapalhar o reboot
    printf("[V] ROM instalada com sucesso!\n");
}

// Func Main, inicia todo o processo.
int main(void){
    LookAndInstall();
    Install();
    return 0;
}


// By BlackReaper.
