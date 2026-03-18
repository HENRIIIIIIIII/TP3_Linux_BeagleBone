# TP3_Linux_BeagleBone
Documentation:
https://wiki.seeedstudio.com/BeagleBone_Green/

Q1. Comment pouvez-vous déterminer cette adresse IP ?

En utilisant le logiciel Advanced IP scaner.
en recherchant de 10.228.134.0 a 10.228.134.255
notre IP: 10.228.134.44 

  4. Sur votre machine hôte, ouvrez Putty2
    a. Insérez l’adresse IP du BBG déterminée ci-dessus.
    b. Sélectionnez SSH.
    c. Puis, bouton « open ».
  5. Une fois la connexion établie, il faudra vous connecter au BBG via le shell fourni.
        User : debian / Mot de passe : temppwd
     <img width="459" height="444" alt="image" src="https://github.com/user-attachments/assets/b78f4022-5f7f-4794-ab28-602a6a0a7e97" />
     <img width="657" height="339" alt="image" src="https://github.com/user-attachments/assets/faaf27b9-446c-4d26-b2ae-3666825b75a9" />

Q2. Quel est le protocole de communication permettant de vous connecter à distance au BBG ?

Le protocole étais selectioné dans putty (SSH).
PuTTY utilise SSH pour ouvrir un terminal sécurisé (Secure Shell).

Q3. Dans le modèle OSI, dans quelle(s) couche(s) se trouve ce protocole ?

Le SSH est un protocole qui s'appuie sur le TCP (couche 4) et les applications (en couche 5).
Donc il se trouve dans les couches 4-5.

Q4. Sur quel protocole de couche 4 s’appuie ce protocole ? Quel est le port utilisé côté serveur

Il s'appuie sur le protocole TCP.
Le port utilisé est le port 22, qui est le port de default du SSH.

  6. La configuration réseau est gérée par networkd. Il faut éditer un fichier de configuration afin de 
  régler une adresse IP statique :
  sudo nano /etc/systemd/network/10-eth0-static.network
  Modifiez le contenu du fichier comme suit :
  [Match]
  Name=eth0
  [Network]
  Address=adresse IP sur étiquette/24
  Gateway=10.228.134.1
  DNS=10.228.146.6 10.228.146.7
  DHCP=no
  7. Sauvegardez le fichier et redémarrez le BBG :

  Sudo reboot

  9. Connectez-vous à nouveau à votre BBG à l’aide de Putty (nouvelle adresse IP).
<img width="452" height="444" alt="image" src="https://github.com/user-attachments/assets/15c21b04-ba48-48e1-a9d2-ebd0e0ec5f02" />

Q5. Si vous n’arriviez pas à vous connecter au BBG, quelle(s) commande(s), testeriez-vous depuis 
une autre machine connectée au même réseau ?

Q6. A la suite de votre connexion, dans quel répertoire vous trouvez-vous ? 
Quelle(s) commande(s) utilisez-vous pour le déterminer ?
<img width="238" height="55" alt="image" src="https://github.com/user-attachments/assets/b56351d0-f16a-4516-9eaa-b8b526379dcb" />

*
debian@BeagleBone:~$ pwd -P
/home/debian
*
debian = User

  10. Créez un répertoire à cet emplacement que vous nommerez : TP3_XXX_YYY
  X et Y représentent vos initiales si vous êtes en binômes.

Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire ?
Qui a les droits d’écriture dessus ? 
<img width="304" height="16" alt="image" src="https://github.com/user-attachments/assets/23bda82f-bf23-429f-b75b-5ccb541fee95" />


  12. Editez un fichier texte (contenant vos noms – prénoms), et placez ce fichier dans le répertoire 
  créé auparavant.
 <img width="478" height="20" alt="image" src="https://github.com/user-attachments/assets/95973500-3258-42dd-be6c-729ac118dfcc" />
<img width="667" height="414" alt="image" src="https://github.com/user-attachments/assets/9e262e5e-4c17-4cb7-a218-37ae3d683913" />


Q8. Comment pouvez-vous contrôler ce que vous avez écrit sans réouvrir le fichier en écriture ?

Avec la commande cat Fichier_texte.txt
<img width="449" height="55" alt="image" src="https://github.com/user-attachments/assets/c6b243ab-c417-449a-bdca-6c9b11d6ad4b" />


Q9. Comment contrôlez-vous qu’un logiciel soit bien installé ?
Quelle(s) est/sont les commandes pour installer un logiciel (vous pouvez tester par exemple avec 
sl ou cmatrix) ?

Pour tester si un logiciel est installé, il faut utiliser la commande "which cmatrix". Si le logiciel est installé voici ce qui s'affiche
<img width="388" height="52" alt="image" src="https://github.com/user-attachments/assets/2c1cbc06-37b4-4334-a2d0-e50c7554e500" />

Si le logiciel n'est pas installé, il faut utiliser les commandes "sudo apt update" pour mettre a jour et "sudo apt install cmatrix" pour installer le logiciel cmatrix
<img width="661" height="238" alt="image" src="https://github.com/user-attachments/assets/98cee4fa-3062-413e-ae52-e6acb297aef9" />
<img width="664" height="114" alt="image" src="https://github.com/user-attachments/assets/00af53c7-3ed9-4bac-ac65-3d823c37106f" />

Q10. Sur le BBG, quelle(s) est/sont la/les commande(s) pour connaitre la configuration du réseau 
Ethernet ? 
La commande a inscrire est "ip addr" ce qui donne les informations suivantes :
<img width="667" height="416" alt="image" src="https://github.com/user-attachments/assets/6a6ed59b-c2e6-489f-b711-62d515014a0c" />

  a. Quelle est l’adresse IP du BBG ?
  10.228.134.227
  b. Quelle est le masque de sous réseau ? 
  255.255.255.0 
  c. Quelle est l’adresse réseau ? 
  10.228.134
  d. Quelle est la passerelle par défaut ? 
  10.228.134.1
  e. Quelle est l’adresse MAC du BBG ? 
  En utilisant la commande arp -a on trouve l'adresse suivante :
  00:09:0f:09:01:08 
  14. Dans un navigateur, depuis votre poste de travail école, accédez à http://checkip.dyndns.org

Q11. Qu’est-ce qui s’affiche en retour ? 
Commentez.

  16. Sur votre BBG, utilisez la commande suivante :
  wget -qO- http://checkip.dyndns.org

Q12. Expliquez ce que fait cette commande.
Qu’est-ce qui s’affiche en retour ? 
Quel est format de la réponse ? 
Faites le parallèle avec la réponse à la Q11.

Q13. Comparez l’adresse IP locale de votre BBG à celles trouvées aux Q11 et Q12. 
Commentez

