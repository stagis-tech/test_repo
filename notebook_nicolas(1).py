# -*- coding: utf-8 -*-
"""Notebook_Nicolas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gri0Kv9R7KPbhJdB7bvinbRjhRSpIf4P
"""

import pandas as pd

import pandas as pd

df=pd.read_excel("https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx", skiprows=6, sheet_name=2, skipfooter = 2)

df

KantoneBestätigteFälle=df.sort_values(by="Bestätigte Fälle")

KantoneBestätigteFälle

KantoneInzidenz=df.sort_values(by="Inzidenz/100 000")

KantoneInzidenz

KantoneInzidenzLetzteZweiWochen=df.sort_values("Inzidenz/100 000.1")

KantoneInzidenzLetzteZweiWochen



KantoneBestätigteFälleLetzteZweiWochen=df.sort_values(by="Bestätigte Fälle.1")

KantoneBestätigteFälleLetzteZweiWochen

KantoneBestätigteFälleLetzteZweiWochen=df["Bestätigte Fälle.1"].max()

KantoneBestätigteFälleLetzteZweiWochen





KantonWenigsteFälle=KantoneInzidenzLetzteZweiWochen['Kanton'].iloc[0]
FälleWenigste=KantoneInzidenzLetzteZweiWochen['Inzidenz/100 000.1'].iloc[0]

KantonWenigsteFälle

FälleWenigste

MeinText1=" Am wenigsten neu registrierte Covid-19-Infektionen in den letzten zwei Wochen verzeichnet der Kanton {}: bloss {} Fälle.".format(KantonWenigsteFälle, FälleWenigste)



MeinText1





df=pd.read_excel('https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx', skiprows=6)

df

AktuelleZahlen=df['Fallzahlen pro Tag'].iloc[-1]

AktuelleZahlen

AktuelleHospitalisationen=df['Hospitalisationen pro Tag'].iloc[-1]

AktuelleHospitalisationen

if AktuelleZahlen > 0:
 print(AktuelleHospitalisationen/AktuelleZahlen)
else :
  print("Berechnung nicht möglich")

GesamteTodesfälle=df['Todesfälle pro Tag, kumuliert'].iloc[-1]

GesamteTodesfälle

df['Todesfälle pro Tag'].plot.line()

df['Fallzahlen pro Tag'].plot.line()



df["Hospitalisationen pro Tag, Kumuliert"].plot.line()

df['Todesfälle pro Tag, kumuliert'].iloc[-1] / df['Fallzahlen pro Tag, kumuliert'].iloc[-1] *100

df['bevoelkerung'] = 8606033

Datum=df['Datum'].iloc[-1]
NeuinfektionenHeute=df['Fallzahlen pro Tag'].iloc[-1]
NeuhospitalisationenHeute=df['Hospitalisationen pro Tag'].iloc[-1]
NeueTodesfaelle=df['Todesfälle pro Tag'].iloc[-1]

InfektionenWochenschnitt=df['Fallzahlen pro Tag'].iloc[-7:].mean()
HospitalisationenWochenschnitt=df['Hospitalisationen pro Tag'].iloc[-7:].mean()
TodesfaelleWochenschnitt=df['Todesfälle pro Tag'].iloc[-7:].mean()

InfektionenTotal=df['Fallzahlen pro Tag, kumuliert'].iloc[-1]
HospitalisationenTotal=df['Hospitalisationen pro Tag, Kumuliert'].iloc[-1]
TodesfaelleTotal=df['Todesfälle pro Tag, kumuliert'].iloc[-1]

AnzahlToteTagEins=df["Todesfälle pro Tag"].iloc[-250]

AnzahlToteTagEins

nan=0

Fehlermeldung="Am gewünschten Tag wurden hierzu keine Daten eingetragen."

if AnzahlToteTagEins is nan:
  print("Am gewünschten Tag wurden hierzu keine Daten eingetragen.")

if AnzahlToteTagEins is 0:
  print(Fehlermeldung)

print(Fehlermeldung)

MeineVariable1="Wieso du?" #Zwischenübung
MeineVariable2="Wieso ich?"
Ausgabetext= "So oft fragte er: {} Aber ebenso oft fragte er: {}".format(MeineVariable1, MeineVariable2)
print(Ausgabetext)

Datum=df['Datum'].iloc[-1]
NeuinfektionenHeute=df['Fallzahlen pro Tag'].iloc[-1]
NeuhospitalisationenHeute=df['Hospitalisationen pro Tag'].iloc[-1]
NeueTodesfaelle=df['Todesfälle pro Tag'].iloc[-1]

InfektionenWochenschnitt=df['Fallzahlen pro Tag'].iloc[-7:].mean()
HospitalisationenWochenschnitt=df['Hospitalisationen pro Tag'].iloc[-7:].mean()
TodesfaelleWochenschnitt=df['Todesfälle pro Tag'].iloc[-7:].mean()

InfektionenTotal=df['Fallzahlen pro Tag, kumuliert'].iloc[-1]
HospitalisationenTotal=df['Hospitalisationen pro Tag, Kumuliert'].iloc[-1]
TodesfaelleTotal=df['Todesfälle pro Tag, kumuliert'].iloc[-1]

ToteTagEins=Fehlermeldung

MeinText="Heute {} meldet das Bundesamt für Gesundheit BAG {} neue Infektionen mit dem neuartigen Coronavirus, die in den vergangenen 24 Stunden registriert wurden. {} Personen mussten hospitalisiert werden. {} Menschen sind gemäss BAG im Zusammenhang mit Covid-19 in den letzten 24 Stunden gestorben. Im Durchschnitt der letzten 7 Tage steckten sich täglich offiziell {} Personen mit dem neuartigen Coronavirus an, {} Personen mussten hospitalisiert werden und {} Menschen starben an den Folgen der Infektion. Seit Beginn der Pandemie zählt die Schweiz insgesamt {} positive Corona-Tests. {} Personen mussten nach einer Infektion ins Spital eingeliefert werden und {} Personen sind bisher an den Folgen an einer Corona-Infektion gestorben.".format(Datum, NeuinfektionenHeute, NeuhospitalisationenHeute, NeueTodesfaelle, InfektionenWochenschnitt, HospitalisationenWochenschnitt, TodesfaelleWochenschnitt, InfektionenTotal, HospitalisationenTotal, TodesfaelleTotal)

print(MeinText)

MeinText3=MeinText + MeinText1

MeinText3

Dateiname="Notebook_Nicolas.txt"

text_file = open("Notebook_Nicolas.txt", "w")
text_file.write(MeinText3)
text_file.close()

