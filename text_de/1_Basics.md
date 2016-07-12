#Haxe-Python Tutorial - Basics

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
    
Bisher also nichts überraschendes. Der Sourcecode wurde Zeile für Zeile in Python übersetzt. Interessanter wird es wenn es entweder eine Funktionalität von Haxe in Python nicht vorhanden ist, oder wenn eine Funktionalität von Python in Haxe nicht vorkommt.

###2. Typ einer Variable auslesen

In diesem Beispiel wird der Typ der variable a ausgelesen.

    package;
    
    import python.Lib;
    
    class Main {
    	
    	static function main() {
    		
    		var a = 5;
    		
    		var typeOfA = Type.typeof( a );
    	}
    	
    }
    
    
    
##Links

* [Intro]()
* Basics
