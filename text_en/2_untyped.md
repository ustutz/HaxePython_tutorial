#Haxe-Python Tutorial - untyped



![haxe to python](https://i.imgsafe.org/63afc9b8fb.png)

**[Previous part: Basics](https://steemit.com/programming/@kkaos/haxe-python-tutorial-basics)**

Das letzte Beispiel hat gezeigt wie eine Funktion, die in Python so nicht vorhanden ist, in den generierten Python Code mit eingebaut wird.

In Python gibt es auch Funktionen um Variablen umzuwandeln. Um eine Variable zum Typ String zu konvertieren gibt es die Funktion `str()`, um eine Variable zum Typ Integer zu konvertieren gibt es die Funktion `int()`. Was ist also zu tun, um die nativen Funktionen direkt zu verwenden?

<h3>3. Konvertieren von Variablentypen mit den Python Funktionen</h3>

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

Wer das ausprobiert bekommt vom Haxe Compiler zwei Fehler gemeldet:

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

Der Compile-Vorgang wird ohne Beanstandung durchgeführt. Der generierte Python Code sieht folgendermassen aus:

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

Andere Beispiele für `untyped` gibt es z.B. wenn Funktionen in eigenen extern Klassen nicht definiert sind, oder für Matrix Multiplikationen mit NumPy. Doch dazu in einem späteren Teil mehr.

Es gibt noch eine Steigerung zu `untyped`. Manchmal ist es gewünscht, den Code genauso wie er geschrieben wurde in den Python Sourcecode zu übertragen. Das einfachste Beispiel dafür ist bei Kommentaren.

**Nächster Teil: Syntax.pythonCode()**

   
<h3>Übersicht</h3>

* Intro
* Basics
* **untyped**
* Syntax.pythonCode()