class Main {
	
	static var a:Int;
	static var b:Int;
	
	static function main() {
		
		a = 10;
		b = 5;
		python.Syntax.pythonCode("print('The value of a is ' + {0} + ' and the value of b is ' + {1})", Std.string(a), String(b));
	}
}

