#Haxe-Python Tutorial - Syntax.pythonCode

<h3>Writing Python sourcecode into the Haxe sourcecode.</h3>

![haxe to python](https://i.imgsafe.org/e1a5de8b18.jpg)

[**Overview**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-intro)

[**Previous part: untyped**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-untyped)

Es kann vorkommen, dass man bestimmte Teile des Quellcodes genauso zu Python übertragen möchte, z.B. bei der Benutzung von Programmbibliotheken wie NumPy oder Pandas. Dazu gibt es die Funktion `Syntax.pythonCode()`. Am einfachsten lässt sich das anhand von Kommentaren zeigen.

Beim Compilevorgang werden normalerweise alle Kommentare entfernt. Um in den erzeugten Python Quellcode Kommentare einzufügen, können sie innerhalb von Anführungszeichen in die Funktion `Syntax.pythonCode()` geschrieben werden.

    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		
    		// This comment is removed by the compiler
    		Syntax.pythonCode( "# This comment is inserted in the Python code" );
    		var a = 1;
    	}
    	
    }

Hier das Ergebnis nach dem Compilieren:
    
    class Main:
    
    	@staticmethod
    	def main():
    		# This comment is inserted in the Python code
    		a = 1

    Main.main()
    
Bei der Benutzung  von `Syntax.pythonCode()` können leicht Fehler in Python entstehen, z.B. durch Optimierungen des Haxe Compilers, die nicht immer vorherzusehen sind. Deshalb sollte die Funktion am besten möglichst sparsam angewendet werden.

<h3>Beispiele bei denen Fehler entstehen</h3>

<h4>1. Klassen Variablen</h4>

Bei Klassen Variablen wird in Python der Klassen-Name zum Variablen-Namen hinzugefügt.  

	package;    
	import python.Syntax;
    
    class Main {
    	static var a:String;
    	
    	static function main() {
    		a = "Hello!";
    		Syntax.pythonCode( "print(a)" );
    	}
    }

Der Variablenname `a` wird zu `Main.a`. Wenn also innerhalb von `Syntax.pythonCode()` die Variable `a` angesprochen wird, ist sie nicht definiert.

    class Main:
    	a = None
    
    	@staticmethod
    	def main():
    		Main.a = "Hello!"
    		print(a)
    
    Main.main()

Der Python Interpreter meldet einen Fehler

    NameError: name 'a' is not defined



<h4>2. Array Compiler Optimierung</h4>

Hier ein Beispiel für eine Compiler Optimierung:

    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		var a = [ 1, 2, 3 ];
    		Syntax.pythonCode( "print( a[2] )" );
    	}
    	
    }
    
Der Array `a` wird in diesem Beispiel wegoptimiert weil er nicht nötig ist. Die Variablennamen werden einfach mit einem Index versehen.

    class Main:
    
    	@staticmethod
    	def main():
    		a_0 = 1
    		a_1 = 2
    		a_2 = 3
    		print( a[2] )
    
    Main.main()
    
Der Python Interpreter meldet wieder einen Fehler

    NameError: name 'a' is not defined

Mit ein bisschen Python Grundwissen lassen sich solche Fehler aber leicht erkennen und beheben.

<h4>Aufruf mit Variablen</h4>
 
`Syntax.pythonCode()` kann nicht mit Variablen als Argument aufgerufen werden. Der einzufügende Text muss innerhalb von Anführungszeichen direkt in der Funktion stehen. So etwas funktioniert z.B. nicht:


    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		var test = "This doesn't work.";
    		Syntax.pythonCode( test );
    	}
    }

Der Python Sourcecode:

    class Main:
    
    	@staticmethod
    	def main():
    		test = "This doesn't work"
    		python_Syntax._pythonCode(test,[])
    
    Main.main()
    
Der Compiler versucht eine `python_Syntax._pythonCode` Klasse einzubinden. Die jedoch in Python nicht existiert und deshalb zu einem Fehler führt.


Beide bisher beschriebenen Möglichkeiten `untyped` und `Syntax.pythonCode()` können auch benutzt werden um Funktionen in externe Python Klassen aufzurufen. Dafür gibt es aber noch eine elegantere Möglichkeit.


**Next part: writing externs (coming soon)**