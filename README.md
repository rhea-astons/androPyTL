# androPyTL

## Description
Notifie des prochains bus et metros des transports publics
lausannois (http://www.t-l.ch) à la station la plus proche
de la position GPS fournie par Android, via Tasker (http://http://tasker.dinglisch.net/)

Copyleft 2013 Raphael Santos
License GPL

## Pré-requis
* Android
* Tasker (https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)
* Scripting Layer for Android (SL4A) (https://code.google.com/p/android-scripting)
* Python Interpreter (https://code.google.com/p/android-scripting/wiki/InstallingInterpreters)

## Tâche Tasker
* Divers > Obtenir une localisation
* Script > Executer un script
  * Nom: androPyTL.py
  * Passer les variables: %LOC

## Divers
Avec une montre Pebble (http://www.getpebble.com) et PebbleTasker (https://play.google.com/store/apps/details?id=com.kodek.pebbletasker), il est possible d'executer la tâche depuis la montre puis de faire remonter la notification des résultats sur la montre.