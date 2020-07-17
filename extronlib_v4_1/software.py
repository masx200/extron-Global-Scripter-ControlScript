# pylint: disable=W0613, C0111, C0103, C0301
"""
The software package.

version: 4.1
ExtronLibraray version: 3.1r5
ControlScript version: 3.1.8
GlobalScripter version: 2.1.0.116
Release date: 13.11.2018

Author: Roni Starc (roni.starc@gmail.com)

ChangeLog:
v2.0 - Fixed some mistakes, updated GS v2.8.r3, added description texts for the entire library
v3.0 - Updated to ControlScript 2.9.25 with FW 3.00.0000-b022
v4.0 :
 - updated/fixed layout of ExtronLibrary, ControlScript and GlobalScripter versions
 - Updated to ExtronLibrary 3.1r5 with FW 3.01.0000-b010
 - small fixes (cosmetic)
v4.1 - Fix in other file, increased version number to preserve consistency

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

class CodecConnect():
    """ This class provides an interface to Extron’s Codec Connect software.

    :Note:: System limits 15 CodecConnect clients per system.

    **Arguments**:
    * **Hostname** (*string*) - Hostname of the host computer. Can be IP Address.
    * **IPPort** (*int*) - IP Port the software is listening on (default is *5000*)
    
    :Note:: Only one object can be instantiated for a given Hostname or IP Address.

    **Parameters**:
    Hostname:- **Returns** (*string*) - Hostname of the host computer
    >**Note**: If unavailable, returns the IP Address.
    IPAddress:- **Returns** (*string*) - IP Address of the host computer
    IPPort:- **Returns** (*int*) - IP Port the software is listening on (default is *5000*)
    ListeningPort:- **Returns** (*int*) - IP Port this CodecConnect instance is listening on for received data

    **Events**:
    Connected: :*Event*:: Triggers when communication is established. The callback takes two arguments. The first one is the *CodecConnect* instance triggering the event and the second one is a string ('*Connected*').
    Disconnected: :*Event*:: Triggers when the communication is broken. The callback takes two arguments. The first one is the *CodecConnect* instance triggering the event and the second one is a string ('*Disconnected*').
    ReceiveData: :*Event*:: Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the *CodecConnect* instance triggering the event and the second one is a bytes string.
    """
    Hostname = None
    IPAddress = None
    IPPort = 0
    ListeningPort = None

    def __init__(self, Hostname, IPPort=None):
        """ CodecConnect class constructor.

        **Arguments**:
        * **Hostname** (*string*) - Hostname of the host computer. Can be IP Address.
        * **IPPort** (*int*) - IP Port the software is listening on (default is *5000*)
        """
        self.Hostname = Hostname
        self.IPPort = IPPort

    def Connect(self, timeout=None):
        """ Connect to the software.

        **Arguments**:
        * **timeout** (*float*) - time in seconds to attempt connection before giving up.
        
        **Returns** 
        * '*Connected*' or reason for failure ('*TimedOut*', '*HostError*', '*PortUnavailable:<port>*, ...'). (*string*)
        """
        return ''

    def Disconnect(self):
        """ Disconnect the socket
        """
        pass

    def Send(self, data):
        """ Send string to licensed software

        **Arguments**:
        * **data** (*bytes, string*) - string to send out
        """
        pass

    @classmethod
    def SetListeningPorts(cls, portList=None):
        """ Set the ports to listen for received data.

        **Arguments**:
        * (*optional*) **portList** (*list of ints*) - list of ports (e.g. [10000, 10001, 10002]). *None* will set to default range.

        **Returns**:
        * '*Listening*' or a reason for failure (e.g. '*PortUnavailable:<port>, ...*')

        """
        return ''
