# TP3_Linux_BeagleBone
Documentation:
https://wiki.seeedstudio.com/BeagleBone_Green/

Q1. Comment pouvez-vous déterminer cette adresse IP ?
-Pour determiner l'adresse IP de la BeaglBone, nous avons utiliser le logiciel "Advanced IP scanner"
-Il suffit de rechercher les adresse de 10.228.134.0 à 10.228.134.255 pour trouver la notre.
-Une fois le scann fini nous obtenons notre adresse IP qui est : 10.228.134.44

  4. Sur votre machine hôte, ouvrez Putty2
    a. Insérez l’adresse IP du BBG déterminée ci-dessus.
    b. Sélectionnez SSH.
    c. Puis, bouton « open ».
  5. Une fois la connexion établie, il faudra vous connecter au BBG via le shell fourni.
        User : debian / Mot de passe : temppwd
     
     -Inscire l'adresse IP scannée précédemment dans PuTTY
     <img width="459" height="444" alt="image" src="https://github.com/user-attachments/assets/b78f4022-5f7f-4794-ab28-602a6a0a7e97" />
     
     -Une fois la BeagleBone connectée, il faut ecrire le nom d'utilisateur "debian" ainsi que le mot de passe "temppwd" 
     <img width="657" height="339" alt="image" src="https://github.com/user-attachments/assets/faaf27b9-446c-4d26-b2ae-3666825b75a9" />

Q2. Quel est le protocole de communication permettant de vous connecter à distance au BBG ?

-Le protocole étais selectioné dans putty et est le protocole SSH.
-PuTTY utilise SSH pour ouvrir un terminal sécurisé (Secure Shell).

Q3. Dans le modèle OSI, dans quelle(s) couche(s) se trouve ce protocole ?

-Le SSH est un protocole qui s'appuie sur le TCP (couche 4) et les applications (en couche 5).
-Donc il se trouve dans les couches 4-5.

Q4. Sur quel protocole de couche 4 s’appuie ce protocole ? Quel est le port utilisé côté serveur

-Il s'appuie sur le protocole TCP.
-Le port utilisé est le port 22, qui est le port de default du SSH.

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

  -Voici le fichier de configuration avec le contenu demandé pour régler une adresse IP statique
  <img width="661" height="418" alt="image" src="https://github.com/user-attachments/assets/ddad2706-4698-46b3-a7a0-438a2fcc35ca" />

  8. Sauvegardez le fichier et redémarrez le BBG :

  -La commande pour sauvegarder et redemarrer est "sudo reboot"

  9. Connectez-vous à nouveau à votre BBG à l’aide de Putty (nouvelle adresse IP).

-Cette fois si quand on se reconnecte, il faut utiliser l'adresse IP statique qui est celle inscrite sur la BeagleBone : 10.228.134.227
<img width="452" height="444" alt="image" src="https://github.com/user-attachments/assets/15c21b04-ba48-48e1-a9d2-ebd0e0ec5f02" />

Q5. Si vous n’arriviez pas à vous connecter au BBG, quelle(s) commande(s), testeriez-vous depuis 
une autre machine connectée au même réseau ?

Q6. A la suite de votre connexion, dans quel répertoire vous trouvez-vous ? 
Quelle(s) commande(s) utilisez-vous pour le déterminer ?

-La commande a utiliser pour savoir dans quel répertoire on se trouve est "pwd -P" elle affichera le contenu ci-dessous :
<img width="238" height="55" alt="image" src="https://github.com/user-attachments/assets/b56351d0-f16a-4516-9eaa-b8b526379dcb" />

debian = User

  10. Créez un répertoire à cet emplacement que vous nommerez : TP3_XXX_YYY
  X et Y représentent vos initiales si vous êtes en binômes.

Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire ?
Qui a les droits d’écriture dessus ? 

-Pour créer un répertoire, il faut taper la commande "mkdir" + nom du répertoire 
<img width="304" height="16" alt="image" src="https://github.com/user-attachments/assets/23bda82f-bf23-429f-b75b-5ccb541fee95" />

Seul l'utilisateur (debian) a les droits d'écriture dans ce répertoire

  12. Editez un fichier texte (contenant vos noms – prénoms), et placez ce fichier dans le répertoire 
  créé auparavant.
-La commande pour créer un fichier texte est "mkdir" + nom du fichier.txt
<img width="478" height="20" alt="image" src="https://github.com/user-attachments/assets/95973500-3258-42dd-be6c-729ac118dfcc" />

-Ensuite inscire les noms et prenoms dans ce fichier :
<img width="667" height="414" alt="image" src="https://github.com/user-attachments/assets/9e262e5e-4c17-4cb7-a218-37ae3d683913" />

Q8. Comment pouvez-vous contrôler ce que vous avez écrit sans réouvrir le fichier en écriture ?

-Le contrôle peut être effectué avec la commande "cat" + nom du fichier.txt :
<img width="450" height="52" alt="image" src="https://github.com/user-attachments/assets/acf24ed8-12a4-4750-8ef3-b22415892786" />


Q9. Comment contrôlez-vous qu’un logiciel soit bien installé ?
Quelle(s) est/sont les commandes pour installer un logiciel (vous pouvez tester par exemple avec 
sl ou cmatrix) ?

-Pour tester si un logiciel est installé, il faut utiliser la commande "which cmatrix". Si le logiciel est installé voici ce qui s'affiche :
<img width="388" height="52" alt="image" src="https://github.com/user-attachments/assets/2c1cbc06-37b4-4334-a2d0-e50c7554e500" />

-Si le logiciel n'est pas installé, il faut utiliser les commandes "sudo apt update" pour mettre a jour :
<img width="661" height="238" alt="image" src="https://github.com/user-attachments/assets/98cee4fa-3062-413e-ae52-e6acb297aef9" />

-et ensuite la commande "sudo apt install cmatrix" pour installer le logiciel cmatrix :
<img width="664" height="114" alt="image" src="https://github.com/user-attachments/assets/00af53c7-3ed9-4bac-ac65-3d823c37106f" />

Q10. Sur le BBG, quelle(s) est/sont la/les commande(s) pour connaitre la configuration du réseau 
Ethernet ? 
-Avec la commande "ip a", on obtient les informations de l'adresse IP, le masque et l'adresse MAC :
<img width="658" height="397" alt="image" src="https://github.com/user-attachments/assets/d73d962d-b888-4dfe-b2b0-dcac1930090a" />

-Avec la commande "ip r", on obtient les informations de la passerelle ainsi que de l'adresse réseau :
<img width="560" height="60" alt="image" src="https://github.com/user-attachments/assets/3721cb9a-27f8-4d7f-84b9-d0c3375c017c" />

  a. Quelle est l’adresse IP du BBG ?
  -A la ligne "inet", l'adresse indiquée est : 10.228.134.227
  b. Quelle est le masque de sous réseau ? 
  -Toujours à la ligne "inet", le /24 signifie que l'adresse de sous réseau est : 255.255.255.0
  c. Quelle est l’adresse réseau ? 
  -10.228.134.0
  d. Quelle est la passerelle par défaut ? 
  -A la ligne "default via", la passerelle indiquée est : 10.228.134.1
  e. Quelle est l’adresse MAC du BBG ? 
  -A la ligne "link/ether", l'adresse MAC indiquée est : 20:d7:78:7d:73:5e
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

