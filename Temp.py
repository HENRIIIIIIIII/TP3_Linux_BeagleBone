__author__ = "Loic Marmy + Henri Mott"
__version__ = "1.0"
__maintainer__ = "Loic Marmy"
__email__ = "loic.marmy@eduvaud.ch"
__status__ = "Prototype"
__date__ = "March 2026"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Librairie pour gerer date et heure
import math                                                                 # Librairie pour les calculs mathematiques
import csv                                                                  # Librairie pour ecrire dans un fichier csv
import time                                                                 # Librarie permettant de faire des pauses
import smtplib                                                              # Librairie permettant l'envoi de mails

from sensirion_i2c_driver import I2cConnection                              # Sensor driver
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice                          # Sensor driver
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver  # Sensor driver
from email.message import EmailMessage					    #

#-----------------------------------------------------
# Declaring the sensor object
#-----------------------------------------------------
sht40 = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

#-----------------------------------------------------
# Fonction de lecture du capteur
#-----------------------------------------------------
def read_sensor():
    try:
        # Le capteur renvoie t(temperature) et rh(humidite)
        t, rh = sht40.single_shot_measurement()
        # Watch out! t and rh are variable that contain not only the values but also the units.
        # You can print the values with the units (print(t)) or you can also recover only the value
        # by specifying which one: t.degrees_celsius or rh.percent_rh
    except Exception as ex:
        # si le capteur ne repond pas, envoie un message d'erreur
        print("Error while recovering sensor values:", ex)
    else:
        # si tout va bien , renvoie temperature et humidite
        return t, rh

    return 0 # In case something went wrong

#----------------------------------------------------
# Fonction de calcul du point de rosee
#----------------------------------------------------
def calculate_dew_point(temp, humidity):
    # Constantes de la formule de Magnus
    beta = 17.62
    gamma = 243.12

    # Formule mathematique du point de rosee
    alpha = math.log(humidity / 100) + (beta * temp) / (gamma + temp)
    dp = (gamma * alpha) / (beta - alpha)

    # retourne la valeur calculee
    return dp

#----------------------------------------------------
# Fonction pour ecrire dans le fichier CSV
#----------------------------------------------------
def csv_write_row(file_path, data_row):
    try:
        # ouvre le fichier CSV en mode append (ajout)
        with open(file_path, "a") as file:
            # Cree un objet "Writer" qui sait ecrire dans un fichier CSV
            writer = csv.writer(file)
            # Ecris une ligne dans le fichier CSV contenant les informations demandees
            writer.writerow(data_row)
    # Renvoie 1 si OK, 0 si erreur
    except Exception as ex:
        return 0, ex
    else:
        return 1

#--------------------------------------------------
# Fonction pour l'envoi du mail
#--------------------------------------------------
def send_email_pure_python(receiver, subject, body) :

    # Construction du message
    msg = EmailMessage()				# Cree un nouvel objet "e-mail"
    msg.set_content(body)				# Met le texte du mail dans l'enveloppe
    msg['Subject'] = subject				# Defini le sujet du mail
    msg['From'] = "shockleytransistor@gmail.com"	# Indique l'adresse de l'expediteur
    msg['To'] = receiver				# Indique le destinataire

    try :
        # Ouvre une connexion au serveur d'envoi de mails de Gmail, sur le port 587
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # Demande au serveur de passer la connexion en mode chiffre (secure)
        server.starttls()

        # Authentification aupres du serveur SMTP (connexion au compte Gmail, mot de passe de connexion)
        server.login("shockleytransistor@gmail.com", "awnabzpcxlhqbkfp")

        # Envoi du mail + fermeture de la connexion
        server.send_message(msg)
        server.quit()

        print("Email sent successfully using Python!")

    # Print if error
    except Exception as e :
        print(f"Error: {e}")

############################################################################
#-----------------------------------------------------
# Programme principal
# -----------------------------------------------------------

# Le code suivant ne s'execute que si le fichier est lance directement
if __name__ == "__main__": 
    # Lecture du capteur
    t, rh = read_sensor()

    # Recuperer les valeurs numeriques (degre et pourcent)
    temperature = t.degrees_celsius
    humidity = rh.percent_rh

    # Test si la temperature depasse le seuil de 28 degres
    if (temperature > 22) :
        # Envoie le mail
        send_email_pure_python("loicmarm@gmail.com", "Python Test", "Temperature exceeded 28 degres \n ")
        # Attends 5 secondes entre chaque envoi
        time.sleep(5)

    # Recuperation du point de rosee
    dew_point = calculate_dew_point(temperature, humidity)

    # Affichage console
    print("\f--------------------------------------")
    print("Temperature :", round(temperature, 2), "C")
    print("Humidite    :", round(humidity, 2), "%")
    print("Point de rosee :", round(dew_point, 2), "C")
    print("---------------------------------------")

    # Recuperer date et heure
    now = datetime.datetime.now()
    date = now.strftime("%d.%m.%Y")
    time = now.strftime("%H:%M")

    # Construit la ligne du fichier CSV
    data_row = [date, time, round(temperature, 2), round(humidity, 2), round(dew_point, 2)]

    # Appel de la fonction d'ecriture du fichier CSV
    csv_write_row("/home/debian/project-name/TempLog.csv", data_row)
