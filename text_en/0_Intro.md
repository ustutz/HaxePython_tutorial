#Haxe-Python Tutorial - Intro

####This tutorial series is for programmers with previous knowledge in the Haxe programming language. It shows the use of the Python compile target.

In one of my current projects I have to analyze a great amount of data. The programming language Python is predestined for this task because there are a lot of excellent libraries to make it easier. So the first thought would be to learn Python to do the data analysis. But it would take a lot of time to get really good at it.

Because I work mainly with the Haxe programming language there is another way. One feature of Haxe is it's many compile targets. The source code of Haxe can be compiled to source code of other programming languages. Currently (July 2016) there are 10 compile targets. Python is one of them.

So I can write the data analysis in the familiar Haxe language. The compiler creates Python source code that runs in the Python interpreter. The use of the Python libraries is supported.

The Python compile target is relatively new, there is not a lot of documentation, and there are some features in Python that can't be transfered 1x1 to Haxe. In these tutorials I'd like to show some ways how to use it.

![haxe to python](http://i.imgsafe.org/600e09ceed.png)

##Requirements

* Basic knowledge of the Haxe programming language and use of the Haxe Toolkit. A good introduction can be found on [Haxe.org](http://haxe.org/documentation/introduction/)
* Basic knowledge of the Python programming language. There is a good introduction on [learnpython.org](http://www.learnpython.org/)

##Tools

* [Haxe Toolkit](http://haxe.org/) Version 3.3 or newer  
* [HaxeDevelop](http://haxedevelop.org/) for Windows or some other [Haxe development environment](http://haxe.org/documentation/introduction/editors-and-ides.html) for Linux oder Mac .
* [Python 3.x](https://www.continuum.io/downloads) e.g. the open source version of [Anaconda](https://www.continuum.io/why-anaconda), because it comes with a lot of important libraries. Install the Python 3.5 version or newer because Haxe cannot compile to Python 2.x code. 

##Ressources

Some ressources that helped me a gread deal:

* [dataquest.io](https://www.dataquest.io/) - excellent online course in data science for Python 
* [github.com/ustutz/Dataquest](https://github.com/ustutz/Dataquest) - my solution to the DataQuest missions in Haxe
* [PyCon HK 2015](https://haxe.io/@andy_li/PyCon%20HK%202015.pdf) - Haxe-Python presentation of Andy Li at the Python conference 2015 in Hong Kong.
* [PyHelpers.hx](https://github.com/andyli/haxe-usage-survey/blob/master/src/PyHelpers.hx) - Haxe Macro, to make function calls with named arguments easier
* [Haxe-usage-survey](https://github.com/andyli/haxe-usage-survey) - Response data and code for the analysis of a survey of Andy Li
* [Extern generator for the Haxe Python target](https://github.com/andyli/pyextern) of Andy Li.

##Github
The texts and sourcecode of these tutorials are also available on Github for error reporting or improvement ideas.

* [Repository](https://github.com/ustutz/HaxePython_tutorial) - to clone, for issues or pull requests
* [Sourcecode](https://github.com/ustutz/HaxePython_tutorial/tree/master/code) - of the examples


##Overview
* **Intro**
* Basics
* untyped
* Syntax.pythonCode
