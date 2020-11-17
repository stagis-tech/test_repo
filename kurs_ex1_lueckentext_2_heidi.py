#%%
# -*- coding: utf-8 -*-



##import packages 
import requests
import pandas as pd
import io
from datetime import date, timedelta
from bs4 import BeautifulSoup
import json

#%%
##import data
#import Covid-19 data released by BAG
r = requests.get('https://www.covid19.admin.ch/api/data/context')
BAGcases_link = json.loads(r.text)['sources']['individual']['csv']['daily']['cases']
BAGcases = pd.read_csv(BAGcases_link)
BAGcasesCH=BAGcases.loc[BAGcases['geoRegion']=='CH']
##want entries (cases total cases today, yesterday etc) and sumTotal (total cumulative cases)

BAGtests_link = json.loads(r.text)['sources']['individual']['csv']['daily']['test']
BAGtests = pd.read_csv(BAGtests_link)
BAGtestsCH=BAGtests.loc[BAGtests['geoRegion']=='CH']
##want entries (total (positive) tests reported today  -  can't figure out where to find them. There is no column for new entries) ps_anteil (positivitätsrate)

BAGdeaths_link = json.loads(r.text)['sources']['individual']['csv']['daily']['death']
BAGdeaths = pd.read_csv(BAGdeaths_link)
BAGdeathsCH=BAGdeaths.loc[BAGdeaths['geoRegion']=='CH']
##want entrie (deaths), sumTotal (cumulative deaths)

##import data
#import SwissCovid App data 
url='https://www.experimental.bfs.admin.ch/bfsstatic/dam/assets/13407769/master'
dataset = requests.get(url, verify=False).content
SCAdat = pd.read_csv(io.StringIO(dataset.decode('utf-8')), sep=',')

print(SCAdat.dtypes) 
SCAdat   ##NOTE: latest data from yesterday

##Calculate number of new cases reported today
##Ich weiss nicht woher die Zahl der täglich neu gemeldeten laborbestätigten Fälle kommt (am 16.11.: 12'839). Denn mit dem Befehl unten fasse ich alle am 16.11. neu gemeldeten Fälle zusammen - und das gibt 13'530!
Cases_new=BAGcasesCH['entries_neu_gemeldet'].sum() 
Cases_new

##report positivity rate on 7-day average
RatePos_testTD=round(BAGtestsCH['pos_anteil_mean7d'].dropna().iloc[-1],1)
RatePos_testTD

##report average number cases over last seven days (excluding today)  -  does not really make sense because the three last days will have more cases reported as they catch up with processing tests
Cases_7d=round(int(BAGcasesCH['entries'][-8:-1].mean()),0)
Cases_7d

Cases_14d=round(int(BAGcasesCH['entries'][-16:-9].mean()),0)
Cases_14d

Case_percChange=round((100/Cases_14d)*Cases_7d-100,1)
Case_percChange

##Number of active SwissCovid-Apps and percentage of the 3 Mio apps that could/should be active
AppsWanted=3
SCAactive=round(SCAdat['active_apps_total_new'].iloc[-1]/1000000,2)
SCAperc=round((100/AppsWanted)*SCAactive,1)

##translate Canton abbreviations
canton_abbrev = {
    'AG': 'Aargau',
    'AI': 'Appenzell Innerrhoden',
    'AR': 'Appenzell Ausserrhoden',
    'BE': 'Bern',
    'BL': 'Basel Landschaft',
    'BS': 'Basel Stadt',
    'FR': 'Freiburg',
    'GE': 'Genf',
    'GL': 'Glarus',
    'GR': 'Graubünden',
    'JU': 'Jura',
    'LU': 'Luzern',
    'NE': 'Neuenburg',
    'NW': 'Nidwalden',
    'OW': 'Obwalden',
    'SG': 'St. Gallen',
    'SH': 'Schaffhausen',
    'SO': 'Solothurn',
    'SZ': 'Schwyz',
    'TG': 'Thurgau',
    'TI': 'Tessin',
    'UR': 'Uri',
    'VD': 'Waadt',
    'VS': 'Wallis',
    'ZG': 'Zug',
    'ZH': 'Zürich'
}

##Which Canton is most affected? (Extract other sheets from the BAG excel file)
MaxDatum=BAGcases[BAGcases['datum']==BAGcases['datum'].max()]

MaxDatum=MaxDatum.iloc[2:]

Cantonmax=MaxDatum[MaxDatum['inz_entries']==MaxDatum['inz_entries'].max()]['geoRegion'].item()
CantonmaxInz=MaxDatum[MaxDatum['inz_entries']==MaxDatum['inz_entries'].max()]['inz_entries'].item()

Cantonmax=canton_abbrev[Cantonmax]

##define date and days of the week 
date=date.today()
datum = date.strftime("%d/%m/%Y")
weekDays = ("Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag")

TD=date.today()
TD=TD.weekday()
TD=weekDays[TD]

TD

##Evaluate positive rate
if RatePos_testTD > 7.5:
  Pos_testTD_eval='deutlich über den von der WHO empfohlenen 5 %. Die Anzahl Erkrankter wird wahrscheinlich unterschätzt.'
elif Pos_testTD > 5:
  Pos_testTD_eval='über den von der WHO empfohlenen 5 %. Die Anzahl Erkrankter wird vielleicht unterschätzt.'
else: 
  Pos_testTD_eval='innerhalb der von der WHO empfohlenen 5 %. Die Anzahl Erkrankter kann relativ genau geschätzt werden.'

##Text

header = "Corona-Briefing vom {}".format(datum)
weekend = "\n\nDas BAG veröffentlich am Wochenende leider keine Daten. Am Montag-Mittag können wir Sie über den neusten Stand informieren."

body="\n\nHeute meldeten die Labore total {} neue Fälle. Diese neu diagnostizierten Fälle verteilen sich auf die vergangenen Tage.".format(Cases_new)
body0="\nDie durchschnittliche Positivitätsrate der letzten sieben Tage liegt bei {} %. Das liegt {}".format(RatePos_testTD, Pos_testTD_eval)
body1="\nIn den letzten sieben Tagen wurden pro Tag durchschnittlich {} Fälle gemeldet. Das sind {} % weniger als im Vergleich zum Durchschnitt der sieben Tage davor ({}).".format(Cases_7d, Case_percChange, Cases_14d)
body2="\n\nGestern waren {} Mio. SwissCovid-Apps aktiv. Das sind {} % der erwünschten 3 Mio. aktiven Apps. ".format(SCAactive, SCAperc)
body3="\n\nDer aktuell am stärksten betroffene Kanton ist zurzeit {} mit {} Fällen pro 100'000 Einwohner*innen.".format(Cantonmax, CantonmaxInz)
body4="\n"

dateiname = "heidi_test1.txt"
#%%

text_file = open("./test_repo/" + dateiname, "w")
#if date.today().strftime('%Y-%m-%d')!=BAGcasesCH['datum'].iloc[-1]: 
  #text_file.write("%s\n%s\n" % (header, weekend))

#else:
#  text_file.write("%s\n%s\n%s\n%s\n%s\n%s\n" % (header, body, body0, body1, body2, body3))
#
text_file.write("%s\n%s\n%s\n%s\n%s\n%s\n" % (header, body, body0, body1, body2, body3))
text_file.close()


print ('Erledigt. ', dateiname, 'wurde hochgeladen.')

