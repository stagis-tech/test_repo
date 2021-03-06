# -*- coding: utf-8 -*-
"""Kopie von Kopie von Corona_CH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gILHOAbGwT6TXBSPLgaEKbVYVkEzHQ0V
"""

import pandas as pd

df = pd.read_excel('https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx', skiprows=6)

df

df.describe()

df ['Fallzahlen pro Tag']

df ['Fallzahlen pro Tag']. iloc [-1]

df ['Fallzahlen pro Tag']. sum ()

df ['Fallzahlen pro Tag']. mean ()

df ['Fallzahlen pro Tag'].plot.line ()

df ['Fallzahlen pro Tag'].plot.hist ()

df['Fallzahlen pro Tag, kumuliert'].iloc[-1]

df['Todesfälle pro Tag, kumuliert'].iloc[-1]

df['Todesfälle pro Tag, kumuliert'].iloc[-1] / df['Fallzahlen pro Tag, kumuliert'].iloc[-1] * 100

df ['bevoelkerung'] = 8606033

df['inzidenz'] = df ['Fallzahlen pro Tag, kumuliert'] / df ['bevoelkerung'] * 100000

Datum = df['Datum'].iloc[-1]
Neuinfektionen_heute = df['Fallzahlen pro Tag'].iloc[-1]
Hospitalisationen_heute = df['Hospitalisationen pro Tag'].iloc[-1]
Todesfälle_heute = df['Todesfälle pro Tag'].iloc[-1]

Durchschnitt_Woche_Neuinfektionen = df['Fallzahlen pro Tag'].iloc[-7:].mean()
Durchschnitt_Woche_Hospitalisationen = df['Hospitalisationen pro Tag'].iloc[-7:].mean()
Durchschnitt_Woche_Todesfälle = df['Todesfälle pro Tag'].iloc[-7:].mean()

Infektionen_Total = df['Fallzahlen pro Tag, kumuliert'].iloc[-1]
Hospitalisationen_Total = df['Hospitalisationen pro Tag, Kumuliert'].iloc[-1]
Todesfälle_Total = df['Todesfälle pro Tag, kumuliert'].iloc[-1]

Mein_Text = "Heute {} meldet das Bundesamt für Gesundheit BAG für die vergangenen 24 Stunden {} Neuinfektionen mit dem Coronavirus. {} Personen mussten hospitalisiert werden. {} Personen verstarben an Covid-19. In den letzten 7 Tagen gab es durchschnittlich {} Neuinfektionen pro Tag, {} Personen mussten hospitalisiert werden und {} Menschen verstarben. Seit Beginn der Pandemie infizierten sich {} Menschen. Es wurden gesamthaft {} Personen hospitalisiert und {} Menschen verstarben.".format(Datum, Neuinfektionen_heute, Hospitalisationen_heute, Todesfälle_heute, Durchschnitt_Woche_Neuinfektionen, Durchschnitt_Woche_Hospitalisationen, Durchschnitt_Woche_Todesfälle, Infektionen_Total, Hospitalisationen_Total, Todesfälle_Total)

print (Mein_Text)

"""# Wochenaufgabe

Liebe Stagis, jetzt geht es darum, euren Text-Bot auf den Server zu packen!
Dazu müsst ihr ein paar Dinge machen. Erstmal müsst ihr die folgenden Zeilen zu Eurem Notebook hinzufügen:

Wichtig: statt 

```
dateiname = "claus_test1.txt"
```
müsst ihr euren Namen für die Datei verwenden. Zum Beispiel:
```
dateiname = "beatrice_egli.txt"
```
Außerdem müsst ihr in der Zeile
```
text_file.write(Mein_Text)
```
anpassen, wie Eure Variable heißt, die den Text des Textroboters enthält. Statt **Mein_Text** also Eure eintragen.
"""

dateiname = "claus_test1.txt"

text_file = open("./test_repos/" + dateiname, "w")
text_file.write(Mein_Text)
text_file.close()

print ('Erledigt. ', dateiname, 'wurde hochgeladen.')

"""Wenn ihr damit fertig seid:
- Klickt im Menü auf `Datei > .py herunterladen`
- Schickt die Datei an Claus

## Hintergrund für die, die es interessiert

- Das System, das ich gebaut habe, läuft auf einem kleinen Raspberry Pi Minicomputer, der in meiner Wohnung steht.
- Darauf läuft eine Linux-Version (Ubuntu)
- Ich habe eine Software namens Jenkins.io installiert - mit der kann man Python-Code zeitgesteuert ausführen (z.B. einmal in der Stunde)
- Jenkins zieht sich Euer Python-Script von Github, führt es aus und lädt die fertige Datei dann wieder auf Github hoch, in das Unterverzeichnis /reports (https://github.com/stagis-tech/test_repo/tree/main/reports)
- Github ist eine Seite, auf der man Code hosten kann - in vielen Profi-Teams wird Git (Git ist nicht gleich Github) genutzt, um zusammen an Code zu arbeiten. Git speichert jede Änderung, man kann sie zusammenführen, vergleichen und notfalls rückgängig machen.
"""

