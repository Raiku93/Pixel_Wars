# Pixelwars
Pixelwars est un jeu multijoueur de dessin en pixel en temps réel.


## Conseil
Le projet est contenu dans le répertoire Pixelwars. Les fichiers hors de ce répertoire servent uniquement à comprendre l'évolution et le développement de ce projet.

## Prérequis
Avant de commencer, assurez-vous d'avoir Python, Django, Redis et virtualenv (venv et généralement présent pas défaut) installés sur votre système.

## Installation

Clonez le dépôt :

```
git clone https://github.com/votre-utilisateur/Pixel_Wars.git
```
Accédez au répertoire du projet :

```
cd Pixelwars
```
Créez un environnement virtuel :

#### Pour Windows

```
python -m venv venv
.\venv\Scripts\activate
```

#### Pour Linux

```
python3 -m venv venv
source venv/bin/activate
```
Installez les dépendances du projet :

```
pip install -r requirements.txt
```
## Configuration

Appliquez les migrations de la base de données  :

```
python manage.py migrate
```

Initialiser la base de données de données :

```
populate_pixels.py
```

Pour trouver l'adresse IP de votre serveur :

#### Pour Windows

```
ipconfig
```
Cherchez l'adresse IPv4 sous l'adaptateur réseau que vous utilisez.

#### Pour Linux

```
ifconfig
```
Cherchez l'adresse votre adresse IPv4.




Mettez à jour l'adresse IP du serveur WebSocket dans le fichier ```static/script.js``` avec l'adresse de la machine hébergeant le jeu.

Lancez le serveur de développement Django :

```
python manage.py runserver <adresseip>:<port>
```

Démarrez le serveur WebSocket en utilisant Redis :

#### Pour Windows

```
redis-server
```
#### Pour Linux

```
redis-server&
```


## Contribution
N'hésitez pas à contribuer à ce projet en ajoutant davantage de fonctionnalités.

## License
Ce projet est sous licence MIT - consultez le fichier LICENSE pour plus de détails.

## Aide
Assurez-vous de remplacer <adresseip> et <port> par l'adresse IP et le numéro de port appropriés que vous souhaitez utiliser pour votre serveur.

Vous pouvez modifier la taille de la grille de pixel dans le fichier suivant : ```PixelWars/App_Pixelwars/management/commands/populate_pixels.py```


Pour accéder à votre jeu, les joueurs doivent se connecter au mème réseau que la machine serveur et écrire l'url l'adresse IP de la machine serveur ! 

En cas de problème, veuillez contacter les développeurs : 
        - Walid TOURABI
        - Mame Khady WADE
        - Hakim BOUALI
        - Adam BOURRAIS

# Bonne partie !
