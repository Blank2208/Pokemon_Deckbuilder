Moin :) <br>

Da unser Code ein wenig unübersichtlich ist, geben wir euch zum Überblick diese ReadMe-Datei mit. :) <br>

Im Ordner "API_to_CSV" befinden sich alle Files, die wir zur Kartendatensatzerhebung genutzt haben. Also die Files, die es uns erlauben, von der API die ganzen Kartendatensätze zu bekommen. Anschließend haben wir diese dann in mehrere CSV-Dateien gespeichert. <br>

Im Ordner "Create_Deck" befindet sich der Deckbuilder, also die Datei die ausgeführt werden muss, um sich ein Deck generieren zu lassen. Wichtig dabei zu beachten ist: <br>
- Unter "Anleitung" befinden sich einige Informationen über den Ablauf der Funktionen innerhalb der "Deckbuilder.py"-File
- In "initial_deck.py" haben wir zu fast jeder Funktion Kommentare ergänzt. In den if-Zweigen haben wir Kommentare wie "Insgesamt: Pokemon: x, Trainer: x, Energy: x" geschrieben. Dies haben wir zur Orientierung gemacht. Je nachdem, wie das Dict bzw. die Zuweisungen zum Beginn des jeweiligen Decks geändert wird, müssen auch "random.sample(pokemon_cards, x)", "random.sample(trainer_cards, x)" und "random.sample(energy_cards, x)" angepasst werden, da die Gesamtzahl aller Karten genau 60 Karten betragen muss!
- Je nach Nutzereingabe wird "<typ>_pokemon_cards.csv" aufgerufen. Diese CSV-Dateien beinhalten alle Pokemon-Karten, welche mit dem Pokemon-Typen der Nutzereingabe übereinstimmt. --> Die Pokemon im Deck werden immer mit den Pokemon ausgetauscht, welche sich in der CSV-Datei befinden.
- Das beste Deck wird dann in "best_deck.csv" gespeichert bzw. das Deck, was der Nutzer mit "ja" bestätigt.
<br>

Im Ordner "Diagrams" befinden sich die Files, womit wir die Statistiken der Kartenverteilung ermittelt haben (Die Diagramme, welche wir in unserer Dokumentationsarbeit und in der Präsentation benutzt haben). <br>

Im Ordner "web_scraping" befinden sich die Files zur Erstellung der Assoziationsregeln. Dabei gilt folgendes: <br>
- Im Unterordner "Assoziationsregeln" befinden sich die Decklisten, aus denen wir die Typen-Assoziationsregeln erstellt haben und die CSV-Dateien, welche wir erhalten haben, als wir den FP-MAX-Algorithmus genutzt haben (Dies war für das Dict wichtig, wo wir die "wichtigsten" Karten bereits bei der Deckerstellung mitgeben
- Im Unterordner "decklisten" befinden sich alle unsere genutzten Decklisten, die wir von Limitless genommen haben. Die Decks haben wir dort noch nicht in ihre Pokemon-Typen gegliedert. "decks_anpassung.csv" ist dabei die CSV-Datei, welche wir momentan nutzen.
- Im Unterordner "functions" befinden sich alle Funktionen, welche wir im Ordner "web_scraping" genutzt haben. Da wir das Refactoring zur Übersicht gemacht haben, als wir bereits "fertig" gewesen sind, kann es sein, dass man bei der Ausführung der Files die input-Wege anpassen muss.
<br>

Die Files, welche sich in keinem Ordner befinden, sind Überreste (*Hier bitte das Pokemon-Item als Bild einfügen*) von unseren Anfängen. Dabei ist lediglich wichtig die "panda_einstellung.py"-File zu behalten, sofern man mit dem Terminal arbeitet. Dadurch sieht man mehr Einträge.
<br>
Ansonsten bleibt uns nur noch zu sagen, dass wir die Python 3.13 Version nutzen. <br>

Für aufkommende Fragen stehe ich (Tom) gerne zur Verfügung. Sowohl auf Discord, als auch über E-Mail. :)










