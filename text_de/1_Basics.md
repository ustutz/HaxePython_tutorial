#Haxe-Python Tutorial - Basics

![haxe to python](https://i.imgsafe.org/e1a5de8b18.jpg)

[Zurück zum Intro]()

Fangen wir mal mit einem sehr einfachen Beispiel an um zu zeigen was der Haxe Compiler generiert.   

###1. Variablen

Variablen sind wahrscheinlich Bestandteil jeder Programmiersprache. Sie erlauben die Zuweisung von Werten.

Hier der Haxe Sourcecode:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var a = 5;
    		var b = 6.2;
    		var d = true;
    		var greeting = "Hello";
    	}
    }
                
Und hier der daraus erzeugte Python Sourcecode:    

    class Main:
    
    	@staticmethod
    	def main():
    		a = 5
    		b = 6.2
    		d = True
    		greeting = "Hello"
    
    Main.main()
    
Bisher also nichts überraschendes. Der Sourcecode wurde Zeile für Zeile in Python übersetzt.

Interessanter wird es wenn es entweder eine Funktionalität von Haxe in Python nicht vorhanden ist, oder wenn eine Funktionalität von Python in Haxe nicht vorkommt.

###2. Typ einer Variable umwandeln

In diesem Beispiel wird die Variable `eight` in einen String umgewandelt und die Variable `ten` wird zum Typ Integer konvertiert.

    package;
    
    class Main {
    
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = Std.string( eight );
    		var int_ten = Std.parseInt( ten );
    	}
    }
    
    
Der Python Sourcecode wird plötzlich sehr viel länger. Hier nur ein kurzer Ausschnitt. Der vollständige Code ist mit diesem Link zu sehen: [Typeconversion.py](https://github.com/ustutz/HaxePython_tutorial/blob/master/code/2_Type_conversion/bin/Typeconversion.py) 

    import math as python_lib_Math
    import math as Math
    import inspect as python_lib_Inspect
    
    
    class Enum:
    	_hx_class_name = "Enum"
    	_hx_fields = ["tag", "index", "params"]
    	_hx_methods = ["__str__"]
    
    	def __init__(self,tag,index,params):
    		self.tag = None
    		self.index = None
    		self.params = None
    		self.tag = tag
    		self.index = index
    		self.params = params
    
    	def __str__(self):
    		if (self.params is None):
    			return self.tag
    		else:
    			return (((HxOverrides.stringOrNull(self.tag) + "(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in self.params]))) + ")")
    
    
    
    class Main:
    	_hx_class_name = "Main"
    	_hx_statics = ["main"]
    
    	@staticmethod
    	def main():
    		ten = "10"
    		eight = 8
    		str_eight = Std.string(eight)
    		int_ten = Std.parseInt(ten)
    
    
    class Std:
    	_hx_class_name = "Std"
    	_hx_statics = ["string", "parseInt", "shortenPossibleNumber", "parseFloat"]
            ...

Was ist passiert?  

Die Funktionen `Std.string` und `Std.int` sind in Python nicht vorhanden. Der Haxe Compiler hat die komplette Funktionalität aber in den Python Sourcecode mit eingefügt. Auch die Main Klasse ist noch zu finden. In dem Code-Ausschnitt kurz vor Ende.

Leider wird der Python Code durch die ganzen Zusätze nicht mehr sehr einfach zu lesen. Das ist auch der Grund wieso es oft nicht sehr sinnvoll ist, mit dem Python Sourcecode weiterzuarbeiten.

Wer sich etwas in Python auskennt weiss vielleicht, dass es auch eine Python Funktion gibt um Variablen in einen anderen Typ zu konvertieren. Wie kann man nun direkt diese Funktion benutzen?

[Weiter zu untyped]()

        
##Übersicht

* [Intro]()
* **Basics**
* [untyped]()
* [python.Syntax.pythonCode]()