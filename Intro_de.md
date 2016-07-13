#Haxe-Python Tutorial

####Dieses Tutorial ist für Programmierer mit Vorkenntnissen in der Haxe Programmiersprache gedacht. Es zeigt die Besonderheiten des Python Compile-Targets.

Bei einem meiner aktuellen Projekte ist eine der Herausforderungen, eine große Menge an Daten auszuwerten. Die Programmiersprache Python ist dafür sehr gut geeignet weil es viele hervorragende Programm-Bibliotheken für Python gibt, die diese Aufgabe sehr erleichtern. Der logische nächste Schritt wäre also, Python zu lernen um damit die Datenauswertung zu programmieren. Natürlich  wär das aber sehr zeitaufwändig.

 Da ich mit der Haxe Programmiersprache arbeite, gibt es noch eine andere, bessere Möglichkeit. Eine Besonderheit von Haxe ist es, dass es mehrere Compile-Targets gibt. Der Source-Code von Haxe wird vom Compiler in den Source-Code von anderen Programmiersprachen übersetzt. Zum jetzigen Zeitpunkt (Juni 2016) gibt es 10 verschieden Compile Targets. Eins davon is Python.

Das bedeutet, ich kann die Datenauswertung wie gewohnt in Haxe programmieren. Der Compiler erzeugt daraus Python Source-Code, der dann ganz normal vom Python Interpreter ausgeführt wird. Auch eine Ansteuerung der Python Libraries ist möglich. 

Das Python Compile Target ist jedoch noch relativ neu und in Python gibt es einige Besonderheiten, die sich nicht  