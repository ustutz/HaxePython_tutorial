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

	@staticmethod
	def string(s):
		return python_Boot.toString1(s,"")

	@staticmethod
	def parseInt(x):
		if (x is None):
			return None
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			try:
				prefix = None
				_this = HxString.substr(x,0,2)
				prefix = _this.lower()
				if (prefix == "0x"):
					return int(x,16)
				raise _HxException("fail")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				r = None
				x1 = Std.parseFloat(x)
				try:
					r = int(x1)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					r = None
				if (r is None):
					r1 = Std.shortenPossibleNumber(x)
					if (r1 != x):
						return Std.parseInt(r1)
					else:
						return None
				return r

	@staticmethod
	def shortenPossibleNumber(x):
		r = ""
		_g1 = 0
		_g = len(x)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			c = None
			if ((i < 0) or ((i >= len(x)))):
				c = ""
			else:
				c = x[i]
			_g2 = HxString.charCodeAt(c,0)
			if (_g2 is not None):
				if (((((((((((_g2 == 46) or ((_g2 == 57))) or ((_g2 == 56))) or ((_g2 == 55))) or ((_g2 == 54))) or ((_g2 == 53))) or ((_g2 == 52))) or ((_g2 == 51))) or ((_g2 == 50))) or ((_g2 == 49))) or ((_g2 == 48))):
					r = (("null" if r is None else r) + ("null" if c is None else c))
				else:
					break
			else:
				break
		return r

	@staticmethod
	def parseFloat(x):
		try:
			return float(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			if (x is not None):
				r1 = Std.shortenPossibleNumber(x)
				if (r1 != x):
					return Std.parseFloat(r1)
			return Math.NaN


class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "toString1", "fields", "simpleField", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def toString1(o,s):
		if (o is None):
			return "null"
		if isinstance(o,str):
			return o
		if (s is None):
			s = ""
		if (len(s) >= 5):
			return "<...>"
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		if isinstance(o,int):
			return str(o)
		if isinstance(o,float):
			try:
				if (o == int(o)):
					def _hx_local_1():
						def _hx_local_0():
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return str(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return str(o)
		if isinstance(o,list):
			o1 = o
			l = len(o1)
			st = "["
			s = (("null" if s is None else s) + "\t")
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				prefix = ""
				if (i > 0):
					prefix = ","
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			st = (("null" if st is None else st) + "]")
			return st
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		if hasattr(o,"__class__"):
			if isinstance(o,_hx_AnonObject):
				toStr = None
				try:
					fields = python_Boot.fields(o)
					fieldsStr = None
					_g1 = []
					_g11 = 0
					while (_g11 < len(fields)):
						f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
						_g11 = (_g11 + 1)
						x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
						_g1.append(x)
					fieldsStr = _g1
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					return "{ ... }"
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			if isinstance(o,Enum):
				o2 = o
				l1 = len(o2.params)
				hasParams = (l1 > 0)
				if hasParams:
					paramsStr = ""
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						prefix1 = ""
						if (i1 > 0):
							prefix1 = ","
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					fields1 = python_Boot.getInstanceFields(o)
					fieldsStr1 = None
					_g3 = []
					_g12 = 0
					while (_g12 < len(fields1)):
						f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
						_g12 = (_g12 + 1)
						x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
						_g3.append(x1)
					fieldsStr1 = _g3
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					return toStr1
				else:
					fields2 = python_Boot.getClassFields(o)
					fieldsStr2 = None
					_g4 = []
					_g13 = 0
					while (_g13 < len(fields2)):
						f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
						_g13 = (_g13 + 1)
						x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
						_g4.append(x2)
					fieldsStr2 = _g4
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					return toStr2
			if (o == str):
				return "#String"
			if (o == list):
				return "#Array"
			if callable(o):
				return "function"
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
			if hasattr(o,"__str__"):
				return o.__str__([])
			if hasattr(o,"__name__"):
				return o.__name__
			return "???"
		else:
			return str(o)

	@staticmethod
	def fields(o):
		a = []
		if (o is not None):
			if hasattr(o,"_hx_fields"):
				fields = o._hx_fields
				return list(fields)
			if isinstance(o,_hx_AnonObject):
				d = o.__dict__
				keys = d.keys()
				handler = python_Boot.unhandleKeywords
				for k in keys:
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				a1 = []
				d1 = o.__dict__
				keys1 = d1.keys()
				for k in keys1:
					a.append(k)
		return a

	@staticmethod
	def simpleField(o,field):
		if (field is None):
			return None
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def getInstanceFields(c):
		f = None
		if hasattr(c,"_hx_fields"):
			f = c._hx_fields
		else:
			f = []
		if hasattr(c,"_hx_methods"):
			a = c._hx_methods
			f = (f + a)
		sc = python_Boot.getSuperClass(c)
		if (sc is None):
			return f
		else:
			scArr = python_Boot.getInstanceFields(sc)
			scMap = set(scArr)
			res = []
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				if (not f1 in scMap):
					scArr.append(f1)
			return scArr

	@staticmethod
	def getSuperClass(c):
		if (c is None):
			return None
		try:
			if hasattr(c,"_hx_super"):
				return c._hx_super
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		return None

	@staticmethod
	def getClassFields(c):
		if hasattr(c,"_hx_statics"):
			x = c._hx_statics
			return list(x)
		else:
			return []

	@staticmethod
	def unhandleKeywords(name):
		if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
			real = HxString.substr(name,python_Boot.prefixLength,None)
			if real in python_Boot.keywords:
				return real
		return name


class _hx_AnonObject:
	_hx_class_name = "_hx_AnonObject"


class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["_get"]

	@staticmethod
	def _get(x,idx):
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None


class _HxException(Exception):
	_hx_class_name = "_HxException"
	_hx_fields = ["val"]
	_hx_methods = []
	_hx_statics = []
	_hx_super = Exception


	def __init__(self,val):
		self.val = None
		message = str(val)
		super().__init__(message)
		self.val = val



class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["eq", "stringOrNull"]

	@staticmethod
	def eq(a,b):
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		if (s is None):
			return "null"
		else:
			return s


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["charCodeAt", "substr"]

	@staticmethod
	def charCodeAt(s,index):
		if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
			return None
		else:
			return ord(s[index])

	@staticmethod
	def substr(s,startIndex,_hx_len = None):
		if (_hx_len is None):
			return s[startIndex:]
		else:
			if (_hx_len == 0):
				return ""
			return s[startIndex:(startIndex + _hx_len)]

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")

Main.main()