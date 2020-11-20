# Docker cheat sheet

## Build

```docker build [OPTIONS] PATH | URL | -```

Build une image docker à partir d'un fichier docker ```Dockerfile``` et un contexte.

Le contexte correspond à un ensemble de fichier localisé par la variable ```PATH``` ou ```URL```.


### ```URL``` peut pointer:

#### **un repo Git**

Le repo est pull dans un dossier temporaire locale. Il est ensuite envoyé au daemon docker qui l'utilise comme contexte.

#### **une archive tar**

```URL``` est passée au daemon docker. Le deaemon télécharge l'archive sur la machine hote.

#### **un ```Dockerfile``` ou un fichier text**

Si ```URL``` pointe un fichier texte, le daemon docker va insérer son contenu dans un ```Dockerfile```. Dans ce cas, il n'y a pas de contexte.


### Bonne pratique

Stocker chaque ```Dockerfile``` dans un dossier vide (le contexte), afin d'ajouter à ce dossier les fichiers nécessaires au processus de build.


## Run

```docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]```

Permet de déclarer et lancer un container à partir d'une image docker.

Il exécute successivement les commandes ```docker create``` et ```docker start```.

Flag ```-it``` pour un processus interactif.

### Bonne pratique

Ne pas utiliser ```run``` à chaque fois. Plutot utiliser ```start``` pour conserver les modifications apportées.


## Create

```docker create [OPTIONS] IMAGE [COMMAND] [ARG...]```

Crée un container à partir d'une image en lui donnant ses paramètres d'exécution. Par exemple, nommer le container.

ex: ```docker create --tty --interactive --name="wonderful_mobidock" debian:7```


## Start

```docker start [OPTIONS] CONTAINER [CONTAINER...]```

Lance un ou plusieurs containers.

ex: ```docker start --attach wonderful_mobido```

Le flag ```--attach``` permet ici d'attacher un terminal au container.


## Stop

```docker stop [OPTIONS] CONTAINER [CONTAINER...]```

Stop un ou plusieurs containers.

## Exec

```docker exec [OPTIONS] CONTAINER COMMAND [ARG...]```

Permet de run une commande à l'intérieur du container.


## Rmi

```docker rmi [OPTIONS] IMAGE [IMAGE...]```

Permet de supprimer une ou plusieurs images docker.

## Ps

```docker ps [OPTIONS]```

Liste les container actifs. Flag ```-a``` pour afficher les containers stopés.

## Rm

```docker rm [OPTIONS] CONTAINER [CONTAINER...]```

Delete un container innactif.

```docker container prune``` pour delete tous les container stopés.

# Definitions et concepts docker


## Image docker

Une image représente un état de container à un moment donné. Elles sont définies par un Dockerfile.

Elles proviennet tous d'une image parente, mis à part les images de base comme les images OS.

On peut lister les images disponibles sur l'host avec ```docker images```.


## Dockerfile

Fichier qui va décrire la construction d'une image docker. Par défaut il doit se trouver à la racine du projet.


## Persistent storage ou volume

Permet de définir un espace de stockage externe au container. Ainsi, la data contenue dans cet espace ne dépend pas de la 'durée de vie' du container. On peut en déclarer plusieurs pour un container. Peuvent être mis en place pendant la configuration du container.


## Port 

Un port docker se comporte comme tout autre port logiciel en informatique. Il permet d'identifier plusieurs interlocuteurs (des programmes) qui, à travers ce port, peuvent écouter ou transmettre des informations.

Un port réseau docker est isolé dans le container, il n'est pas exposé au monde extèrieur. Pour communiquer avec le monde extèrieur il nous faudra donc exposer un port de l'hote sur un port interne au container. C'est de la redirection de port.

Un port peut aussi être exposé afin de communiquer entre container avec ```EXPOSE``` et ```link```, sans passer par l'hote.

```link``` permet à un container d'utiliser les services d'un autre container. Pour ce faire il regarde la valeur du ```EXPOSE``` du container cible, exposant une adresse de port.