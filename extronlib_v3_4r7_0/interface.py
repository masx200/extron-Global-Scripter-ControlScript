# pylint: disable=W0613, C0111, C0103, R0913, C0301
"""
The interface package.

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

class CircuitBreakerInterface():
    """ This class provides a common interface to a circuit breaker on an Extron product (*extronlib.device*). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    **Arguments**:
    * **Host** (*object*) - handle to Extron device class that instantiated this interface class
    * **Port ** (*string*) - port name (e.g. '*CBR1*')

    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    State:- **Returns** (*string*) - current state of the circuit breaker ('*Closed*', '*Tripped*')

    **Events**:
    Offline: :*Event*:: Triggers when the device goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when the device comes online. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    StateChanged: :*Event*:: Triggers when the circuit breaker state changes. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event, and the second is a string ('*Closed*' or '*Tripped*').
    """
    Host = None
    Port = ''
    State = ''
    Offline = None
    Online = None
    StateChanged = None

    def __init__(self, Host, Port):
        """
        CircuitBreaker class constructor.

        **Arguments**:
        * **Host** (*object*) - handle to Extron device class that instantiated this interface class
        * **Port ** (*string*) - port name (e.g. '*CBR1*')
        """
        self.Host = Host
        self.Port = Port


class ClientObject():
    """ This class provides a handle to connected clients to an *EthernetServerInterfaceEx*.
    
    :Note:: This class cannot be instantiated by the programmer. It is only created by the *EthernetServerInterfaceEx* object.

    **Parameters**:
    Hostname:- **Returns** (*string*) - Hostname DNS name of the connection. Can be the IP Address
    IPAddress:- **Returns** (*string*) - the IP Address of the connected device
    ServicePort:- **Returns** (*int*) - ServicePort port on which the client will listen for data
    """
    Hostname = ''
    IPAddress = ''
    ServicePort = 0

    def __init__(self):
        """ ClientObject class constructor. """
        
        pass

    def Disconnect(self):
        """ Closes the connection gracefully on client. """
        pass

    def Send(self, data):
        """ Send string to the client.

        **Arguments**:
        * **data** (*bytes, string*) - string to send out

        **Raises**:
        * TypeError
        * IOError
        """
        pass

class ContactInterface():
    """ This class will provide a common interface for controlling and collecting data from Contact Input ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*CII1*')

    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    State:- **Returns** (*string*) - 	current state of IO port ('*On*', '*Off*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes online. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    StateChanged: :*Event*:: Triggers when the input state changes. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*On*' or '*Off*').
    """
    Host = None
    Port = ''
    Offline = None
    Online = None
    Port = ''
    State = ''
    StateChanged = None

    def __init__(self, Host, Port):
        """ ContactInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*CII1*')
        """
        self.Host = Host
        self.Port = Port

class DigitalInputInterface():
    """ This class will provide a common interface for collecting data from Digital Input ports on Extron devices (*extronlib.device*). he user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*DII1*')
    * (*optional*) **Pullup** (*bool*) - pull-up state on the port

    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    Pullup:- **Returns** (*bool*) - indicates if the Input port is being pulled up or not
    State:- **Returns** (*string*) - current state of Input port ('*On*', '*Off*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes online. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    StateChanged: :*Event*:: Triggers when the input state changes. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*On*' or '*Off*').
    """
    Host = None
    Port = ''
    Pullup = False
    State = ''
    Online = None
    Offline = None
    StateChanged = None

    def __init__(self, Host, Port, Pullup=False):
        """ DigitalInputInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*DII1*')
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        """
        self.Host = Host
        self.Port = Port
        self.Pullup = Pullup

    def Initialize(self, Pullup=None):
        """ Initializes Digital Input Port to given values. User may provide any or all of theparameters. None leaves property unmodified.
        
        **Arguments**:
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        """
        pass


class DigitalIOInterface():
    """ This class will provide a common interface for controlling and collecting data from Digital IO ports on Extron devices (*extronlib.device*). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*DIO1*')
    * (*optional*) **Mode** (*string*) - Possible modes are: '*DigitalInput*' (default), and '*DigitalOutput*'
    * (*optional*) **Pullup** (*bool*) - pull-up state on the port

    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Mode:- **Returns** (*string*) - mode of the Digital IO port ('*DigitalInput*', '*DigitalOutput*')
    Port:- **Returns** (*string*) - port name
    Pullup:- **Returns** (*bool*) - indicates if the Input port is being pulled up or not
    State:- **Returns** (*string*) - current state of Input port ('*On*', '*Off*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes online. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    StateChanged: :*Event*:: Triggers when the input state changes. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*On*' or '*Off*').
    """
    Host = None
    Port = ''
    Mode = ''
    Pullup = False
    Offline = None
    Online = None
    State = ''
    StateChanged = None

    def __init__(self, Host, Port, Mode='DigitalInput', Pullup=False):
        """ DigitalIOInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*DIO1*')
        * (*optional*) **Mode** (*string*) - Possible modes are: '*DigitalInput*' (default), and '*DigitalOutput*'
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        """
        self.Host = Host
        self.Port = Port
        self.Mode = Mode
        
        self.Pullup = Pullup

    def Initialize(self, Mode=None, Pullup=None):
        """ Initializes Digital IO Port to given values. User may provide any or all of theparameters. None leaves property unmodified.
        
        **Arguments**:
        * (*optional*) **Mode** (*string*) - Possible modes are: '*DigitalInput*' (default), and '*DigitalOutput*'
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        """
        pass

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        **Arguments**:
        * **duration** (*float*) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state to be set ('On' or 1, 'Off' or 0)

        **Arguments**:
        * **State** (*int, string*) - output state to be set ('*On*' or *1*, '*Off*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass

class EthernetClientInterface():
    """ This class provides an interface to a client ethernet socket. This class allows the user to send data over the ethernet port in a synchronous or asynchronous manner.

    :Note:: In synchronous mode, the user will use SendAndWait to wait for the response. In asynchronous mode, the user will assign a handler function to ReceiveData event handler. Then responses and unsolicited messages will be sent to the users receive data handler.

    **Arguments**:
    * **Hostname** (*string*) - DNS Name of the connection. Can be IP Address
    * **IPPort** (*int*) - IP port number of the connection
    * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*', '*UDP*', or '*SSH*'
    * (*optional*) **ServicePort ** (*int*) - Sets the port on which to listen for response data, UDP only, zero means listen on port OS assigns
    * (*optional*) **Credentials ** (*tuple*) - Username and password for SSH connection.

    **Parameters**:
    Credentials:- **Returns** (*tuple, bool*) - Username and password for SSH connection.

        >**Note**:
        >* returns tuple: ('*username*', '*password*') if provided otherwise *None*.
        >* only applies when protocol '*SSH*' is used.
    Hostname:- **Returns** (*string*) - server Host name
    IPAddress:- **Returns** (*string*) - server IP Address
    IPPort:- **Returns** (*int*) - IP port number of the connection
    Protocol:- **Returns** (*string*) - Value for either ’*TCP*’, ’*UDP*’, '*SSH*' connection.
    ServicePort:- **Returns** (*int*) - the port on which the socket is listening for response data

    **Events**:
    Connected: :*Event*:: Triggers when socket connection is established.
    Disconnected: :*Event*:: Triggers when the socket connection is broken
    ReceiveData: :*Event*:: Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the *EthernetClientInterface* instance triggering the event and the second one is a bytes string.
        >**Note**:
        >* The maximum amount of data per *ReceiveData* event that will be passed into the handler is 1024 bytes. For payloads greater than 1024 bytes, multiple events will be triggered.
        >* When UDP protocol is used, the data will be truncated to 1024 bytes.
        >* When protocol is UDP, the service port is not known until communication is active. ServicePort will return 0 when unknown.
    
    **Note** on credentials:
        >* returns tuple: ('*username*', '*password*') if provided otherwise *None*.
        >* only applies when protocol '*SSH*' is used.
    """
    Hostname = ''
    IPAddress = ''
    IPPort = 0
    Protocol = ''
    ServicePort = 0
    Credentials = None
    Connected = None
    Disconnected = None
    ReceiveData = None

    def __init__(self, Hostname, IPPort, Protocol='TCP', ServicePort=0, Credentials=None):
        """ EthernetClientInterface class constructor.

        **Arguments**:
        * **Hostname** (*string*) - DNS Name of the connection. Can be IP Address
        * **IPPort** (*int*) - IP port number of the connection
        * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*', '*UDP*', or '*SSH*'
        * (*optional*) **ServicePort ** (*int*) - Sets the port on which to listen for response data, UDP only, zero means listen on port OS assigns
        * (*optional*) **Credentials ** (*tuple*) - Username and password for SSH connection.
        """
        self.Hostname = Hostname
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.ServicePort = ServicePort
        self.Credentials = Credentials

    def Connect(self, timeout=None):
        """ Connect to the server

        **Arguments**:
        * (*optional*) **timeout** (*float*) - time in seconds to attempt connection before giving up.
        
        **Returns** 
        * '*Connected*' or '*ConnectedAlready*' or reason for failure (*string*)
        
        :Note:: Does not apply to UDP connections.
        """
        pass

    def Disconnect(self):
        """ Disconnect the socket

        :Note:: Does not apply to UDP connections.
        """
        pass

    def SSLWrap(self, certificate=None, cert_reqs='CERT_NONE', ssl_version='TLSv2', ca_certs=None):
        """ Wrap this connection in an SSL context

        :Note::This is almost a direct call to *ssl.wrap_socket()*. See python documentation for more details. The following changes are applied:
            >* Property **server_side** is set to *False*
            >* Property **cert_reqs** is a string
            >* Property **ssl_version** is a string
            >* Property **do_handshake_on_connect** is set to *True*
            >* Property **suppress_ragged_eofs** is set to *True*
            >* Property **ciphers** is fixed to the system default

        **Arguments**:
        * **certificate** (*string*) - alias to a specific keyfile/certificate pair
        * **cert_reqs** (*string*) - specifies whether a certificate is required from the other side of the connection (*'CERT_NONE'*, *'CERT_OPTIONAL'*, or *'CERT_REQUIRED'*). If the value of this parameter is not *'CERT_NONE'*, then the ca_certs parameter must point to a file of CA certificates.
        * **ssl_version** (*string*) - version from the supported SSL/TLS version table ('*TLSv2*'). Currently only TLS 1.2 is allowed.
        * **ca_certs** (*string*) - alias to a file that contains a set of concatenated “certification authority” certificates, which are used to validate certificates passed from the other end of the connection.
        
        :Note::
            >* Requires protocol *'TCP'*.
            >* **certificate** and **ca_certs** specify aliases to machine certificate/key pairs and CA certificates uploaded to the processor in Toolbelt.
        """
        pass

    def Send(self, data):
        """ Send string over ethernet port if it’s open

        **Arguments**:
        * **data** (*bytes, string*) - string to send out
        
        **Raises**:
        * TypeError
        * IOError
        """
        pass

    def SendAndWait(self, data, timeout, **delimiter):
        """ Send data to the controlled device and wait (blocking) for response. It returns after timeout seconds expires or immediately if the optional condition is satisfied.
        
        :Note:: In addition to data and timeout, the method accepts an optional delimiter, which is used to compare against the received response. It supports any one of the following conditions:
            >* **deliLen** (*int*) - length of the response
            >* **deliTag** (*bytes*) - suffix of the response
            >* **deliRex** (*regular expression object*) - regular expression

        :Note:: The function will return an empty byte array if timeout expires and nothing is received, or the condition (if provided) is not met.
        
        **Arguments**:
        * **data** (*bytes, string*) - data to send.
        * **timeout** (*float*) - amount of time to wait for response.
        * **delimiter** (*see above*) - optional conditions to look for in response.

        **Returns**:
        * Response received data (may be empty) (*bytes*)
        """
        pass

    def StartKeepAlive(self, interval, data):
        """ Repeatedly sends data at the given interval

        **Arguments**:
        * **interval** (*float*) - Time in seconds between transmissions
        * **data** (*bytes, string*) - data bytes to send
        """
        pass

    def StopKeepAlive(self):
        """ Stop the currently running keep alive routine
        """
        pass

class EthernetServerInterface():
    """ This class provides an interface to a server Ethernet socket. After instantiation, the server is started by calling StartListen(). This class allows the user to send data over the Ethernet port in an asynchronous manner using Send() and ReceiveData after a client has connected.

    :Warning:: **This class is no longer supported. For any new development, *EthernetServerInterfaceEx* should be used.**
    
    **Arguments**:
    * **IPPort ** (*int*) - IP port number of the listening service.
    * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*' or '*UDP*'
    * (*optional*) **Interface ** (*string*) - Defines the network interface on which to listen ('*Any*', '*LAN*' of '*AVLAN*')
    * (*optional*) **ServicePort ** (*int*) - sets the port from which the client will send data. Zero means any service port is valid.

    **Note**: *ServicePort* is only applicable to '*UDP*' protocol type.

    **Parameters**:
    Hostname:- **Returns** (*string*) - Hostname DNS name of the connection. Can be the IP Address
    IPAddress:- **Returns** (*string*) - the IP Address of the connected device
    IPPort:- **Returns** (*int*) - IP Port number of the listening service
    Interface:- **Returns** (*string*) - name of interface on which the server is listening
    Protocol:- **Returns** (*string*) - Value for either ’*TCP*’, ’*UDP*’ connection.
    ServicePort:- **Returns** (*int*) - ServicePort port on which the client will listen for data

    **Events**:
    Connected: :*Event*:: Triggers when socket connection is established.
    Disconnected: :*Event*:: Triggers when the socket connection is broken
    ReceiveData: :*Event*:: Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the *EthernetServerInterface* instance triggering the event and the second one is a bytes string.
    """

    IPPort = 0
    Protocol = ''
    Interface = ''
    ServicePort = 0
    Connected = None
    Disconnected = None
    HostName = ''
    IPAddress = ''
    ReceiveData = None

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', ServicePort=0):
        """ EthernetServerInterface class constructor.

        **Arguments**:
        * **IPPort ** (*int*) - IP port number of the listening service.
        * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*' or '*UDP*'
        * (*optional*) **Interface ** (*string*) - Defines the network interface on which to listen ('*Any*', '*LAN*' of '*AVLAN*')
        * (*optional*) **ServicePort ** (*int*) - sets the port from which the client will send data. Zero means any service port is valid.
        """
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.Interface = Interface
        self.ServicePort = ServicePort

    def Disconnect(self):
        """ Closes the connection gracefully.
        """
        pass

    def Send(self, data):
        """ Send string over ethernet port if it’s open

        **Arguments**:
        * **data ** (*int*) - string to send out

        **Raises**:
        * TypeError
        * IOError
        """
        pass

    def StartListen(self, timeout=0):
        """ Start the listener

        **Arguments**:
        * (*optional*) **timeout ** (*float*) - how long to listen for connections (0=Forever)

        **Returns**:
        * '*Listening*' or a reason for failure (e.g. '*PortUnavailable*')

        **Raises**:
        * IOError
        """
        pass

    def StopListen(self):
        """ Stop the listener
        """
        pass

class EthernetServerInterfaceEx():
    """ This class provides an interface to an Ethernet server that allows a user-defined amount of client connections. After instantiation, the server is started by calling *StartListen()*. This class allows the user to send data over the Ethernet port in an asynchronous manner using *Send()* and *ReceiveData* after a client has connected.

    **Arguments**:
    * **IPPort ** (*int*) - IP port number of the listening service.
    * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*' or '*UDP*'
    * (*optional*) **Interface ** (*string*) - Defines the network interface on which to listen ('*Any*', '*LAN*' of '*AVLAN*')
    * (*optional*) **MaxClients ** (*int*) - maximum number of client connections to allow (*None* == Unlimited, 0 == Invalid)

    **Parameters**:
    Clients:- **Returns** (*list of ClientObject*) - List of connected clients.
    IPPort:- **Returns** (*int*) - IP Port number of the listening service
    Interface:- **Returns** (*string*) - name of interface on which the server is listening ('*Any*', '*LAN*' of '*AVLAN*')
    MaxClients:- **Returns** (*int or None*) - maximum number of client connections to allow (*None* == Unlimited, 0 == Invalid)
    Protocol:- **Returns** (*string*) - socket protocol ('*TCP*', '*UDP*')
    
    **Events**:
    Connected: :*Event*:: Triggers when socket connection is established. The callback takes two arguments. The first one is the *ClientObject* instance triggering the event and the second one is a string ('*Connected*').
    Disconnected: :*Event*:: Triggers when the socket connection is broken. The callback takes two arguments. The first one is the *ClientObject* instance triggering the event and the second one is a string ('*Disconnected*').
    ReceiveData: :*Event*:: Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the *ClientObject* instance triggering the event and the second one is a bytes string.
    """

    IPPort = 0
    Protocol = ''
    Interface = ''
    MaxClients = None
    Clients = []
    Connected = None
    Disconnected = None
    ReceiveData = None

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', MaxClients=None):
        """ EthernetServerInterfaceEx class constructor.

        **Arguments**:
        * **IPPort ** (*int*) - IP port number of the listening service.
        * (*optional*) **Protocol ** (*string*) - Value for either '*TCP*' or '*UDP*'
        * (*optional*) **Interface ** (*string*) - Defines the network interface on which to listen
        * (*optional*) **MaxClients ** (*int*) - maximum number of client connections to allow (*None* == Unlimited, 0 == Invalid)
        """
        
        self.IPPort = IPPort
        self.Protocol = Protocol
        self.Interface = Interface
        self.MaxClients = MaxClients

    def Disconnect(self, client):
        """ Closes the connection gracefully on specified client.

        **Arguments**:
        * **client** (*ClientObject*) - handle to client object        
        """
        pass

    def SSLWrap(self, certificate=None, cert_reqs='CERT_NONE', ssl_version='TLSv2', ca_certs=None):
        """ Wrap all connections to this server instance in an SSL context.

        :Note::This is almost a direct call to *ssl.wrap_socket()*. See python documentation for more details. The following changes are applied:
            >* Property **server_side** is set to *False*
            >* Property **cert_reqs** is a string
            >* Property **ssl_version** is a string
            >* Property **do_handshake_on_connect** is set to *True*
            >* Property **suppress_ragged_eofs** is set to *True*
            >* Property **ciphers** is fixed to the system default

        **Arguments**:
        * **certificate** (*string*) - alias to a specific keyfile/certificate pair
        * **cert_reqs** (*string*) - specifies whether a certificate is required from the other side of the connection (*'CERT_NONE'*, *'CERT_OPTIONAL'*, or *'CERT_REQUIRED'*). If the value of this parameter is not *'CERT_NONE'*, then the ca_certs parameter must point to a file of CA certificates.
        * **ssl_version** (*string*) - version from the supported SSL/TLS version table ('*TLSv2*'). Currently only TLS 1.2 is allowed.
        * **ca_certs** (*string*) - alias to a file that contains a set of concatenated “certification authority” certificates, which are used to validate certificates passed from the other end of the connection.
        
        :Note::
            >* Requires protocol *'TCP'*.
            >* **certificate** and **ca_certs** specify aliases to machine certificate/key pairs and CA certificates uploaded to the processor in Toolbelt.
        """
        pass

    def StartListen(self, timeout=0):
        """ Start the listener

        **Arguments**:
        * (*optional*) **timeout ** (*float*) - how long to listen for connections (0=Forever)

        **Returns**:
        * '*Listening*' or a reason for failure (e.g. '*PortUnavailable*')

        **Raises**:
        * IOError

        **Note**: Return examples:
        * *Listening*
        * *ListeningAlready*
        * *PortUnavailable*
        * *InterfaceUnavailable: LAN*
        * *InterfaceUnavailable: LAN, AVLAN*

        **Note**: If '*Listening*' not in result, the server will not be listening.
        """
        pass

    def StopListen(self, client):
        """ Stop the listener
        """
        pass

class FlexIOInterface():
    """ This class will provide a common interface for controlling and collecting data from Flex IO ports on Extron devices (*extronlib.device*). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*FIO1*')
    * (*optional*) **Mode** (*string*) - Possible modes are: '*AnalogInput*', '*DigitalInput*' (default), and '*DigitalOutput*'.
    * (*optional*) **Pullup** (*bool*) - pull-up state on the port
    * (*optional*) **Upper** (*float*) - upper threshold in volts
    * (*optional*) **Lower** (*float*) - lower threshold in volts

    **Parameters**:
    AnalogVoltage:- **Returns** (*float*) - current voltage of analog input port
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Lower:- **Returns** (*float*) - lower threshold for digital input in volts
        >**Note**: Only applicable when Flex IO is in '*DigitalInput*' mode.
    Mode:- **Returns** (*string*) - mode of the Flex IO port ('*AnalogInput*', '*DigitalInput*', '*DigitalOutput*').
    Port:- **Returns** (*string*) - port name
    Pullup:- **Returns** (*bool*) - indicates if the input port is being pulled up or not
    State:- **Returns** (*string*) - current state of IO port ('*On*', '*Off*')
    Upper:- **Returns** (*float*) - upper threshold for digital input in volts
        >**Note**: Only applicable when Flex IO is in '*DigitalInput*' mode.
    
    **Events**:
    AnalogVoltageChanged: :*Event*:: triggers when the input voltage changes. The callback takes two arguments. The first one is the *extronlib.interface.FlexIOInterface* instance triggering the event and the second one is the voltage.
        >**Note**: Minimum voltage change required to trigger event is 0.05V.
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    StateChanged: :*Event*:: Triggers when the input state changes. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*On*' or '*Off*').
        >**Note**: Only triggers for ports in Input mode.
    """

    Host = None
    Port = ''
    Mode = ''
    Pullup = False
    Upper = 0.0
    Lower = 0.0
    AnalogVoltage = 0.0
    AnalogVoltageChanged = None
    Offline = None
    Online = None
    StateChanged = None

    def __init__(self, Host, Port, Mode='DigitalInput', Pullup=False, Upper=2.8, Lower=2.0):
        """ FlexIOInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*FIO1*')
        * (*optional*) **Mode** (*string*) - Possible modes are: '*AnalogInput*', '*DigitalInput*' (default), and '*DigitalOutput*'.
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        * (*optional*) **Upper** (*float*) - upper threshold in volts
        * (*optional*) **Lower** (*float*) - lower threshold in volts
        """
        self.Host = Host
        self.Port = Port
        self.Mode = Mode
        self.Pullup = Pullup
        self.Upper = Upper
        self.Lower = Lower

    def Initialize(self, Mode=None, Pullup=None, Upper=None, Lower=None):
        """ Initializes Flex IO Port to given values. User may provide any or all of the parameters. None leaves property unmodified.
        
        **Arguments**:
        * (*optional*) **Mode** (*string*) - Possible modes are: '*AnalogInput*', '*DigitalInput*' (default), and '*DigitalOutput*'.
        * (*optional*) **Pullup** (*bool*) - pull-up state on the port
        * (*optional*) **Upper** (*float*) - upper threshold in volts
        * (*optional*) **Lower** (*float*) - lower threshold in volts
        """
        pass

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        **Arguments**:
        * **duration** (*float*) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state

        **Arguments**:
        * **State** (*int, string*) - output state to be set ('*On*' or *1*, '*Off*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass

class IRInterface():
    """ This class provides an interface to an IR port. This class allows the user to transmit IR data through an IR or IR/Serial port.

    **Note**: If an IR/Serial port is passed in and it has already been instantiated as an *SerialInterface*, an exception will be raised.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g., '*IRS1*')
    * **File** (*string*) - IR file name (e.g. '*someDevice.eir*')

    **Parameters**:
    File:- **Returns** (*string*) - file name
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    """

    Host = None
    Port = ''
    File = ''
    Offline = None
    Online = None

    def __init__(self, Host, Port, File):
        """ IRInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g., '*IRS1*')
        * **File** (*string*) - IR file name (e.g. '*someDevice.eir*')
        """

        self.Host = Host
        self.Port = Port
        self.File = File

    def Initialize(self, File=None):
        """ Initializes IR Port to given file. None leaves property unmodified.
        
        **Arguments**:
        * (*optional*) **File** (*string*) - IR file name (e.g. '*someDevice.eir*')
        """
        pass

    def PlayContinuous(self, irFunction):
        """ Begin playback of an IR function. Function will play continuously until stopped. Will complete at least one header, one body, and the current body.
        
        **Arguments**:
        * **irFunction** (*string*) - function within the driver to play

        :Note:: PlayContinuous is interruptable by subsequent Play function calls (*PlayCount()*, *PlayTime()*) and *Stop()*.
        """
        pass

    def PlayCount(self, irFunction, repeatCount=None):
        """  Play an IR function Count times. Function will play the header once and the body 1 + the specified number of repeat times.
        
        **Arguments**:
        * **irFunction** (*string*) - function within the driver to play
        * (*optional*) **repeatCount ** (*int*) - number of times to repeat the body (0-15)

        **Note**:
        * *PlayCount* is uninterruptible, except by *Stop()*.
        * *repeatCount* of *None* means play the number defined in the driver.
        """
        pass

    def PlayTime(self, irFunction, duration):
        """ Play an IR function for the specified length of time. Function will play the header once and the body as many times as it can. Playback will stop when the time runs out. Current body will be completed.
        
        **Arguments**:
        * **irFunction** (*string*) - function within the driver to play
        * **duration** (*float*) - time in seconds to play the function

       :Note:: *PlayTime* is uninterruptible, except by *Stop()*.
        """
        pass

    def Stop(self):
        """ Stop the current playback. Will complete the current body.
        """
        pass

class PoEInterface():
    """ This is the interface class for the Power over Ethernet ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g., '*POE1*')

    **Parameters**:
    CurrentLoad:- **Returns** (*float*) - the current load of PoE port in watts
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    PowerStatus:- **Returns** (*string*) - State of power transmission on the port ('*Active*', '*Inactive*'). '*Active*' if there is a device being powered by the port.
    State:- **Returns** (*string*) - current state of IO port ('*On*', '*Off*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*').
    PowerStatusChanged: :*Event*:: Triggers when the state of power transmission on the port changes (e.g. a PoE device is plugged into the port). The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Active*' or '*Inactive*'). 
    """

    Host = None
    Port = ''
    CurrentLoad = 0.0
    Offline = None
    Online = None
    PowerStatus = ''
    PowerStatusChanged = None
    State = ''

    def __init__(self, Host, Port):
        """ PoEInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g., '*POE1*')
        """

        self.Host = Host
        self.Port = Port

    def SetState(self, State):
        """
        **Arguments**:
        * **State** (*int*, *string*) - output state to be set ('*On*' or *1*, '*Off*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state to the logical opposite of the current state.
        """
        pass

class RelayInterface():
    """ This class provides a common interface for controlling relays on Extron devices (*extronlib.device*). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*RLY1*')
    
    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    State:- **Returns** (*string*) - current state of Relay port ('*Close*', '*Open*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    """
    Host = None
    Port = ''
    Offline = None
    Online = None

    def __init__(self, Host, Port):
        """ RelayInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*RLY1*')
        """
        self.Host = Host
        self.Port = Port

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        **Arguments**:
        * **duration** (*float*) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state to be set ('Close' or 1, 'Open' or 0)
        
        **Arguments**:
        * **State** (*int, string*) - output state to be set ('*Close*' or *1*, '*Open*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass

class SerialInterface():
    """ This class provides an interface to a serial port. This class allows the user to send data over the serial port in a synchronous or asynchronous manner. This class is used for all ports capable of serial communication (e.g., Serial Ports, IR Serial Ports).

        >**Note**:
        >* In synchronous mode, the user will use *SendAndWait()* to wait for the response.
        >* In asynchronous mode, the user will assign a handler function to *ReceiveData* to handle responses.
        >* If an IR/Serial port is passed in and it has already been instantiated as an *IRInterface*, an exception will be raised.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g.  '*COM1*', '*IRS1*')
    * (*optional*) **Baud** (*int*) - baudrate
    * (*optional*) **Data** (*int*) - number of data bits
    * (*optional*) **Parity** (*string*) - '*None*', '*Odd*' or '*Even*'
    * (*optional*) **Stop** (*int*) - number of stop bits
    * (*optional*) **FlowControl** (*string*) - '*HW*', '*SW*', or '*Off*'
    * (*optional*) **CharDelay** (*float*) - time between each character sent to the connected device
    * (*optional*) **Mode** (*string*) - mode of the port, '*RS232*', '*RS422*' or '*RS485*'

    **Parameters**:
    Baud:- **Returns** (*int*) - the baud rate
    CharDelay:- **Returns** (*float*) - inter-character delay
    Data:- **Returns** (*int*) - the number of data bits
    FlowControl:- **Returns** (*string*) - flow control
    Host:- **Returns** (*extronlib.device*) - the host device
    Mode:- **Returns** (*string*) - the current Mode
    Parity:- **Returns** (*string*) - parity
    Port:- **Returns** (*string*) - the port name this interface is attached to
    Stop:- **Returns** (*int*) - number of stop bits

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    ReceiveData: :*Event*:: Receive Data event handler used for asynchronous transactions. The callback takes two arguments. The first one is the *SerialInterface* instance triggering the event and the second one is a bytes string.
    """
    Host = None
    Port = ''
    Baud = 0
    Data = 0
    Parity = ''
    Stop = 0
    FlowControl = ''
    CharDelay = 0.0
    Mode = ''
    Offline = None
    Online = None
    ReceiveData = None

    def __init__(self, Host, Port, Baud=9600, Data=8, Parity='None', Stop=1, FlowControl='Off', CharDelay=0, Mode='RS232'):
        """ SerialInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g.  '*COM1*', '*IRS1*')
        * (*optional*) **Baud** (*int*) - baudrate
        * (*optional*) **Data** (*int*) - number of data bits
        * (*optional*) **Parity** (*string*) - '*None*', '*Odd*' or '*Even*'
        * (*optional*) **Stop** (*int*) - number of stop bits
        * (*optional*) **FlowControl** (*string*) - '*HW*', '*SW*', or '*Off*'
        * (*optional*) **CharDelay** (*float*) - time between each character sent to the connected device
        * (*optional*) **Mode** (*string*) - mode of the port, '*RS232*', '*RS422*' or '*RS485*'
        """
        self.Host = Host
        self.Port = Port
        self.Baud = Baud
        self.Data = Data
        self.Parity = Parity
        self.Stop = Stop
        self.FlowControl = FlowControl
        self.CharDelay = CharDelay
        self.Mode = Mode

    def Initialize(self, Baud=None, Data=None, Parity=None, Stop=None, FlowControl=None, CharDelay=None, Mode=None):
        """ Initializes Serial Port to given values. User may provide any or all of the parameters. None leaves property unmodified.
        
        **Arguments**:
        * (*optional*) **Baud** (*int*) - baudrate
        * (*optional*) **Data** (*int*) - number of data bits
        * (*optional*) **Parity** (*string*) - '*None*', '*Odd*' or '*Even*'
        * (*optional*) **Stop** (*int*) - number of stop bits
        * (*optional*) **FlowControl** (*string*) - '*HW*', '*SW*', or '*Off*'
        * (*optional*) **CharDelay** (*float*) - time between each character sent to the connected device
        * (*optional*) **Mode** (*string*) - mode of the port, '*RS232*', '*RS422*' or '*RS485*'
        """
        pass

    def Send(self, data):
        """ Send string over serial port if it’s open

        **Arguments**:
        * **data** (*bytes, string*) - data to send
        
        **Raises**:
        * TypeError
        * IOError
        """
        pass

    def SendAndWait(self, data, timeout, **delimiter):
        """ Send data to the controlled device and wait (blocking) for response

        **Note** In addition to data and timeout, the method accepts an optional delimiter, which is used to compare against the received response. It supports any one of the following conditions:
            >* *deliLen* (*int*) - length of the response
            >* *deliTag* (*byte*) - suffix of the response
            >* *deliRex* (*regular expression object*) - regular expression

        It returns after timeout seconds expires, or returns immediately if the optional condition is satisfied.

        :Note:: The function will return an empty byte array if timeout expires and nothing is received, or the condition (if provided) is not met.

        **Arguments**:
        * **data** (*bytes, string*) - data to send.
        * **timeout** (*float*) - amount of time to wait for response.
        * **delimiter** (*see above*) - optional conditions to look for in response.

        **Returns** 
        * Response received data (may be empty) (*bytes*)
        """
        pass

    def StartKeepAlive(self, interval, data):
        """ Repeatedly sends data at the given interval
        
        **Arguments**:
        * **interval** (*float*) - Time in seconds between transmissions
        * **data** (*bytes*) - data bytes to send
        """
        pass

    def StopKeepAlive(self):
        """ Stop the currently running keep alive routine
        """
        pass

class SWACReceptacleInterface():
    """ This class provides a common interface to a switched AC power receptacle on an Extron product (*extronlib.device*). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*SAC1*')
    
    **Parameters**:
    CurrentChanged:- **Returns** (*float*) - instantaneous current draw in Amperes
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    State:- **Returns** (*string*) - current state of receptacle ('*On*', '*Off*')
    
    **Events**:
    CurrentChanged: :*Event*:: triggers when the current draw changes. The callback takes two arguments. The first one is the *SWACReceptacleInterface* instance triggering the event, and the second is the current.
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    
    """
    Current = 0.0
    Host = None
    Port = ''
    Offline = None
    Online = None
    State = ''
    StateChanged = None

    def __init__(self, Host, Port):
        """ SWACReceptacleInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*SAC1*')
        """
        self.Host = Host
        self.Port = Port
    
    def SetState(self, State):
        """ Sets output state to be set ('On' or 1, 'Off' or 0)

        **Arguments**:
        * **State** (*int, string*) - output state to be set ('*On*' or *1*, '*Off*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state of the receptacle to the logical opposite of the current state.
        """
        pass

class SWPowerInterface():
    """ This is the interface class for the Switched Power ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.

    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*SPI1*')
    
    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    Port:- **Returns** (*string*) - port name
    State:- **Returns** (*string*) - current state of IO port ('*On*', '*Off*')
    
    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    
    """
    Host = None
    Port = ''
    Offline = None
    Online = None
    State = ''

    def __init__(self, Host, Port):
        """ SWPowerInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*SPI1*')
        """
        self.Host = Host
        self.Port = Port

    def Pulse(self, duration):
        """ Turns the port on for the specified time in seconds with 10ms accuracy and a 100ms minimum value.
        
        **Arguments**:
        * **duration** (*float*) - pulse duration
        """
        pass

    def SetState(self, State):
        """ Sets output state to be set ('On' or 1, 'Off' or 0)

        **Arguments**:
        * **State** (*int, string*) - output state to be set ('*On*' or *1*, '*Off*' or *0*)
        """
        pass

    def Toggle(self):
        """ Changes the state of the IO Object to the logical opposite of the current state.
        """
        pass

class VolumeInterface():
    """ This class will provide a common interface for controlling and collecting data from Volume Ports on Extron devices (extronlib.device). The user can instantiate the class directly or create a subclass to add, remove, or alter behavior for different types of devices.
    
    **Arguments**:
    * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
    * **Port** (*string*) - port name (e.g. '*VOL1*')

    **Parameters**:
    Host:- **Returns** (*extronlib.device*) - 	the host device
    Level:- **Returns** (*int*) - Current volume level (percentage).
    Max:- **Returns** (*float*) - Maximum level (0.0 V < Max <= 10.0 V).
    Min:- **Returns** (*float*) - Minimum level (0.0 V <= Min < 10.0 V).
    Mute:- **Returns** (*string*) - Current state of volume port mute. ('*On*', '*Off*')
    Port:- **Returns** (*string*) - the port name this interface is attached to
    SoftStart:- **Returns** (*string*) - Current state of Soft Start. ('*Enabled*', '*Disabled*')

    **Events**:
    Offline: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when port goes offline. The callback takes two arguments. The first one is the *extronlib.interface* instance triggering the event and the second one is a string ('*Online*'). 
    
    """
    Host = None
    Port = ''
    Level = 0
    Max = 0.0
    Min = 0.0
    Mute = ''
    SoftStart = ''
    Offline = None
    Online = None
    

    def __init__(self, Host, Port):
        """ VolumeInterface class constructor.

        **Arguments**:
        * **Host** (*extronlib.device*) - handle to Extron device class that instantiated this interface class
        * **Port** (*string*) - port name (e.g. '*VOL1*')
        """
        self.Host = Host
        self.Port = Port
        self.Level = 0
        self.Max = 0.0
        self.Min = 0.0
        self.SoftStart = ''

    def SetLevel(self, Level):
        """ Sets Level of volume control port
        
        **Arguments**:
        * **Level** (*int*) - Level (0 % <= Value <= 100 %).
        """
        pass

    def SetMute(self, Mute):
        """ Sets the mute state.

        **Arguments**:
        * **Mute** (*string*) - mute state ('*On*', '*Off*').
        """
        pass

    def SetRange(self, Min, Max):
        """ Set volume control object’s range.

        **Arguments**:
        * **Min** (*float*) - minimum voltage
        * **Max** (*float*) - maximum voltage
        """
        pass

    def SetSoftStart(self, SoftStart):
        """ Enable or Disable Soft Start.

        **Arguments**:
        * **SoftStart** (*string*) - Soft Start state ('*Enabled*', '*Disabled*').
        """
        pass
    