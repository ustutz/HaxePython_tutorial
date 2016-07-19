#Haxe-Python Tutorial - untyped

<h3>Telling the compiler: "Shut up. I know what I'm doing."</h3>

![haxe to python](https://i.imgsafe.org/63afc9b8fb.png)

[**Overview**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-intro)

[**Previous part: Basics**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-basics)

The last examples showed, how a function, that is not available as such, will be added to the generated Python sourcecode. 

In Python there are functions to convert variable types, too. To convert a variable to the String type there is the function `str()`. To convert a variable to an Integer there is the function `int()`. How can we use these native function directly?

<h3>3. Converting variable types with Python functions</h3>

One idea could be to just write the Python function into the Haxe sourcecode like so:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = str( eight );
    		var int_ten = int( ten );
    	}
    }

If you try this the Haxe compiler gives you two error messages:

    src/Main.hx:10: characters 18-21 : Unknown identifier : str  
    src/Main.hx:11: characters 16-19 : Unknown identifier : int
    
That's because the functions `str()` and `int()` are not known to the compiler.

Well, but we know, these two functions will be valid in Python. For a case like this there is the keyword `untyped`, which we include before the function call:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = untyped str( eight );
    		var int_ten = untyped int( ten );
    	}
    }

The compiler is pleased, and the generated Python code looks like this:

    class Main:
    
    	@staticmethod
    	def main():
    		ten = "10"
    		eight = 8
    		str_eight = str(eight)
    		int_ten = int(ten)
    
    Main.main()

Perfect! Just what we wanted. 

When using the `untyped` keyword, keep in mind that the compiler doesn't check the rest of the line for errors. 

It will not be checked  

* if functions or variables are declared
* if types of functions or variables are correct 

Other examples for `untyped` are when functions in your own Extern classes are not defined, or for matrix multiplications with NumPy. More about that in a later part.

The compiler still checks if the code after `untyped` is valid Haxe code. Something like this won't go through, because array access with `:` and `,` is not possible in Haxe.

    var is_value_empty = untyped data[:,4] == "";

For something like this there is another method.

**Next part: Syntax.pythonCode() (coming soon)**
