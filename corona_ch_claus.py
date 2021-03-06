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

Mein_Text = "Heute {} meldet das Bundesamt für Gesundheit (BAG) für die vergangenen 24 Stunden {} Neuinfektionen mit dem Coronavirus. {} Personen mussten hospitalisiert werden. {} Personen verstarben an Covid-19. In den letzten 7 Tagen gab es durchschnittlich {} Neuinfektionen pro Tag, {} Personen mussten hospitalisiert werden und {} Menschen verstarben. Seit Beginn der Pandemie infizierten sich {} Menschen. Es wurden gesamthaft {} Personen hospitalisiert und {} Menschen verstarben.".format(Datum, Neuinfektionen_heute, Hospitalisationen_heute, Todesfälle_heute, Durchschnitt_Woche_Neuinfektionen, Durchschnitt_Woche_Hospitalisationen, Durchschnitt_Woche_Todesfälle, Infektionen_Total, Hospitalisationen_Total, Todesfälle_Total)

print (Mein_Text)

dateiname = "claus_test1.txt"

text_file = open("./test_repo/reports/" + dateiname, "w")
text_file.write(Mein_Text)
text_file.close()

print ('Erledigt')
