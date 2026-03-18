# TP3_Linux_BeagleBone
Documentation:
https://wiki.seeedstudio.com/BeagleBone_Green/
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=header"/>

### Q1. Comment pouvez-vous déterminer cette adresse IP ?

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
     
     -Une fois la BeagleBone connectée, il faut ecrire le nom d'utilisateur "debian"
     ainsi que le mot de passe "temppwd"
     
     <img width="657" height="339" alt="Mot de passe" src="https://github.com/user-attachments/assets/9a135ea3-7054-4790-8e1f-6d3f37f66028" />

![divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&height=2)

### Q2. Quel est le protocole de communication permettant de vous connecter à distance au BBG ?

-Le protocole étais selectioné dans putty et est le protocole SSH.
-PuTTY utilise SSH pour ouvrir un terminal sécurisé (Secure Shell).

### Q3. Dans le modèle OSI, dans quelle(s) couche(s) se trouve ce protocole ?

-Le SSH est un protocole qui s'appuie sur le TCP (couche 4) et les applications (en couche 5).
-Donc il se trouve dans les couches 4-5.

### Q4. Sur quel protocole de couche 4 s’appuie ce protocole ? Quel est le port utilisé côté serveur

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

  -Voici le fichier de configuration avec le contenu demandé pour régler 
  une adresse IP statique
  
  <img width="661" height="418" alt="Adress_Statique" src="https://github.com/user-attachments/assets/9562e7a3-9bfa-4ebe-a153-e2960828bfde" />

  8. Sauvegardez le fichier et redémarrez le BBG :

  -La commande pour sauvegarder et redemarrer est "sudo reboot"

  9. Connectez-vous à nouveau à votre BBG à l’aide de Putty (nouvelle adresse IP).

-Cette fois si quand on se reconnecte, il faut utiliser l'adresse IP statique qui est 
celle inscrite sur la BeagleBone : 10.228.134.227

<img width="452" height="444" alt="config_Adressestatique" src="https://github.com/user-attachments/assets/253a8817-25d7-458f-8429-64b9f777b0f4" />

### Q5. Si vous n’arriviez pas à vous connecter au BBG, quelle(s) commande(s), testeriez-vous depuis 
une autre machine connectée au même réseau ?

  ping <adresse_IP>
  Pour tester la connection entre 2 machines
  
  telnet <adresse_IP> 
  Et utilisé pour nous connecter à un port comme le port 22
  
  nmap <adresse_IP>
  (« Network Mapper ») est un outil open source d'exploration réseau et d'audit de sécurité source: https://nmap.org/man/fr/index.html#man-description

### Q6. A la suite de votre connexion, dans quel répertoire vous trouvez-vous ? 
Quelle(s) commande(s) utilisez-vous pour le déterminer ?

-La commande a utiliser pour savoir dans quel répertoire on se trouve est "pwd -P" 
elle affichera le contenu ci-dessous :

<img width="238" height="55" alt="Repertoireactuel" src="https://github.com/user-attachments/assets/4dee9f59-50a5-4e7a-b50d-b19cd53b0e8b" />

Le repertoire est donc le repertoire du user

  10. Créez un répertoire à cet emplacement que vous nommerez : TP3_XXX_YYY
  X et Y représentent vos initiales si vous êtes en binômes.

### Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire ?
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

###Q8. Comment pouvez-vous contrôler ce que vous avez écrit sans réouvrir le fichier en écriture ?

-Le contrôle peut être effectué avec la commande "cat" + nom du fichier.txt :

<img width="450" height="52" alt="contenudufichier" src="https://github.com/user-attachments/assets/bf72fe6e-7d38-46c1-bc1b-4e9c89781d01" />

### Q9. Comment contrôlez-vous qu’un logiciel soit bien installé ?
Quelle(s) est/sont les commandes pour installer un logiciel (vous pouvez tester par exemple avec 
sl ou cmatrix) ?

-Pour tester si un logiciel est installé, il faut utiliser la commande "which cmatrix". 
Si le logiciel est installé voici ce qui s'affiche :

<img width="388" height="52" alt="image" src="https://github.com/user-attachments/assets/2c1cbc06-37b4-4334-a2d0-e50c7554e500" />

-Si le logiciel n'est pas installé, il faut utiliser les commandes "sudo apt update" pour mettre a jour :

<img width="661" height="238" alt="miseajour" src="https://github.com/user-attachments/assets/1deac06f-54e2-4d57-b81f-3a3fff7a5e8e" />

-et ensuite la commande "sudo apt install cmatrix" pour installer le logiciel cmatrix :

<img width="664" height="114" alt="installationcmatrix" src="https://github.com/user-attachments/assets/7031f767-a3ff-4e3c-88ea-e3ef9b91cec8" />

### Q10. Sur le BBG, quelle(s) est/sont la/les commande(s) pour connaitre la configuration du réseau 
Ethernet ? 
-Avec la commande "ip a", on obtient les informations de l'adresse IP, le masque et l'adresse MAC :

<img width="658" height="397" alt="infoa" src="https://github.com/user-attachments/assets/2e72cf3a-4a09-4ca1-904b-b4a6159d4690" />

-Avec la commande "ip r", on obtient les informations de la passerelle ainsi que de l'adresse réseau :

<img width="560" height="60" alt="infor" src="https://github.com/user-attachments/assets/e3f96579-0cd3-4de8-b836-535da54004ca" />

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

### Q11. Qu’est-ce qui s’affiche en retour ? 
Commentez.

<img width="646" height="131" alt="image" src="https://github.com/user-attachments/assets/ecefcef7-588d-41fc-b970-e9c4abf1c8fd" />

Le site nous donne l'adresse publique IP, pour accéder à l'internet.
Current IP Address: 193.5.240.10 

  16. Sur votre BBG, utilisez la commande suivante :
  wget -qO- http://checkip.dyndns.org
source: https://www.gnu.org/software/wget/

<img width="682" height="86" alt="image" src="https://github.com/user-attachments/assets/a2bd3854-5ff0-4b13-b7a6-be32ba3dbe04" />

### Q12. Expliquez ce que fait cette commande.

Qu’est-ce qui s’affiche en retour ? 

Wget est pour télécharger/récupérer des fichiers ou contenus depuis Internet directement depuis le terminal.

  - q correspond a "quiet"
  - O "correspond a write document to file"  (wget --help)
    
Cette commande nous liste le code ou HTML pur du site, donc la page, le texte dans la page puis le résultat.
<html><head><title> 
sont des elements HTML 
  source: https://www.w3schools.com/html/html_head.asp

Quel est format de la réponse ? 
Faites le parallèle avec la réponse à la Q11.

Le format et en element HTML, code source complet de la page.

### Q13. Comparez l’adresse IP locale de votre BBG à celles trouvées aux Q11 et Q12. 
Commentez

Les IP sont identiques parce que notre ordinateur et notre BBG vont à travers notre routeur (NAT  ou Network Address Translation) pour accéder à l'internet.
Mais leur adresse locale est différente de celle du PC.
