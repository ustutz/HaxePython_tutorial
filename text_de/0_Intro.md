#Haxe-Python Tutorial - Intro

####Dieses Tutorial ist für Programmierer mit Vorkenntnissen in der Haxe Programmiersprache gedacht. Es zeigt die Anwendung des Python Compile-Targets.

Bei einem meiner aktuellen Projekte ist eine der Herausforderungen, eine große Menge an Daten auszuwerten. Die Programmiersprache Python ist dafür sehr gut geeignet weil es viele hervorragende Programm-Bibliotheken für Python gibt, die diese Aufgabe sehr erleichtern. Der logische nächste Schritt wäre also, Python zu lernen um damit die Datenauswertung zu programmieren. Natürlich  wär das aber sehr zeitaufwändig.

Da ich mit der Haxe Programmiersprache arbeite, gibt es noch eine andere Möglichkeit. Eine Besonderheit von Haxe ist es, dass es mehrere Compile-Targets gibt. Der Source-Code von Haxe wird vom Compiler in den Source-Code von anderen Programmiersprachen übersetzt. Zum jetzigen Zeitpunkt (Juli 2016) gibt es 10 verschieden Compile Targets. Eins davon is Python.

Das bedeutet, ich kann die Datenauswertung wie gewohnt in Haxe programmieren. Der Compiler erzeugt daraus Python Source-Code, der dann ganz normal vom Python Interpreter ausgeführt wird. Auch eine Ansteuerung der Python Libraries ist möglich. 

Das Python Compile Target ist jedoch noch relativ neu und in Python gibt es einige Besonderheiten, die sich nicht 1x1 auf Haxe übertragen lassen. Die Möglichkeiten, die ich entdeckt habe möchte ich in dieser Tutorial Serie zeigen.

##Voraussetzungen

* Grundlagen in der Haxe Programmiersprache und dem Umgang mit dem Haxe Toolkits. Eine gute Einführung gibt es auf [Haxe.org](http://haxe.org/documentation/introduction/)
* Grundlagen der Python Programmiersprache. Eine gute Einführung gibt es auf [learnpython.org](http://www.learnpython.org/)

##Benötigte Software

* [Haxe Toolkit](http://haxe.org/) ab Version 3.3  
* [HaxeDevelop](http://haxedevelop.org/) für Windows
  oder irgendeine andere [Haxe Entwicklungsumgebung](http://haxe.org/documentation/introduction/editors-and-ides.html) für Linux oder Mac .
* [Python 3.+](https://www.continuum.io/downloads) Ich benutze das Python Paket von [Anaconda](https://www.continuum.io/why-anaconda) weil da die wichtigen Libraries mit installiert werden. Wichtig ist es, das Python 3.5 Paket oder ein neueres zu installieren, da aus Haxe kein Python 2.7 Code erstellt werden kann.

## Ressourcen

Hier sind einige Ressourcen aufgelistet die mir sehr weitergeholfen haben

* [dataquest.io](https://www.dataquest.io/) - Hervorragender Online Kurs zum Thema DataScience in Pyhon.
* [github.com/ustutz/Dataquest](https://github.com/ustutz/Dataquest) - meine Lösungen der Dataquest Missionen in Haxe.
* [PyCon HK 2015](https://haxe.io/@andy_li/PyCon%20HK%202015.pdf) - Haxe-Python Präsentation von Andy Li an der Python Konferenz 2015 in Honkkong.
* [PyHelpers.hx](https://github.com/andyli/haxe-usage-survey/blob/master/src/PyHelpers.hx) - Haxe Macro, das die Arbeit beim Aufruf von externen Python Funktionen sehr vereinfacht.
* [Haxe-usage-survey](https://github.com/andyli/haxe-usage-survey) - Auswertung einer Umfrage zur Benutzung von Haxe von Andi Li.
* [Extern generator for the Haxe Python target](https://github.com/andyli/pyextern) von Andy Li.

##Github
Die ganzen Texte und der Sourcecode dieser Tutorials sind auch auf Github verfügbar. Falls jemand Fehler findet oder Verbesserungsvorschläge hat.  

* [Repository](https://github.com/ustutz/HaxePython_tutorial) - zum Clonen, für Issues oder Pull Requests
* [Sourcecode](https://github.com/ustutz/HaxePython_tutorial/tree/master/code) - der Beispiele

##Übersicht
* Intro
* [Basics]()
* [untyped]()

