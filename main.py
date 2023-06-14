from fflogsapi.client import FFLogsClient
from fflogsapi.util.gql_enums import GQLEnum
import matplotlib.pyplot as plt
#using client id and client secret to access api
client = FFLogsClient('995e65fb-ee35-42a4-9dd8-edc7d6d1a00c', 'bEPqdAvnTYOeYqsGS72Czyh93otJ19ok7m4Up82j')
#setting encounter specifically with the id
encounternine = client.get_encounter(id = 88)
# setting the fight to filter for savage difficulty rankings as well as the metric chosen
encrankingsrdpsnine = encounternine.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('rdps'),
})

encrankingsndpsnine = encounternine.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('ndps'),
})

encrankingshpsnine = encounternine.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

#p10 variables
encounterten = client.get_encounter(id = 89)

encrankingsrdpsten = encounterten.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('rdps'),
})

encrankingsndpsten = encounterten.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('ndps'),
})

encrankingshpsten = encounterten.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

#p11 variables
encountereleven = client.get_encounter(id = 90)

encrankingsrdpseleven = encountereleven.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

encrankingsndpseleven = encountereleven.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

encrankingshpseleven = encountereleven.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

#p12p1 variables
encountertwelveone = client.get_encounter(id = 91)

encrankingsrdpstwelveone = encountertwelveone.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})
encrankingsndpstwelveone = encountertwelveone.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})
encrankingshpstwelveone = encountertwelveone.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})

#p12p2 variables
encountertwelvetwo = client.get_encounter(id = 92)

encrankingsrdpstwelvetwo = encountertwelvetwo.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('rdps'),
})
encrankingsndpstwelvetwo = encountertwelvetwo.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('ndps'),
})
encrankingshpstwelvetwo = encountertwelvetwo.character_rankings(filters={
    'difficulty': 101,
    'metric': GQLEnum('hps'),
})
client.close()
client.save_cache()
print(encrankingshpstwelvetwo)

#changing the dictionary into a list
encrankingslistone = list(encrankingsrdpsnine.items())
encrankingslistonefilter = []
listone = []
listtwo = []
for metric in encrankingsrdpsnine['rankings']:
    if metric['amount'] or metric['startTime']:
       listone.append(metric['amount'])
       listtwo.append(metric['startTime'])

encrankingslisttwo = list(encrankingsndpsnine.items())
encrankingslisttwofilter = []
listthree = []
listfour = []
for metric in encrankingsndpsnine['rankings']:
    if metric['amount'] or metric['startTime']:
       listthree.append(metric['amount'])
       listfour.append(metric['startTime'])

encrankingslistthree = list(encrankingshpsnine.items())
encrankingslistthreefilter = []
listfive = []
listsix = []
for metric in encrankingshpsnine['rankings']:
    if metric['amount'] or metric['startTime']:
       listfive.append(metric['amount'])
       listsix.append(metric['startTime'])

encrankingslistfour = list(encrankingsrdpsten.items())
encrankingslistfourfilter = []
listseven = []
listeight = []
for metric in encrankingsrdpsten['rankings']:
    if metric['amount'] or metric['startTime']:
       listseven.append(metric['amount'])
       listeight.append(metric['startTime'])

encrankingslistfive = list(encrankingsndpsten.items())
encrankingslistfivefilter = []
listnine = []
listten = []
for metric in encrankingsndpsten['rankings']:
    if metric['amount'] or metric['startTime']:
       listnine.append(metric['amount'])
       listten.append(metric['startTime'])

encrankingslistsix = list(encrankingshpsten.items())
encrankingslistsixfilter = []
listeleven = []
listtwelve = []
for metric in encrankingshpsten['rankings']:
    if metric['amount'] or metric['startTime']:
       listeleven.append(metric['amount'])
       listtwelve.append(metric['startTime'])

encrankingslistseven = list(encrankingsrdpseleven.items())
encrankingslistsevenfilter = []
listthirteen = []
listfourteen = []
for metric in encrankingsrdpseleven['rankings']:
    if metric['amount'] or metric['startTime']:
       listthirteen.append(metric['amount'])
       listfourteen.append(metric['startTime'])

encrankingslisteight = list(encrankingsndpseleven.items())
encrankingslisteightfilter = []
listfifteen = []
listsixteen = []
for metric in encrankingsndpseleven['rankings']:
    if metric['amount'] or metric['startTime']:
       listfifteen.append(metric['amount'])
       listsixteen.append(metric['startTime'])

encrankingslistnine = list(encrankingshpseleven.items())
encrankingslistninefilter = []
listseventeen = []
listeighteen = []
for metric in encrankingshpseleven['rankings']:
    if metric['amount'] or metric['startTime']:
       listseventeen.append(metric['amount'])
       listeighteen.append(metric['startTime'])

encrankingslistten = list(encrankingsrdpstwelveone.items())
encrankingslisttenfilter = []
listnineteen = []
listtwenty = []
for metric in encrankingsrdpstwelveone['rankings']:
    if metric['amount'] or metric['startTime']:
       listnineteen.append(metric['amount'])
       listtwenty.append(metric['startTime'])

encrankingslisteleven = list(encrankingsndpstwelveone.items())
encrankingslistelevenfilter = []
listtwentyone = []
listtwentytwo = []
for metric in encrankingsndpstwelveone['rankings']:
    if metric['amount'] or metric['startTime']:
       listtwentyone.append(metric['amount'])
       listtwentytwo.append(metric['startTime'])

encrankingslisttwelve = list(encrankingshpstwelveone.items())
encrankingslisttwelvefilter = []
listtwentythree = []
listtwentyfour = []
for metric in encrankingshpstwelveone['rankings']:
    if metric['amount'] or metric['startTime']:
       listtwentythree.append(metric['amount'])
       listtwentyfour.append(metric['startTime'])

encrankingslistthirteen = list(encrankingsrdpstwelvetwo.items())
encrankingslistthirteenfilter = []
listtwentyfive = []
listtwentysix = []
for metric in encrankingsrdpstwelvetwo['rankings']:
    if metric['amount'] or metric['startTime']:
       listtwentyfive.append(metric['amount'])
       listtwentysix.append(metric['startTime'])

encrankingslistfourteen = list(encrankingsndpstwelvetwo.items())
encrankingslistfourteenfilter = []
listtwentyseven = []
listtwentyeight = []
for metric in encrankingsndpstwelvetwo['rankings']:
    if metric['amount'] or metric['startTime']:
       listtwentyseven.append(metric['amount'])
       listtwentyeight.append(metric['startTime'])

encrankingslistfifteen = list(encrankingshpstwelvetwo.items())
encrankingslistfifteenfilter = []
listtwentynine = []
listthirty = []
for metric in encrankingshpstwelvetwo['rankings']:
    if metric['amount'] or metric['startTime']:
       listtwentynine.append(metric['amount'])
       listthirty.append(metric['startTime'])
#merging both lists into tuples
merged_listone = tuple(zip(listone, listtwo))
merged_listtwo = tuple(zip(listthree, listfour))
merged_listthree = tuple(zip(listfive, listsix))
merged_listfour = tuple(zip(listseven, listeight))
merged_listfive = tuple(zip(listnine, listten))
merged_listsix = tuple(zip(listeleven, listtwelve))
merged_listseven = tuple(zip(listthirteen, listfourteen))
merged_listeight = tuple(zip(listfifteen, listsixteen))
merged_listnine = tuple(zip(listseventeen, listeighteen))
merged_listten = tuple(zip(listnineteen, listtwenty))
merged_listeleven = tuple(zip(listtwentyone, listtwentytwo))
merged_listtwelve = tuple(zip(listtwentythree, listtwentyfour))
merged_listthirteen = tuple(zip(listtwentyfive, listtwentysix))
merged_listfourteen = tuple(zip(listtwentyseven, listtwentyeight))
merged_listfifteen = tuple(zip(listtwentynine, listthirty))
#sorting so that data is in ascending order with startTime int
merged_listone = sorted(merged_listone, key=lambda merged_listone: int(merged_listone[1]));
merged_listtwo = sorted(merged_listtwo, key=lambda merged_listtwo: int(merged_listtwo[1]));
merged_listthree = sorted(merged_listthree, key=lambda merged_listthree: int(merged_listthree[1]));
merged_listfour = sorted(merged_listfour, key=lambda merged_listfour: int(merged_listfour[1]));
merged_listfive = sorted(merged_listfive, key=lambda merged_listfive: int(merged_listfive[1]));
merged_listsix = sorted(merged_listsix, key=lambda merged_listsix: int(merged_listsix[1]));
merged_listseven = sorted(merged_listseven, key=lambda merged_listseven: int(merged_listseven[1]));
merged_listeight = sorted(merged_listeight, key=lambda merged_listeight: int(merged_listeight[1]));
merged_listnine = sorted(merged_listnine, key=lambda merged_listnine: int(merged_listnine[1]));
merged_listten = sorted(merged_listten, key=lambda merged_listten: int(merged_listten[1]));
merged_listeleven = sorted(merged_listeleven, key=lambda merged_listeleven: int(merged_listeleven[1]));
merged_listtwelve = sorted(merged_listtwelve, key=lambda merged_listtwelve: int(merged_listtwelve[1]));
merged_listthirteen = sorted(merged_listthirteen, key=lambda merged_listthirteen: int(merged_listthirteen[1]));
merged_listfourteen = sorted(merged_listfourteen, key=lambda merged_listfoureen: int(merged_listfoureen[1]));
merged_listfifteen = sorted(merged_listfifteen, key=lambda merged_listfifteen: int(merged_listfifteen[1]));
#split merged_list into two lists
listaone = []
listbone = []
for i in merged_listone:
   listaone.append(i[0])
   listbone.append(i[1])

listatwo = []
listbtwo = []
for i in merged_listtwo:
   listatwo.append(i[0])
   listbtwo.append(i[1])

listathree = []
listbthree = []
for i in merged_listthree:
   listathree.append(i[0])
   listbthree.append(i[1])

listafour = []
listbfour = []
for i in merged_listfour:
   listafour.append(i[0])
   listbfour.append(i[1])

listafive = []
listbfive = []
for i in merged_listfive:
   listafive.append(i[0])
   listbfive.append(i[1])

listasix = []
listbsix = []
for i in merged_listsix:
   listasix.append(i[0])
   listbsix.append(i[1])

listaseven = []
listbseven = []
for i in merged_listseven:
   listaseven.append(i[0])
   listbseven.append(i[1])

listaeight = []
listbeight = []
for i in merged_listeight:
   listaeight.append(i[0])
   listbeight.append(i[1])

listanine = []
listbnine = []
for i in merged_listnine:
   listanine.append(i[0])
   listbnine.append(i[1])

listaten = []
listbten = []
for i in merged_listten:
   listaten.append(i[0])
   listbten.append(i[1])

listaeleven = []
listbeleven = []
for i in merged_listeleven:
   listaeleven.append(i[0])
   listbeleven.append(i[1])

listatwelve = []
listbtwelve = []
for i in merged_listtwelve:
   listatwelve.append(i[0])
   listbtwelve.append(i[1])

listathirteen = []
listbthirteen = []
for i in merged_listthirteen:
   listathirteen.append(i[0])
   listbthirteen.append(i[1])

listafourteen = []
listbfourteen = []
for i in merged_listfourteen:
   listafourteen.append(i[0])
   listbfourteen.append(i[1])

listafifteen = []
listbfifteen = []
for i in merged_listfifteen:
   listafifteen.append(i[0])
   listbfifteen.append(i[1])
#plotting the graph for the data
plt.figure(1)
plt.plot(listbone,listaone)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphone.png'.format(i))

plt.figure(2)
plt.plot(listbtwo,listatwo)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphtwo.png'.format(i))

plt.figure(3)
plt.plot(listbthree,listathree)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphthree.png'.format(i))

plt.figure(4)
plt.plot(listbfour,listafour)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphfour.png'.format(i))

plt.figure(5)
plt.plot(listbfive,listafive)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphfive.png'.format(i))

plt.figure(6)
plt.plot(listbsix,listasix)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphsix.png'.format(i))

plt.figure(7)
plt.plot(listbseven,listaseven)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphseven.png'.format(i))

plt.figure(8)
plt.plot(listbeight,listaeight)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/grapheight.png'.format(i))

plt.figure(9)
plt.plot(listbnine,listanine)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphnine.png'.format(i))

plt.figure(10)
plt.plot(listbten,listaten)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphten.png'.format(i))

plt.figure(11)
plt.plot(listbeleven,listaeleven)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/grapheleven.png'.format(i))

plt.figure(12)
plt.plot(listbtwelve,listatwelve)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphtwelve.png'.format(i))

plt.figure(13)
plt.plot(listbthirteen,listathirteen)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphthirteen.png'.format(i))

plt.figure(14)
plt.plot(listbfourteen,listafourteen)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphfourteen.png'.format(i))

plt.figure(15)
plt.plot(listbfifteen,listafifteen)
plt.ylabel('Amount')
plt.xlabel('Start Time')
plt.savefig('static/graphfifteen.png'.format(i))