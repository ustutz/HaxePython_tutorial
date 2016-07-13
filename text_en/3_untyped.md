#Haxe-Python Tutorial - untyped

**[Previous part: Basics]()**

Das letzte Beispiel hat gezeigt wie eine Funktion, die in Python so nicht vorhanden ist, in den generierten Python Code mit eingebaut wird.

In Python gibt es auch Funktionen um Variablen umzuwandeln. Um eine Variable zum Typ String zu konvertieren gibt es die Funktion `str()`, um eine Variable zum Typ Integer zu konvertieren gibt es die Funktion `int()`. Was ist also zu tun, um die nativen Funktionen direkt zu verwenden?

Eine Idee könnte sein, einfach die Python Funktionen in den Haxe Code zu schreiben. Ungefähr so:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = str( eight );
    		var int_ten = int( ten );
    	}
    }

Wer das ausprobiert bekommt aber vom Haxe Compiler zwei Fehler gemeldet:

    src/Main.hx:10: characters 18-21 : Unknown identifier : str  
    src/Main.hx:11: characters 16-19 : Unknown identifier : int
    
Die Funktionen `str()` und `int()` sind dem Compiler nicht bekannt.

Wir wissen aber, dass es diese Funktionen im Python Code geben wird. Um den Compiler ruhigzustellen gibt es das Keyword `untyped`, das wir vor den Funktionsaufruf schreiben:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = untyped str( eight );
    		var int_ten = untyped int( ten );
    	}
    }

Der Compile-Vorgang wird ohne Beanstandung durchgeführt. Der generierte Python Code sieht so aus:

    class Main:
    
    	@staticmethod
    	def main():
    		ten = "10"
    		eight = 8
    		str_eight = str(eight)
    		int_ten = int(ten)
    
    Main.main()
    
Bei Benutzung des `untyped` Keywords ist zu beachten, dass der Compiler den nachfolgenden Teil nicht auf Fehler überprüft.

Es wird nicht überprüft  

* ob Funktionen oder Variablen deklariert sind
* ob die Typen der Funktion oder der Variablen korrekt sind


**Next part: Syntax.pythonCode** (coming soon)


##Übersicht

* [Intro]()
* [Basics]()
* **untyped**
* Syntax.pythonCode (coming soon)