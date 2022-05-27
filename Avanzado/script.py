import glob
import os
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import re

NOMBRE_ARCHIVO = "Sorpresa.txt"


def get_user_path():
    return "{}\\".format(Path.home())


def delay_action(option=2):
    if option == 1:
        sleep(randrange(1, 4)) #* randrange(1, 60) * 2)  # Esto da un tiempo de dormir en segundos
    else:
        sleep(5)


def create_file(desktop_path):
    file = open(desktop_path + NOMBRE_ARCHIVO, "w")
    file.write("Buenas he entrado en tu ordenador y voy a echar un vistazo, no tengas miedo no voy a hacer nada malo... \n")
    return file


def get_chrome_history(history_path):
    urls = None
    while not urls:
        try:
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            # cursor.execute("")
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC LIMIT 100")
            urls = cursor.fetchall()
            return urls
        except sqlite3.OperationalError:
            print("La base de datos esta abierta, reintentando en 5 segundos...")
            sleep(5)


def merge_file_history(file, history):
    twitter_views = []
    pages = []
    pages_to_draw = []
    cont = 0
    for item in history:
        result = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])   # Expresión logica, más info en pythex.org
        if result and result[0] not in ["notifications", "home"]:       # Con los paréntesis fuera de la expresión regular hacemos una captura de ese valor obtenido
            twitter_views.append(result[0])
                                                                        # [A-Za-z0-9]+$  el mas significa que tiene que haber uno o más de uno
                                                                        # El dólar es para que acabe en esa línea
        elif cont % 10 == 0:
            cont += 1
            pages.append(item[0])

        else:
            cont += 1

    if twitter_views:
        file.write("Has visitado estos perfiles de twitter {}...\n".format(", ".join(twitter_views)))

    if pages:
        for page in pages:
            if page not in pages_to_draw:
                pages_to_draw.append(page)

        file.write("Has visitado estas paginas de google {}...\n".format(", ".join(pages_to_draw))) # CUIDADO, SIMBOLOS
        # ESPECIALES DAN PROBLEMAS


def check_bank_account(file, chrome_history):
    bank = None
    banks = ["BBVA", "CaixaBank", "Santander", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                bank = b
                break
        if bank:
            break
    if bank:
        file.write("Con que {} es tu banco...\n".format(bank))


def copy_actually_History(history_path):    # Opción crear un archivo temporal al que conectarse en vez de esperar
    urls = None
    temp_path = history_path + "temp"
    copyfile(history_path, temp_path)
    connection = sqlite3.connect(temp_path)
    cursor = connection.cursor()
    # cursor.execute("")
    cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC LIMIT 100")
    urls = cursor.fetchall()
    return urls


def check_steam(file):
    try:
        path = "C:\Program Files (x86)\Steam\steamapps\common\*"    # Glob necesita que el path acabe con * pq usa
        games = []
        game_paths = glob.glob(path)         # Posiciones relativas
        game_paths.sort(key=os.path.getmtime, reverse=True)
        for game_path in game_paths:
            games.append(game_path.split("\\")[-1])
        file.write("Asi que ultimamente has jugado a {}...".format(", ".join(games[:3])))

    except:
        file.write("Con que no tienes instalado Steam...")


def search_chrome_user(user_path):
    history_paths = []
    # other_files = [".", "..", "AutofillRegex", "AutofillStates", "BrowserMetrics", "CertificateRevocation",
      #             "ClientSidePhishing", "Crashpad", "Crowd Deny", "DesktopSharingHub", "FileTypePolicies",
       #            "FirstPartySetsPreloaded", "Floc", "GrShaderCache", "Guest Profile", "hyphen - data",
        #           "MEIPreload", "Notification Resources", "OnDeviceHeadSuggestModel",
         #          "OptimizationGuidePredictionModels", "OptimizationHints", "OriginTrials", "PKIMetadata", "pnacl",
          #         "PnaclTranslationCache", "RecoveryImproved", "Safe Browsing", "SafetyTips", "ShaderCache",
           #        "SSLErrorAssistant", "Subresource Filter", "SwReporter", "System Profile", "ThirdPartyModuleList64",
            #       "TrustTokenKeyCommitments", "Webstore Downloads", "WidevineCdm", "ZxcvbnData"]
    pseudopath = user_path + "AppData/Local/Google/Chrome/User Data/"
    for item in os.listdir(pseudopath):
        if os.path.isdir(os.path.join(pseudopath, item)):
            if item == "Guest Profile" or item == "System Profile":
                pass
            else:
                for item2 in os.listdir(pseudopath + item):
                    if item2 == "History":
                        history_paths.append(pseudopath + item + "/History")

    return history_paths

def main():
    # delay_action(1)
    user_path = get_user_path()
    desktop_path = user_path + "Desktop\\"  # Para poner \ en un print debemos poner dos \\
    file = create_file(desktop_path)

    history_paths = search_chrome_user(user_path)

    for item in history_paths:
        file.write("\n")
        chrome_history = get_chrome_history(item)
        delay_action(1)
        merge_file_history(file, chrome_history)
        check_bank_account(file, chrome_history)

    check_steam(file)   # Quitar comentarios del codigo y arreglar error


if __name__ == "__main__":
    main()
