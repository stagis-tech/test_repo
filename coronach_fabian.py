#%%
import pandas as pd

df=pd.read_excel('https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx', skiprows=6)

df.dropna()

df.describe()

df['Fallzahlen pro Tag'].plot.line()

df['Fallzahlen pro Tag, kumuliert'].iloc[-1]

df['Todesfälle pro Tag, kumuliert'].iloc[-1]

df['Todesfälle pro Tag, kumuliert'].iloc[-1] / df['Fallzahlen pro Tag, kumuliert'].iloc[-1] *100

df['bevoelkerung'] = 8606033

df['inzidenz'] = df['Fallzahlen pro Tag, kumuliert'] / df['bevoelkerung']*100000

datum = df['Datum'].iloc[-1].date()
infektionen_heute = df['Fallzahlen pro Tag'].iloc[-1]
hospitalisationen_heute = int(df['Hospitalisationen pro Tag'].iloc[-1])
todesfaelle_heute = int(df['Todesfälle pro Tag'].iloc[-1])

df['inzidenz'] = df['Fallzahlen pro Tag, kumuliert'] / df['bevoelkerung']*100000
inzidenz_heute = df['inzidenz'].iloc[-1]

infektionen_7 = int(df['Fallzahlen pro Tag'].iloc[-7:].mean())
hospitalisationen_7 = int(df['Hospitalisationen pro Tag'].iloc[-7:].mean())
todesfaelle_7 = int(df['Todesfälle pro Tag'].iloc[-7:].mean())
inzidenz_7 = int(df['inzidenz'].iloc[-7:].mean())

infektionen_tot = df['Fallzahlen pro Tag, kumuliert'].iloc[-1]
hospitalisationen_tot = df['Hospitalisationen pro Tag, Kumuliert'].iloc[-1]
todesfaelle_tot = df['Todesfälle pro Tag, kumuliert'].iloc[-1]

if hospitalisationen_heute == 1:
  hosptext = "Person musste"
else:
  hosptext = "Personen mussten"

datumus = pd.Timestamp.date(df['Datum'].iloc[-1])
datumch = datumus.strftime(format = "%d.%m.%Y")

titel = "Tagesübersicht vom {}".format(datumch)

print(titel)

mein_text = "\nHeute meldet das Bundesamt für Gesundheit für die vergangenen 24 Stunden {} Infektionen mit dem neuartigen Coronavirus. {} {} hospitalisiert werden und {} Todesfälle zählt das BAG als Folge einer Corona-Infektion. Die Inzidenz beläuft sich auf {} Fälle pro 100 000 Einwohner. Im Durchschnitt der letzten 7 Tage steckten sich täglich {} Personen mit dem neuartigen Coronavirus an, {} Personen mussten hospitalisiert werden und {} Menschen starben an den Folgen der Infektion. Die Inzidenz im 7-Tage-Schnitt beläuft sich auf {} pro 100 000 Einwohner. Seit Beginn der Pandemie gab es in der Schweiz {} positive Corona-Tests. Insgesamt {} Personen mussten aufgrund einer Infektion ins Spital eingeliefert werden und {} Personen sind bisher an den Folgen an einer Corona-Infektion verstorben.".format(infektionen_heute, hospitalisationen_heute, hosptext, todesfaelle_heute, inzidenz_heute, infektionen_7, hospitalisationen_7, todesfaelle_7, inzidenz_7, infektionen_tot, hospitalisationen_tot, todesfaelle_tot)

print(mein_text)

df.sort_values(by='Fallzahlen pro Tag', ascending = True).dropna()

datum_fallzahlen_max = df.sort_values(by='Fallzahlen pro Tag', ascending = True).iloc[-1].Datum.date().strftime(format = "%d.%m.%Y")
fallzahlen_max = df.sort_values(by= 'Fallzahlen pro Tag', ascending = True).iloc[-1]

fallzahlen_max_text = (fallzahlen_max['Fallzahlen pro Tag'])

print(fallzahlen_max_text)

mein_text2 = "Am meisten positive Tests, nämlich {}, wurden am {} gemeldet.".format(fallzahlen_max_text, datum_fallzahlen_max)

print(mein_text2)

hospitalisationen_max = df.sort_values(by= 'Hospitalisationen pro Tag', ascending = True).iloc[-1]
datum_hosp_max = (hospitalisationen_max['Datum'].date()).strftime(format = "%d.%m.%Y")
hosp_max_text = int((hospitalisationen_max['Hospitalisationen pro Tag']))

todesfaelle_max =df.sort_values(by= 'Todesfälle pro Tag', ascending = True).dropna().iloc[-1]
datum_tod_max = (todesfaelle_max['Datum'].date()).strftime(format = "%d.%m.%Y")
tod_max_text = todesfaelle_max['Todesfälle pro Tag']

mein_text3 = "Mit {} gemeldeten Hospitalisationen wurden am {} am meisten Personen wegen Covid-19 ins Spital eingeliefert. Am {} sind laut BAG-Daten mit {} am meisten Menschen an Corona verstorben.".format(hosp_max_text, datum_hosp_max, datum_tod_max, int(tod_max_text) )

print(mein_text3)

print(mein_text, mein_text2, mein_text3)

#Ab hier Aufgabe 2

df_kantone=pd.read_excel('https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx',sheet_name=2, skiprows= 6, skipfooter = 2 )

kantone = pd.read_csv('https://raw.githubusercontent.com/stagis-tech/test_repo/main/kantone.csv', sep=";")

df_kantone_neu = pd.merge (df_kantone, kantone, left_on="Kanton", right_on="abk")

df_kantone_neu

# Relevant scheinen mir vor allem die Werte der letzten 14 Tage. Eine Inzidenz über den gesamten Verlauf der Pandemie erscheint mir wenig sinnvoll. Ich rechne deswegen mit den Spalten 'Bestätigte Fälle.1' und 'Inzidenz/100 000.1'

faelle_14_CH_tot = df_kantone['Bestätigte Fälle.1'].max()
faelle_kanton_max =  df_kantone_neu.sort_values(by = 'Bestätigte Fälle.1', ascending= True).iloc[-2].dropna()
faelle_kanton_max_wert= faelle_kanton_max['Bestätigte Fälle.1']
kanton_max = faelle_kanton_max['name'] 
anteil_kanton_max = int(100/df_kantone['Bestätigte Fälle.1'].max()*faelle_kanton_max_wert) #Prozentsatz der totalen Fälle im Kanton mit den meisten Fällen als Ganze Zahl.

print(anteil_kanton_max)

print(faelle_kanton_max)

faelle_kanton_min =  df_kantone_neu.sort_values(by = 'Bestätigte Fälle.1', ascending= False).iloc[-1].dropna()
faelle_kanton_min_wert = faelle_kanton_min['Bestätigte Fälle.1']
faelle_kanton_min_text = faelle_kanton_min['name'] + faelle_kanton_min[ 'Unnamed: 2' ]

print(faelle_kanton_min)

inzidenz_CH_tot =int(df_kantone['Inzidenz/100 000.1'].iloc[-1])
inzidenz_kanton_max =df_kantone_neu.sort_values(by = 'Inzidenz/100 000.1', ascending = True).iloc[-1].dropna()
inzidenz_kanton_max_wert = inzidenz_kanton_max['Inzidenz/100 000.1']
inzidenz_kanton_max_text = inzidenz_kanton_max['name'] 
vergleich_inzidenz_max = inzidenz_kanton_max_wert/inzidenz_CH_tot

print(inzidenz_kanton_max)

print(inzidenz_CH_tot)

print(vergleich_inzidenz_max)

inzidenz_kanton_min =df_kantone_neu.sort_values(by = 'Inzidenz/100 000.1', ascending = False).iloc[-1].dropna()
inzidenz_kanton_min_wert = inzidenz_kanton_min['Inzidenz/100 000.1']
inzidenz_kanton_min_text = inzidenz_kanton_min['name']
vergleich_inzidenz_min = inzidenz_kanton_min_wert/inzidenz_CH_tot

text_kantone_faelle_max = "\nÜber die letzten 14 Tage gerechnet wurden in der Schweiz insgesamt {} Fälle gemeldet. {} davon im Kanton {}. Somit meldet der Kanton {} mit {}% aller Fälle der Schweiz die meisten Neuinfektionen.".format(faelle_14_CH_tot, faelle_kanton_max_wert, kanton_max, kanton_max, anteil_kanton_max, )

print (text_kantone_faelle_max)

text_kantone_faelle_min = "Mit {} Fällen meldet der Kanton {} absolut gesehen am wenigsten Neuinfektionen über die letzten 14 Tage.".format(faelle_kanton_min_wert, faelle_kanton_min_text)

print(text_kantone_faelle_min)

text_inzidenz_max1 = "\nDie höchste Inzidenz weist jedoch der Kanton {} auf und meldet für die letzten 14 Tage eine Inzidenz von {} Neuinfektionen pro 100 000 Einwohner.".format(inzidenz_kanton_max_text, int(inzidenz_kanton_max_wert))

print(text_inzidenz_max1)

if inzidenz_kanton_max_wert > inzidenz_CH_tot:
  vergleicher = ("mal grösser als")
elif inzidenz_kanton_max_wert < inzidenz_CH_tot:
  vergleicher = (" mal kleiner als")
else:
  vergleicher = ("gleich gross wie")

print(vergleicher)

text_inzidenz_max2 = "Über die ganze Schweiz gesehen beträgt die Inzidenz {}. Somit ist die Inzidenz im Kanton {} {} {} die Inzidenz in der gesamten Schweiz.".format(int(inzidenz_CH_tot), inzidenz_kanton_max_text, round(vergleich_inzidenz_max, 2), vergleicher)

print(text_inzidenz_max2)

text_inzidenz_min = "Der Kanton {} hat mit {} noch die tiefste Inzidenz. Sie ist nur {} so hoch wie der Schweizer Durschnitt.".format(inzidenz_kanton_min_text,int(inzidenz_kanton_min_wert), round(vergleich_inzidenz_min, 2))

print(text_inzidenz_min)

#Alle Texte zusammen:
print(titel,mein_text, mein_text2, mein_text3,text_kantone_faelle_max,text_kantone_faelle_min,text_inzidenz_max1,text_inzidenz_max2,text_inzidenz_min,sep="\n")

#Wochenaufgabe 3:

dateiname = "fabian_kohler_corona.txt"

#text_file = open("./test_repos/" + dateiname, "w")
#text_file.write(titel,mein_text, mein_text2, mein_text3,text_kantone_faelle_max,text_kantone_faelle_min,text_inzidenz_max1,text_inzidenz_max2,text_inzidenz_min,sep="\n")
#text_file.close()

print ('Erledigt. ', dateiname, 'wurde hochgeladen.')


# %%
