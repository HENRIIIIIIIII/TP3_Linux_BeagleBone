# TP3_Linux_BeagleBone
Documentation:
https://wiki.seeedstudio.com/BeagleBone_Green/

Q1. Comment pouvez-vous déterminer cette adresse IP ?

En utilisant le logiciel Advanced IP scaner.
en rechérchant de 10.228.134.0 a 255
notre IP: 10.228.134.44 

  4. Sur votre machine hôte, ouvrez Putty2
    a. Insérez l’adresse IP du BBG déterminée ci-dessus.
    b. Sélectionnez SSH.
    c. Puis, bouton « open ».
  5. Une fois la connexion établie, il faudra vous connecter au BBG via le shell fourni.
        User : debian / Mot de passe : temppwd

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

  8. Connectez-vous à nouveau à votre BBG à l’aide de Putty (nouvelle adresse IP).

Q5. Si vous n’arriviez pas à vous connecter au BBG, quelle(s) commande(s), testeriez-vous depuis 
une autre machine connectée au même réseau ?

Q6. A la suite de votre connexion, dans quel répertoire vous trouvez-vous ? 
Quelle(s) commande(s) utilisez-vous pour le déterminer ?

  10. Créez un répertoire à cet emplacement que vous nommerez : TP3_XXX_YYY
  X et Y représentent vos initiales si vous êtes en binômes.

Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire ?
Qui a les droits d’écriture dessus ? 

  12. Editez un fichier texte (contenant vos noms – prénoms), et placez ce fichier dans le répertoire 
  créé auparavant.

Q8. Comment pouvez-vous contrôler ce que vous avez écrit sans réouvrir le fichier en écriture ?

Q9. Comment contrôlez-vous qu’un logiciel soit bien installé ?
Quelle(s) est/sont les commandes pour installer un logiciel (vous pouvez tester par exemple avec 
sl ou cmatrix) ?

Q10. Sur le BBG, quelle(s) est/sont la/les commande(s) pour connaitre la configuration du réseau 
Ethernet ? 
  a. Quelle est l’adresse IP du BBG ?
  b. Quelle est le masque de sous réseau ? 
  c. Quelle est l’adresse réseau ? 
  d. Quelle est la passerelle par défaut ? 
  e. Quelle est l’adresse MAC du BBG ? 
  
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

