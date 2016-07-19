#Haxe-Python Tutorial - Basics

<h3>Two simple examples that show the cross compilation from Haxe to Python</h3>

![haxe to python](https://i.imgsafe.org/63afc9b8fb.png)

[**Overview**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-intro)

Let's begin with a very simple example to show the code the Haxe compiler generates.

<h3>1. Variables</h3>

Variables are an essential building block of probably every programming language. They make assigning values possible.

This is the Haxe source code:

    package;
    
    class Main {
    	
    	static function main() {
    		
    		var a = 5;
    		var b = 6.2;
    		var d = true;
    		var greeting = "Hello";
    	}
    }
                
And this is the generated Python source code:

    class Main:
    
    	@staticmethod
    	def main():
    		a = 5
    		b = 6.2
    		d = True
    		greeting = "Hello"
    
    Main.main()
    
Nothing surprising yet. The sourcecode has been translated line for line to Python.

It gets more interesting when functions of Haxe are not available in Python or when some functionality of Python is not available in Haxe.

<h3>2. Convert the type of a variable</h3>

In this example the value of the variable `eight` is being converted to a string and the value of the variable `ten` is being converted to the integer type. 

    package;
    
    class Main {
    
    	static function main() {
    		
    		var ten = "10";
    		var eight = 8;
    		
    		var str_eight = Std.string( eight );
    		var int_ten = Std.parseInt( ten );
    	}
    }
    

The compiled Python code suddenly becomes much larger. This is only a short excerpt. The complete code can be viewed here: [Typeconversion.py](https://github.com/ustutz/HaxePython_tutorial/blob/master/code/2_Type_conversion/bin/Typeconversion.py) 

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

What happened?

The functions `Std.string` and `Std.int` are not available in Python. But the Haxe compiler included the complete functionality into the compiled source code. The Main class is still there. In this excerpt it is right before the end, and it still looks easy to understand.

Unfortunately this Python code becomes much more confusing and harder to read. But don't let that discourage you. Most of the time you don't even have to look at the generated code and with a little bit of practice it becomes easier to distinguish your parts and the added stuff.

Those who know more about Python probably know there are functions in Python to convert variable types, too. How can we just use those?

[**Next part: untyped**](https://steemit.com/programming/@kkaos/haxe-python-tutorial-untyped)
