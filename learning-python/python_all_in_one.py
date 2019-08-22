#encoding:UTF-8  
import this

def __help():
    print("===============================================")
#i want to use this func to guild user to call all the test function
    print("this function means to be used as a guild");
    print("ipython")
    print("run ./python-all-in-one.py")
    print("test_example()")

    print("Another method to hack this file:\n\
    import import python_all_in_one as pai\n\
    pai.test_example(...)\n   \
    \n")
    pass

def test_numbers():
    var1 = 1
    var2 = 10
    print "var1:", var1
    print "var2:", var2
    print(type(var1));

    #delete a varible
    del var1

def test_string():
    a = "Hello"
    b = "Python"

    print "a + b 输出结果：", a + b 
    print "a * 2 输出结果：", a * 2 
    print "a[1] 输出结果：", a[1] 
    print "a[1:4] 输出结果：", a[1:4] 

    if( "H" in a) :
        print "H 在变量 a 中" 
    else :
        print "H 不在变量 a 中" 

    if( "M" not in a) :
        print "M 不在变量 a 中" 
    else :
        print "M 在变量 a 中"

    print r'\n'
    print R'\n'

def test_list():
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7 ]
     
    print "list1[0]:\t", list1[0]
    print "list2[1:5]:\t", list2[1:5]

    list3 = []          ## 空列表
    list3.append('Google')   ## 使用 append() 添加元素
    list3.append('Runoob')
    print "list3:\t", list3

    list1.sort()
    print "After sorting value"
    print "list1:\t", list1
    del list1[2]
    print "After deleting value at index 2 : "
    print "list1:\t", list1




def test_tuple():
    tup1 = ('physics', 'chemistry', 1997, 2000);
    tup2 = (1, 2, 3, 4, 5 );
    tup3 = "a", "b", "c", "d";

    print "tup1[0]: ", tup1[0]
    print "tup2[1:5]: ", tup2[1:5]

    tup4 = tup1+tup2
    print "tup4: ", tup4

    print tup3[2];

    del tup3[2]     #here is an error
    del tup3

def test_dict():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

    print "dict['Name']: ", dict['Name'];
    print "dict['Age']: ", dict['Age'];
    #print "dict['Sex']: ", dict['Sex'];

    print "Another Year, update Age:"
    dict['Age'] += 1
    print "dict['Age']: ", dict['Age'];

    print len(dict)
    dict.clear()
    print len(dict)

    del dict


'''
#3.0
def test_print_3_0():
    a='spam'
    b=99
    c=['eggs', 'fruits', 'meat']

    print a, b, c
    print(a,b,c)
    print(a,b,c,sep=' ')
    print(a,b,c,end='')
    print("Another String!!!")
'''

def test_print_2_6():
    x='a'
    y='b'

    print x,y               #a b
    print("%s %s" %(x,y))   #a b
    
    print(x,y)              #('a', 'b') 
    t=(x,y); print t        #('a', 'b')
    
    print x,y,;print x,y    #a b a b
    print x,y; print x,y    #a b
                            #a b

    sys.stdout.write("Hello World!!!")


def test_print_redirection():
    tmp=sys.stdout
    sys.stdout=open('log.txt', 'a')

    tmp.write('from tmp=sys.stdout')
    print('spam')
    print(1,2,3)

    sys.stdout.close() # cause ipython crash
    #print(open('log.txt').read()) # stdout closed, this argument causes a IOERROR

def test_None_all_and_maybe_multiply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c
    return result

def test_None():
    type(None)
    
    a=12
    b=13
    sum = test_None_all_and_maybe_multiply(a,b)
    print "a=%d b=%d sum=%d" %(a,b,sum)

'''
    value=true-expr if condition false-expr
'''
def test_ternary_expression_max_of_two(a, b):
    max= a if a>b else b

    #equally as
    if a>b:
        max2=a
    else:
        max2=b

    if max!=max2:
        print "That's impossible!!!"
    return max

'''
[ expr for val in collection if condition ]
'''
def test_ternary_expression():
    a=1
    b=10
    max = test_ternary_expression_max_of_two(a,b)
    print "a=%d b=%d max=%d" %(a,b,max)

def test_expression_from_for():
    result = [i for i in range(20) if i%7==0 ]
    print result

def test_currying():
    add_numbers=lambda x, y: x+y

    add_five=lambda z: add_numbers(z,5)
    print add_five(4)

import time
def test_time():
    ticks = time.time()
    print "当前时间戳为:", ticks

    localtime = time.localtime(time.time())
    print "本地时间为 :", localtime

    localtime = time.asctime( time.localtime(time.time()) )
    print "本地时间为 :", localtime

    # 格式化成2016-03-20 11:45:39形式
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar
def test_calendar():
    cal = calendar.month(2016, 1)
    print "以下输出2016年1月份的日历:"
    print cal;

'''
a simple function to show how yield works 
A concept of generator must be kept in mind
'''
def test_yield(n):
    func=lambda x:x*2;
    for i in range(n):  
        yield func(i)  
        print("i=",i) 
    #做一些其它的事情      
    print("do something.")
    print("end.")

def test_yield_main():
    #1. 使用for循环  
    for j in test_yield(5):
        print(j)
    

    #2. to explain how yield, the equal code is as:
    f=lambda x:x*2
    for i in range(5):
        print( f(i) )
        print("i=",i)
    print("do something.")
    print("end.")

    #3. if directly call "yield" function, nothing printed 
    test_yield(5)

    #4. generator
    g=test_yield(5)
    for j in g:
        print j

def test_generator_gensquares(N):
    for i in range(N):
        x = yield i**2
        print "in test_generator_gensquares:", x

def test_generator():
    for i in test_generator_gensquares(5):
        print i,
    
    #g is a generator
    g = test_generator_gensquares(4)
    print "test_generator", g
    print g.next()
    g.send(88) # the x in test_generator_gensquares() will get this 88
    print g.next()
    print g.next()
    #print g.next()
    #print g.next() #here cause a StopIteration


    #generator from a expression 
    expr = (x**2 for x in range(5))
    print type(expr)
    print expr.next()
    
    g = (c*4 for c in 'SPAM')   # generator
    print g, type(g), (iter(g) is g)

    g = [c*4 for c in 'SPAM'] # list
    print g, type(g), (iter(g) is g)
    it=iter(g)
    print it.next(),it.next(),it.next(),it.next()

    g=('SSSS', 'PPPP', 'AAAA', 'MMMM')#tuple
    print g, type(g), (iter(g) is g)
    it=iter(g)
    print it.next(),it.next(),it.next(),it.next()

'''
lambda is a keyword for temporary function
'''
def test_lambda():
    #temperary function array
    Funcs=[lambda x:x**2, lambda x:x*3]

    func0=Funcs[0]
    func1=Funcs[1]

    print func0(2)
    print func1(2)

    #piece 2
    l=list(map(lambda x: x+1, [0,1,2]))
    print(l)

    l = map(pow, [2,3,4],[2,2,2])
    print(l)

    #multy return
    y = lambda x:[x**2, x*3]
    print y(4)
    y = lambda x:(x**2, x*3)
    print y(4)

    #multy parameters
    sum = lambda x,y:x+y
    print(sum(1,2))

'''
a str type should be input as:
"this is a text" or
'this is a text'
'''
def test_input():
    while True:
        reply = input('input:')
        if reply == 'stop': break
        #print(reply.upper())
        print(type(reply))

        reply = raw_input('raw input:')
        if reply == 'stop': break
        print(reply.upper())
        print(type(reply))

def test_varibles():
    return

import os;
def test_file():
    try:
        document = open("testfile.txt", "w+");
        print "文件名: ", document.name;
        document.write("这是我创建的第一个测试文件！\nwelcome!");
        print document.tell();
#输出当前指针位置
        document.seek(os.SEEK_SET);
#设置指针回到文件最初
        context = document.read();
        print context;
    finally:
        document.close();

def test_exception():
    ret = os.access("testfile", os.W_OK)
    print "W_OK - 返回值 %s"% ret

    try:
        fh = open("testfile", "w")
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError:
        print "Error: 没有找到文件或读取文件失败"
    else:
        print "内容写入文件成功"
        fh.close()

'''
    for
    while
    nest

    break
    continue
    pass
'''
def test_loops():
    count = 0
    while (count < 9):
        print 'The count is:', count
        count = count + 1
    print "Good bye!"

    for i in range(10):
        print i

    for i in ['Bob', 'Lucy', 'Jam', 'Alan']:
        #print("Excellent student:"+i)
        if (i=='Jam'):
            print "Find Jam in the list"
            break;

    for i in ['Bob', 'Lucy', 'Jam', 'Alan']:
        if (i=='Lucy'):
            print "Lucy CHEAT, so remove her from the list"
            continue;
        else:
            print("Excellent student:"+i);
            pass;
        print("Congradulation!!")

def test_nest():
    i = 2
    while(i < 10000):
       j = 2
       while(j <= (i/j)):
          if not(i%j): break
          j = j + 1
       if (j > i/j) : print i, "\t是素数"
       #if (j > i/j) : print i,  "\tis prime number"
       i = i + 1
     
    print "Good bye!"


def test_if(choice):
    if choice == 'spam':
        print(1.25)
    elif choice == 'ham':
        print(1.99)
    elif choice == 'eggs':
        print(0.99)
    elif choice == 'bacon':
        print(1.10)
    else:
        print('Bad choice')

def test_switch():
    return

import random
def test_random():
    print random.random()
    print random.choice([1, 2, 3, 4])

import inspect
def func_a(arg_a,arg_b, *args,  **kwargs):
    print(arg_a, arg_b, args, kwargs)
    #print(arg_a, args, kwargs)

# this function run on python3
def test_function():
    # 获取函数签名
    func_signature = inspect.signature(func_a)
    func_args = []
    # 获取函数所有参数
    for k, v in func_signature.parameters.items():
        # 获取函数参数后，需要判断参数类型
        # 当kind为 POSITIONAL_OR_KEYWORD，说明在这个参数之前没有任何类似*args的参数，那这个函数可以通过参数位置或者参数关键字进行调用
        # 这两种参数要另外做判断
        if str(v.kind) in ('POSITIONAL_OR_KEYWORD', 'KEYWORD_ONLY'):
            # 通过v.default可以获取到参数的默认值
            # 如果参数没有默认值，则default的值为：class inspect_empty
            # 所以通过v.default的__name__ 来判断是不是_empty 如果是_empty代表没有默认值
            # 同时，因为类本身是type类的实例，所以使用isinstance判断是不是type类的实例
            if isinstance(v.default, type) and v.default.__name__ == '_empty':
                func_args.append({k: None})
            else:
                func_args.append({k: v.default})
        # 当kind为 VAR_POSITIONAL时，说明参数是类似*args
        elif str(v.kind) == 'VAR_POSITIONAL':
            args_list = []
            func_args.append(args_list)
        # 当kind为 VAR_KEYWORD时，说明参数是类似**kwargs
        elif str(v.kind) == 'VAR_KEYWORD':
            args_dict = {}
            func_args.append(args_dict)

    print(func_args)

from Tkinter import *           # 导入 Tkinter 库
def test_GUI():
    root = Tk()                     # 创建窗口对象的背景色
                                    # 创建两个列表
    li     = ['C','python','php','html','SQL','java']
    movie  = ['CSS','jQuery','Bootstrap']
    listb  = Listbox(root)          #  创建两个列表组件
    listb2 = Listbox(root)
    for item in li:                 # 第一个小部件插入数据
        listb.insert(0,item)

    for item in movie:              # 第二个小部件插入数据
        listb2.insert(0,item)

    listb.pack()                    # 将小部件放置到主窗口中
    listb2.pack()
    root.mainloop()                 # 进入消息循环

class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
      print( "%s 's __init__ called" %self.name)
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def __del__ (self):
      print( "%s 's __del__ called" %self.name)

'''
构造函数 __init__
析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行： 

Python内置类属性
    __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    __doc__ :类的文档字符串
    __name__: 类名
    __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''
def test_class():
#    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
#"创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee();
    emp2.displayEmployee()
    print "Total Employee %d" % Employee.empCount

    print "Employee.__doc__:", Employee.__doc__
    print "Employee.__name__:", Employee.__name__
    print "Employee.__module__:", Employee.__module__
    print "Employee.__bases__:", Employee.__bases__
    print "Employee.__dict__:", Employee.__dict__

'''
__init__ ( self [,args...] ) 构造函数 简单的调用方法: obj = className(args)
__del__( self ) 析构方法, 删除一个对象 简单的调用方法 : del obj
__repr__( self ) 转化为供解释器读取的形式 简单的调用方法 : repr(obj)
__str__( self ) 用于将值转化为适于人阅读的形式 简单的调用方法 : str(obj)
__cmp__ ( self, x ) 对象比较 简单的调用方法 : cmp(obj, x)
'''
class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"
 
   def parentMethod(self):
      print '调用父类方法'
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print "父类属性 :", Parent.parentAttr
 
class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"
 
   def childMethod(self):
      print '调用子类方法'
def test_subclass():
    c = Child()          # 实例化子类
    c.childMethod()      # 调用子类的方法
    c.parentMethod()     # 调用父类方法
    c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
    c.getAttr()          # 再次调用父类的方法 - 获取属性值

'''
运算符重载
'''
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
def test_operatan():
    v1 = Vector(2,10)
    v2 = Vector(5,-2)
    print v1 + v2

'''
类的私有属性
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的私有方法
    __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 
'''


'''
Python 正则表达式
http://www.runoob.com/python/python-reg-expressions.html
'''
import re
def test_re():
    line = "Cats are smarter than dogs"
    matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
    if matchObj:
       print "matchObj.group() : ", matchObj.group()
       print "matchObj.group(1) : ", matchObj.group(1)
       print "matchObj.group(2) : ", matchObj.group(2)
    else:
       print "No match!!"

'''
multi-thread
test_thread():
'''
import thread
import time
# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )
 
def test_thread():
# 创建两个线程
    try:
       thread.start_new_thread( print_time, ("Thread-1", 2, ) )
       thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
       print "Error: unable to start thread"
     
    while 1:
       pass
'''
test_thread_lock():

threadLock = threading.Lock()
threadLock.acquire()
threadLock.release()
'''
import threading
class myThread (threading.Thread):
    lock = []
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        #threadLock.acquire()
        if (len(self.lock) > 0) :
            self.lock[0].acquire()
        else:
            print "no lock at all"
            return
        print_time2(self.name, self.counter, 3)
        # 释放锁
        #threadLock.release()
        if (len(self.lock) > 0) :
            self.lock[0].release()
        else:
            print "no lock at all"
            return
 
def print_time2(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
 
def test_thread_lock():
    threads = []
     
# 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    threadLock = threading.Lock()
    thread1.lock.append(threadLock)
     
# 开启新线程
    thread1.start()
    thread2.start()
     
# 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
     
# 等待所有线程完成
    for t in threads:
        t.join()
    print "Exiting Main Thread"

'''
test_varibles()
成员变量是[]可以看作是CPP中的static成员变量
'''
class A:
    x = []
    y = 0
    def __init__(self):
        pass
    def add(self):
        self.x.append('1')
        self.y+=1
    
    #private 
    __nickname = "Ace"
    def __setnickname(name):
        __nickname=name


def test_class_varible():
    a=A() 
    print a.x,a.y
    print A.x,A.y
    a.add()
    print a.x,a.y
    print A.x,A.y
    b=A() 
    print b.x,b.y
    print A.x,A.y

    print a.__nickname #here is an error
    a.__setnickname('nn')#here is an error
    print a.__nickname #here is an error

def func_plus_one(x):
    return x + 1
def test_assert():
    assert func(3) == 5

class Bad(Exception):
    pass
def doomed():
    raise Bad()

def test_exception():
    try:
        print("### TEST: Basic")
        assert func_plus_one(3) == 5
    except AssertionError:
        print "get AssertionError!!!!"

    #test raise
    try:
        print("### TEST: Raise IndexError")
        raise IndexError
    except IndexError:
        print "get exception that was just raised"

    #test user defined exception
    try:
        print("### TEST: User Exception")
        doomed()
    except Bad :
        print "get Bad(Exception)"

    #test try/finally, remember:
    #"finally" will be always executed no matter any exception caught or not
    print("### TEST: try/except/finally")
    try :
        i=3
        assert func_plus_one(i)==5
    except AssertionError:
        print "get AssertionError!!!"
    finally: 
        print "func_plus_one( %d ) Called" %i

    try:
        i=4
        assert func_plus_one(i)==5
    except AssertionError:
        print "get AssertionError!!!"
    finally: 
        print "func_plus_one( %d ) Called" %i


    #try-except-else
    print("### TEST: try/except/else")
    try :
        i=4
        assert func_plus_one(i) == 5
        doomed()
    except AssertionError:
        print("get AssertionError!!!")
    except Bad:
        print("get Bad(Exception)")
    else:
        print("any exception occurred.")

    #try-except-else-finally
    print("### TEST: try/except/else")
    try :
        i=4
        assert func_plus_one(i) == 5
        doomed()
    except AssertionError:
        print("get AssertionError!!!")
    except Bad:
        print("get Bad(Exception)")
    else:
        print("any exception occurred.")

def test_with_as():
    try:
        with open('data') as fin, open('res','w')as fout:
            for line in fin:
                if 'some key' in line:
                    fout.write(line)
    except IOError:
        print "open or write file failed!!!!"

def test_timer_func(*pargs, **kargs):
    count=0
    while (count<10000):
        count+=1
    return 0

def test_timer(func, *pargs, **kargs) :
    start = time.clock()
    repts=8000
    for i in range(repts):
        ret = func(*pargs, **kargs)
        elapsed=time.clock()-start
    print("elapsed as %d" % elapsed)
    return (elapsed, ret)

def test_star_starstar(*pargs, **kargs):
    print type(pargs)
    print type(kargs)

def test_module():
    # import a class from a module
    from python_all_in_one import A
    from python_all_in_one import A as name1
    
    del name1
    #equally as:
    import python_all_in_one 
    name1=python_all_in_one.A
    del python_all_in_one

    import python_all_in_one as pai
    pai.test_string()
    
def test_common_functions():
#map

    f=lambda x: x*2
    m=map(f, [1,2,3])
    print m
#iter
    g=('SSSS', 'PPPP', 'AAAA', 'MMMM')#tuple
    print g, type(g), (iter(g) is g)
    it=iter(g)
    print it.next(),it.next(),it.next(),it.next()
#zip
    x='abd'
    i=[str(j+1) for j in range(len(x))]
    k='123'

    z=zip(x,i)
    print z

    z=zip(x,k)
    print z
#range, xrange

#exec
#This statement supports dynamic execution of Python code. 
    pi=3.1415
    d=4.8
    exec("x=pi*pow(d/2,2)")
    print"x=pi*pow(d/2,2) = ", x
    
    exec(
    """if x>5:
            print "x>5 : ", x
    """
    )
#open
    f=open("log.txt", w)
    f.write("this is a test string")
    f.close()
    pass

# transform from one type to another
def test_type_casting():
    x=4
    s=str(x)
    l = range(5)
    t = tuple(l)
    print(type(x), type(s), type(l), type(t))
    print x,s,l,t
'''
<type 'tuple'>
<type 'dict'>
'''



'''
@decorator
def test_decorator(arg):
    print arg
'''

import struct
def test_construction():
    name='test.mp3'
    fp=open(name)
    
    head=fp.read(10)
    print head,type(head)

    id3,ver,revision,flag,length  = struct.unpack("!3sBBBI",frame)
    print id3,ver,revision,flag,length

import subprocess,shlex  
def test_shell_cmd():
    cmd = "md5sum filename"  
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)  
    print (p.stdout.read())

import simplejson
def test_dict_str_conversion():
    d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    s = str(d)
    exec("d2="+s)
    print(d2)
    if d==d2:
        print("exec copy dict ok")
    else:
        print("exec copy dict ng")

    # use json to copy
    json_str = simplejson.dumps(d)
    d3 = simplejson.loads(json_str)

    if d==d3:
        print("json copy dict ok")
    else:
        print("json copy dict ng")

def test_list_to_str():
    l = ['physics', 'chemistry', 1997, 2000]
    print(str(l))
    print(''.join(l))



if __name__ == '__main__':
    '''
    test_timer(test_timer_func)
    test_print_redirection()
    test_with_as()
    test_exception()
    test_assert()
    test_thread_lock()
    test_lambda()
    test_yield_main()
    test_if("eggs")
    test_random()
    test_loops()
    test_nest()
    test_input()
    test_numbers()
    test_string()
    test_list()
    test_tuple()
    test_dict()
    test_time()
    test_calendar()
    test_file()
    test_exception()
    test_GUI()
    test_function()
    test_class()
    test_subclass()
    test_operatan()
    test_re()
    test_thread()
    '''

    __help()
    test_module()
