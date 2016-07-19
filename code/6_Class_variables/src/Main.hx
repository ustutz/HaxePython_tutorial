package;
import python.Syntax;

class Main {
	static var a:String;
	
	static function main() {
		a = "Hello!";
		Syntax.pythonCode( "print(a)" );
	}
}