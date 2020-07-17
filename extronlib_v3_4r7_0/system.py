# pylint: disable=W0613, C0111, C0103, C0301
"""
The system package.

version: 3.4r7.0
ExtronLibraray version: 3.4r7
ControlScript version: 3.4.6
GlobalScripter version: 2.3.1.3
Release date: 3.10.2019

Author: Roni Starc (roni.starc@gmail.com)

ChangeLog:
v2.0 - Fixed some mistakes, updated GS v2.8.r3, added description texts for the entire library
v3.0 - Updated to ControlScript 2.9.25 with FW 3.00.0000-b022
v4.0 :
 - updated/fixed layout of ExtronLibrary, ControlScript and GlobalScripter versions
 - Updated to ExtronLibrary 3.1r5 with FW 3.01.0000-b010
 - small fixes (cosmetic)
v4.1 - Fix in other file, increased version number to preserve consistency
v4.2 (now v3.2r6.0):
 - Updated to ExtronLibrary 3.2r6
 - Changed versioning to match The ExtronLibrary naming for simplicity; 3rd "digit" is reserved for dummy library fixes when there is no change in the ExtronLibrary.
 - v3.2r6.0 is what v4.2 should have been

new versioning:
v3.3r5.0:
 - Updated to ExronLibrary 3.3r5
v3.3r5.1:
 - Fixed errors in Wait class's Change() and System.Timer (errors found by Eric Walters, thank you)
 - Updated to ExtronLibrary 3.4r7, and ControlScript 3.4.6

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

def GetSystemUpTime():
    """ Returns system up time in seconds.

    **Returns** 
    * system up time in seconds (*int*)
    """
    return 0

def GetUnverifiedContext():
    """ Python 3.4.3 changed the default behavior of the stdlib http clients. They will now verify that “the server presents a certificate which is signed by a CA in the platform trust store and whose hostname matches the hostname being requested by default”. This method returns an unverified context for use when a valid certificate is impossible.

    **Returns**
    * unverified context object compatible with stdlib http clients. (*ssl.SSLContext*)

    :Warning:: **This is a potential security risk. It should only be used when a secure solution is impossible.**
    """
    return None

def Ping(hostname='localhost', count=5):
    """ Ping a host and return the result in a tuple: (# of success ping, # of failure ping , avg time)
    
    **Arguments**:
    * (*optional*) **hostname** (*string*) - IP address to ping.
    * (*optional*) **count** (*int*) - how many times to ping.
    
    **Returns** 
    * tuple (# of success, # of fail, avg time ) (*int, int, float*)
    """
    return ()

def ProgramLog(Entry, Severity='error'):
    """ Write entry to program log file.

    **Arguments**:
    * **Entry** (*string*) - the message to enter into the log
    * (*optional*) **Severity** (*string*) - indicates the severity to the log viewer. ('*info*', '*warning*', or '*error*')
    
    **Note**: ProgramLog also generates a trace message.
    """
    pass

def WakeOnLan(macAddress, port=9):
    """ Wake-on-LAN is an computer networking standard that allows a computer to be awakened by a network message. The network message, ‘Magic Packet’, is sent out through UDP broadcast, port 9.
    
    **Arguments**:
    * **macAddress** (*string*) - Target device’s MAC address. The format is six groups of two hex digits, separated by hyphens ('*01-23-45-67-ab-cd*', e.g.).
    * (*optional*) **port** (*int*) - Port on which target device is listening.

    :Note:: Typical ports for WakeOnLan are 0, 7 and 9.
    """  
    pass

class Clock():
    """ The clock is used to create timed events. It will allow the user to schedule programmed actions to occur based on calendar time.
    
    :Note::
    * When DST causes the clock to spring forward one hour, events scheduled within the skipped hour do not fire.
    * When DST causes the clock to fall back an hour, events scheduled within the repeated hour fire twice.

    **Arguments**:
    * **Times** (*list of strings*) - list of times (e.g. '*HH:MM:SS*') of day to call *Function*
    * **Days** (*list of strings*) - list of weekdays to set alarm. If Days is omitted, the alarm is set for every weekday
    * **Function** (*function*) - function to execute when alarm time is up

    **Parameters**:
    Days:- **Returns** (*list of strings*) - list of days to execute
    > :Note:: list will be empty if it was not provided to the constructor (i.e. the Clock is set for every day).
    Function:- **Returns** (*function*) - Code to execute at given Times.
    > :Note:: Function must accept two parameters: the Clock object and datetime object.
    State:- **Returns** (*string*) - State of the clock device. ('*Enabled*', '*Disabled*')
    Times:- **Returns** (*list of strings*) - list of times to execute.
    WEEKDAYS:- (*dict*) - days of the week dictionary {'*Monday*' ::: 0, '*Tuesday*'::: 1, *'Wednesday*'::: 2, '*Thursday*'::: 3, '*Friday*'::: 4, '*Saturday*'::: 5, '*Sunday*'::: 6}
    """
    Times = []
    Days = []
    Function = None
    State = ''
    WEEKDAYS = {'Monday': 0,
                'Tuesday': 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6}

    def __init__(self, Times, Days=None, Function=None):
        """ Clock class constructor.

        **Arguments**:
        * **Times** (*list of strings*) - list of times (e.g. '*HH:MM:SS*') of day to call *Function*
        * **Days** (*list of strings*) - list of weekdays to set alarm. If Days is omitted, the alarm is set for every weekday
        * **Function** (*function*) - function to execute when alarm time is up
        """
        self.Times = Times
        self.Days = Days
        self.Function = Function

    def Disable(self):
        """ Disable alarm
        """
        pass

    def Enable(self):
        """ Enable alarm
        """
        pass

    def SetDays(self, Days):
        """ Send string to licensed software

        **Arguments**:
        * **Days** (*list of strings*) - a list of Calendar days, as listed in *WEEKDAYS*
        """
        pass

    def SetTimes(self, Times):
        """ Set new alarm times

        **Arguments**:
        * **Times** (*list of strings*) - list of times (e.g. '*HH:MM:SS*') of day to call Function
        """
        pass


class Email():
    """ Class to send email using the configured mail settings. The confiured settings can be over ridden during instantiation.
    
    :Note:: default sender will be login *username@unit-name* or *hostname@unit-name* if there is no authentication. To override, call *Sender()*
    
    **Arguments**:
    * **smtpServer** (*string*) - ip address or hostname of SMTP server
    * **port** (*int*) - port number
    * **username** (*string*) - login username for SMTP authentication
    * **password** (*string*) - login password for SMTP authentication
    * **sslEnabled** (*bool*) - Enable (True) or Disable (False) SSL for the connection
    """
    smtpServer = ''
    port = 0
    username = ''
    password = ''
    sslEnabled = False

    def __init__(self, smtpServer=None, port=None, username=None, password=None, sslEnabled=None):
        """ Email class constructor.

        **Arguments**:
        * **smtpServer** (*string*) - ip address or hostname of SMTP server
        * **port** (*int*) - port number
        * **username** (*string*) - login username for SMTP authentication
        * **password** (*string*) - login password for SMTP authentication
        * **sslEnabled** (*bool*) - Enable (True) or Disable (False) SSL for the connection
        """
        
        self.smtpServer = smtpServer
        self.port = port
        self.username = username
        self.password = password
        self.sslEnabled = sslEnabled

    def Receiver(self, receiver=None, cc=False):
        """ Set receiver’s email address(es) by passing in a list of strings. For example, ['abc@extron.com‘,’xyz@extron.com‘] It will appear in the **<To::: receiver>** field of the email. If cc is set to True, it will appear in the **<CC::: receiver>** field of the email.
        
        **Arguments**:
        * **receiver** (*list of strings*) - receiver’s email address(es)
        * (*optional*) **cc** (*bool*) - Set *True* to put the receiver address(es) in the cc list
        
        :Note:: *Receiver()* must be called each time the list changes.
        
        """
        pass

    def SendMessage(self, msg):
        """ Create main body of the email and send out. Message string will be sent out as plain text.
        
        **Arguments**:
        * **msg** (*string*) - message to send
        """
        pass

    def Sender(self, sender):
        """ Set sender’s email address. It will appear in the <From: sender> field of the email.
        
        **Arguments**:
        * **sender** (*string*) - sender email address

        :Note:: Overrides default sender.
        """
        pass

    def Subject(self, subject):
        """ Set email’s subject. It will appear in the **<Subject::: >** field of the email.

        **Arguments**:
        * **subject** (*string*) - subject of the email
        """
        pass

class File():
    """ Access to files located in user area. These files are stored in a location that can be accessed using 3rd party SFTP clients.
    
    :Note:: File class accesses user area with ‘admin’ privileges.

    **Arguments**:
    * **Filename** (*string*) - Name of file to open
    * **mode** (*string*) - the mode in which the files is opened.
    * **encoding** (*string*) - the name of the encoding used to decode/encode the file.
    * **newline** (*string*) - controls how universal newlines mode works

    :Note:: 
    * *mode*, *encoding*, and *newline* have the same meanings as those passed to the built-in function *open()*. See the documentation at python.org.
    * *ChangeDir()*, *DeleteDir()*, *DeleteFile()*, *Exists()*, *GetCurrentDir()*, *ListDir()*, *MakeDir()*, and *RenameFile()* are all **classmethods**.
    
    :Note:: For restricted file access, substitute File with RFile in the examples above and below.

    **Parameters**:
    Filename:- **Returns** (*string*) - name of file
    """
    Filename = ''
    mode = ''
    encoding = ''
    newline = ''

    def __init__(self, Filename, mode='r', encoding=None, newline=None):
        """ File class constructor.

        **Arguments**:
        * **Filename** (*string*) - Name of file to open
        * **mode** (*string*) - the mode in which the files is opened.
        * **encoding** (*string*) - the name of the encoding used to decode/encode the file.
        * **newline** (*string*) - controls how universal newlines mode works
        """
        self.Filename = Filename
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

    def ChangeDir(self, path):
        """ Change the current working directory to path
        
        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def DeleteDir(self, path):
        """ Remove a directory

        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def DeleteFile(self, filename):
        """ Delete a file

        **Arguments**:
        * **filename** (*string*) - the name of the file to be deleted (path to file)
        """
        pass

    def Exists(self, path):
        """ Return True if path exists

        **Arguments**:
        * **path** (*string*) - path to directory

        **Returns** 
        * true if exists else false (*bool*)
        """
        return True

    def GetCurrentDir(self):
        """ Get the current path.

        **Returns** 
        * the current working directory (*string*)
        """
        return ''

    def ListDir(self, path=None):
        """ List directory contents

        **Arguments**:
        * **path** (*string*) - if provided, path to directory to list, else list current directory

        **Returns** 
        * directory listing (*string*)
        """
        return ''

    def MakeDir(self, path):
        """ Make a new directory

        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def RenameFile(self, oldname, newname):
        """ Rename a file from oldname to newname

        **Arguments**:
        * **oldname** (*string*) - the original filename
        * **newname** (*string*) - the filename to rename to
        """
        pass

    def close(self):
        """ Close an already opened file
        """
        pass

    def read(self, size=-1):
        """ Read data from opened file

        **Arguments**:
        * **size** (*int*) - max number of char/bytes to read

        **Returns** 
        * data (*bytes*)
        """
        return None

    def readline(self):
        """ Read from opened file until newline or EOF occurs

        **Returns** 
        * data (*bytes*)
        """
        return None

    def seek(self, offset, whence=0):
        """ Change the stream position

        **Arguments**:
        * **offset** (*int*) - offset from the start of the file
        * (*optional*) **whence** (*int*) - 
        > * 0 = absolute file positioning
        > * 1 = seek relative to the current position
        > * 2 = seek relative to the file’s end.

        :Note:: Files opened in text mode (i.e. not using '*b*'), only seeks relative to the beginning of the file are allowed – the exception being a seek to the very file end with seek(0,2).
        """
        pass

    def tell(self):
        """ Returns the current cursor position

        **Returns** 
        * the current cursor position (*int*)
        """
        return 0

    def write(self, data):
        """ Write string or bytes to file

        **Arguments**:
        * **data** (*string, bytes*) - data to be written to file
        """
        pass

    def writelines(self, seq):
        """ Write iterable object such as a list of strings

        **Arguments**:
        * **seq** (*e.g. list of strings*) - iterable sequence

        **Raises**:
        * FileNotOpenError
        """
        pass

class RFile():
    """ Access to restricted files. These files can only be created and accessed within the program. Files can be uploaded to provide initial values via the Global Scripter® project.
    
    **Arguments**:
    * **Filename** (*string*) - Name of file to open
    * **mode** (*string*) - the mode in which the files is opened.
    * **encoding** (*string*) - the name of the encoding used to decode/encode the file.
    * **newline** (*string*) - controls how universal newlines mode works

    :Note:: 
    * *mode*, *encoding*, and *newline* have the same meanings as those passed to the built-in function *open()*. See the documentation at python.org.
    * *ChangeDir()*, *DeleteDir()*, *DeleteFile()*, *Exists()*, *GetCurrentDir()*, *ListDir()*, *MakeDir()*, and *RenameFile()* are all **classmethods**.
    
    :Note:: For restricted file access, substitute File with RFile in the examples above and below.

    **Parameters**:
    Filename:- **Returns** (*string*) - name of file    
    """
    Filename = ''
    mode = ''
    encoding = ''
    newline = ''

    def __init__(self, Filename, mode='r', encoding=None, newline=None):
        """ RFile class constructor.

        **Arguments**:
        * **Filename** (*string*) - Name of file to open
        * **mode** (*string*) - the mode in which the files is opened.
        * **encoding** (*string*) - the name of the encoding used to decode/encode the file.
        * **newline** (*string*) - controls how universal newlines mode works
        """
        self.Filename = Filename
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

    def ChangeDir(self, path):
        """ Change the current working directory to path

        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def DeleteDir(self, path):
        """ Remove a directory

        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def DeleteFile(self, filename):
        """ Delete a file

        **Arguments**:
        * **filename** (*string*) - the name of the file to be deleted (path to file)
        """
        pass

    def Exists(self, path):
        """ Return True if path exists

        **Arguments**:
        * **path** (*string*) - path to directory

        **Returns** 
        * true if exists else false (*bool*)
        """
        return True

    def GetCurrentDir(self):
        """ Get the current path.

        **Returns** 
        * the current working directory (*string*)
        """
        return ''

    def ListDir(self, path=None):
        """ List directory contents

        **Arguments**:
        * **path** (*string*) - if provided, path to directory to list, else list current directory

        **Returns** 
        * directory listing (*string*)
        """
        return ''

    def MakeDir(self, path):
        """ Make a new directory

        **Arguments**:
        * **path** (*string*) - path to directory
        """
        pass

    def RenameFile(self, oldname, newname):
        """ Rename a file from oldname to newname

        **Arguments**:
        * **oldname** (*string*) - the original filename
        * **newname** (*string*) - the filename to rename to
        """
        pass

    def close(self):
        """ Close an already opened file
        """
        pass

    def read(self, size=-1):
        """ Read data from opened file

        **Arguments**:
        * **size** (*int*) - max number of char/bytes to read

        **Returns** 
        * data (*bytes*)
        """
        return None

    def readline(self):
        """ Read from opened file until newline or EOF occurs

        **Returns** 
        * data (*bytes*)
        """
        return None

    def seek(self, offset, whence=0):
        """ Change the stream position

        **Arguments**:
        * **offset** (*int*) - offset from the start of the file
        * (*optional*) **whence** (*int*) - 
        > * 0 = absolute file positioning
        > * 1 = seek relative to the current position
        > * 2 = seek relative to the file’s end.

        :Note:: Files opened in text mode (i.e. not using '*b*'), only seeks relative to the beginning of the file are allowed – the exception being a seek to the very file end with seek(0,2).
        """
        pass

    def tell(self):
        """ Returns the current cursor position

        **Returns** 
        * the current cursor position (*int*)
        """
        return 0

    def write(self, data):
        """ Write string or bytes to file

        **Arguments**:
        * **data** (*string, bytes*) - data to be written to file
        """
        pass

    def writelines(self, seq):
        """ Write iterable object such as a list of strings

        **Arguments**:
        * **seq** (*e.g. list of strings*) - iterable sequence

        **Raises**:
        * FileNotOpenError
        """
        pass

class MESet():
    """ The Mutually Exclusive set allows for the grouping of objects to allow easy selection of related items. For instance, a group of buttons could be grouped so that selecting one button deselects the others in the group.
    
    Compatible extronlib classes:
    > * IOInterface (and any children):
    >> * *extronlib.interface.RelayInterface*
    >> * *extronlib.interface.FlexIOInterface* (Output only)
    >> * *extronlib.interface.DigitalIOInterface* (Output only)
    >> * *extronlib.interface.SWPowerInterface*
    > * Button:

    **Arguments**:
    * **Objects** (*list*) - list of compatible objects

    :Note::
    * Each object must have a method *SetState*.
    * *SetState* must take an integer argument.
    * Any object with a *SetState* function that takes an integer object is compatible with this class.
    * A programmer can create their own class and use it with MESet.

    **Parameters**:
    Objects:- **Returns** (*list*) - the list of objects to track
    """
    Objects = []

    def __init__(self, Objects):
        """ MESet class constructor.

       **Arguments**:
        * **Objects** (*list*) - list of compatible objects
        """
        self.Objects = Objects

    def Append(self, obj):
        """ Add an object to the list

        **Arguments**:
        * **obj** (*any*) - any compatible object to add
        """
        pass

    def GetCurrent(self):
        """ Gets the currently selected object in the group.

        **Returns** 
        * the currently selected object in the group.
        """
        pass
    
    def Remove(self, obj):
        """ Remove an object from the list

        **Arguments**:
        * **obj** (*int or compatible object*) - the object or the index of the object
        """
        pass

    def SetCurrent(self, obj):
        """ Selects the current object in the group

        **Arguments**:
        * **obj** (*int or compatible object*) - the object or the index of the object
        
        :Note:: When *None* is passed in, all objects will be deselected.
        """
        pass

    def SetStates(self, obj, offState, onState):
        """ Selects the off and on states for the object (i.e. use states other than the default 0 and 1, respectively).
        
        **Arguments**:
        * **obj** (*int or object*) - the object or the index of the object
        * **offState** (*int*) - the ID of the deselected state
        * **onState** (*int*) - the ID of the selected state
        """
        pass

class Timer():
    """ The Timer class allows the user to execute programmed actions on a regular time differential schedule.
    
    :Note::
    * The handler (*Function*) must accept exactly two parameters, which are the **Timer** that called it and the *Count*.
    * If the handler (*Function*) has not finished by the time the *Interval* has expired, *Function* will not be called and *Count* will not be incremented (i.e. that interval will be skipped).
    
    In addition to being used as a decorator, Timer can be named and modified.
    
    **Arguments**:
    * **Interval** (*float*) - How often to call the handler in seconds (minimum interval is 0.1s).
    * **Function** (*function*) - Handler function to execute each *Interval*.

    **Parameters**:
    Count:- **Returns** (*int*) - Number of events triggered by this timer.
    Function:- **Returns** (*function*) - Handler function to execute each *Interval*. Function must accept exactly two parameters, which are the *Timer* that called it and the *Count*.
    Interval:- **Returns** (*float*) - How often to call the handler in seconds.
    State:- **Returns** (*string*) - Current state of Timer ('*Running*', '*Paused*', '*Stopped*')

    **Events**:
    StateChanged: :*Event*:: Triggers when the timer state changes. The callback takes two arguments. The first is the *Timer* instance triggering the event and the second is a string ('*Running*', '*Paused*', '*Stopped*').
    """
    
    Interval = 0.0
    Function = None
    Count = 0
    State = ''
    StateChanged = None

    def __init__(self, Interval, Function=None):
        """ Timer class constructor.

        **Arguments**:
        **Arguments**:
        * **Interval** (*float*) - How often to call the handler in seconds (minimum interval is 0.1s).
        * **Function** (*function*) - Handler function to execute each *Interval*.
        """
        
        Interval = 0.0
        Function = None

    def Change(self, Interval):
        """ Set a new *Interval* value for future events in this instance.
        
        **Arguments**:
        * **Interval** (*float*) - How often to call the handler in seconds.
        
        """
        pass

    def Pause(self):
        """ Pause the timer (i.e. stop calling the *Function*).
        
        :Note:: Does not reset the timer or the *Count*.
        """
        pass

    def Resume(self):
        """ Resume the timer after being paused or stopped.
        """
        pass

    def Restart(self):
        """Restarts the timer – resets the Count and executes the Function in Interval seconds."""
        pass
    
    def Stop(self):
        """ Stop the timer.
        
        :Note:: Resets the timer and the *Count*.
        """
        pass


class Wait():
    """ The wait class allows the user to execute programmed actions after a desired delay without blocking other processor activity.
    
    In addition to being used as a one-shot (decorator), Wait can be named and reusable.

    **Arguments**:
    * **Time** (*float*) - Expiration time of the wait in seconds
    * **Function** (*function*) - Code to execute when Time expires

    **Parameters**:
    Function:- **Returns** (*function*) - Code to execute when Time expires.
    Time:- **Returns** (*float*) - Expiration time of the wait in seconds with 10ms precision.
    """
    Time = 0.0
    Function = None

    def __init__(self, Time, Function=None):
        """ File class constructor.

        **Arguments**:
        * **Time** (*float*) - Expiration time of the wait in seconds
        * **Function** (*function*) - Code to execute when Time expires
        """
        self.Time = Time
        self.Function = Function

    def Add(self, Time):
        """ Add time to current timer.
        """
        pass

    def Cancel(self):
        """ Stop wait Function from executing when the timer expires.

        """
        pass

    def Change(self, Time):
        """ Set a new Time value for current and future timers in this instance.
        
        **Arguments**:
        * **Time** (*float*) - Time in seconds
        """
        pass

    def Restart(self):
        """ Restarts the timer – executes the Function in Time seconds. If the a timer is active, cancels that timer before starting the new timer.
        """
        pass
