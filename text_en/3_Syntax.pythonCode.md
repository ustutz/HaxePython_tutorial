#Haxe-Python Tutorial - Syntax.pythonCode()

<h3>Writing Python sourcecode in the Haxe sourcecode.</h3>

![haxe to python](https://i.imgsafe.org/e1a5de8b18.jpg)

[**Overview**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-intro)

[**Previous part: untyped**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-untyped)

Sometimes it is necessary to transfer some parts of the source code exactly to Python, e.g. when using Python libraries like NumPy or Pandas. To make this possible there is the function `Syntax.pythonCode()`. The easiest example to show this is with comments.

When compiling, all comments are usually removed. To include comments into the created Python source code they can be written inside of quotes, into the function `Syntax.pythonCode()`. Don't forget to include the Python comment character `#`.


    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		
    		// This comment is removed by the compiler
    		Syntax.pythonCode( "# This comment is inserted in the Python code" );
    		var a = 1;
    	}
    	
    }

Here the result after compiling:
    
    class Main:
    
    	@staticmethod
    	def main():
    		# This comment is inserted in the Python code
    		a = 1

    Main.main()
    
With more complex examples however, errors in Python could be created, for example by optimizations of the Haxe compiler. Because of this it's best to use this function only when absolutely necessary.

<h3>Examples that create errors</h3>

<h4>1. Class variables</h4>

For class variables, in Python the name of the class is added to the variable name.

	package;    
	import python.Syntax;
    
    class Main {
    	static var a:String;
    	
    	static function main() {
    		a = "Hello!";
    		Syntax.pythonCode( "print(a)" );
    	}
    }

The variable name `a` becomes `Main.a`. But inside `Syntax.pythonCode()` the variable is still accessed as `a`.

    class Main:
    	a = None
    
    	@staticmethod
    	def main():
    		Main.a = "Hello!"
    		print(a)
    
    Main.main()

The Python interpreter reports an error

    NameError: name 'a' is not defined



<h4>2. Array compiler optimization</h4>

Here an example for an optimization of the Haxe compiler:

    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		var a = [ 1, 2, 3 ];
    		Syntax.pythonCode( "print( a[2] )" );
    	}
    	
    }
    
The Array `a` is optimized away, because its values are is never accessed as array values. The compiler adds a simple underscore with numbering to the variable name. 

    class Main:
    
    	@staticmethod
    	def main():
    		a_0 = 1
    		a_1 = 2
    		a_2 = 3
    		print( a[2] )
    
    Main.main()
    
The Python interpreter again reports the error

    NameError: name 'a' is not defined

With some basic knowledge in Python however, it is not too hard to find such errors and correct them.

<h4>Calling of Syntax.pythonCode() with variables (the wrong way)</h4>

`Syntax.pythonCode()` cannot be called with a variable as an argument. The text to be included has to be written directly inside of the function and inside of quotes. Something like this doesn't work: 

    package;
    import python.Syntax;
    
    class Main {
    	
    	static function main() {
    		var test = "This doesn't work.";
    		Syntax.pythonCode( test );
    	}
    }

The Python source code:

    class Main:
    
    	@staticmethod
    	def main():
    		test = "This doesn't work"
    		python_Syntax._pythonCode(test,[])
    
    Main.main()
    
The compiler includes a class `python_Syntax._pythonCode`. It doesn't exist in Python and creates an error.

<h4>Calling of Syntax.pythonCode() with variables (the right way)</h4>

After I wrote this article I learned there is a way to use code interpolation in `Syntax.pythonCode()`.

    class Main {
    	
    	static var a:Int;
    	static var b:Int;
    	
    	static function main() {
    		
    		a = 10;
    		b = 5;
    		python.Syntax.pythonCode("print('The value of a is ' + {0} + ' and the value of b is ' + {1})", Std.string(a), String(b));
    	}
    }
    

The generated Python main class looks like this. The complete code can be viewed here: [SyntaxPythonCodeStringInterpolation.py](https://github.com/ustutz/HaxePython_tutorial/blob/master/code/5_1_SyntaxPythonCode_StringInterpolation/bin/SyntaxPythonCodeStringInterpolation.py)


	...
    class Main:
	    _hx_class_name = "Main"
	    __slots__ = ()
	    _hx_statics = ["a", "b", "main"]
	    a = None
	    b = None
	
	    @staticmethod
	    def main():
	        Main.a = 10
	        Main.b = 5
	        python_Syntax._pythonCode((((("print( 'The value of a is " + Std.string(Main.a)) + " and the value of b is ") + Std.string(Main.b)) + "' )"),[])
	
	
	


Both `untyped` and `Syntax.pythonCode()` can be used to call external Python classes. But there is a more elegant way for that.

**Next part: writing externs (coming soon)**