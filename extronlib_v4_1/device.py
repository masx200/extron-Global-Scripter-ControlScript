# pylint: disable=W0613, C0111, C0103
"""
The device package.

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

class eBUSDevice():
    """ Defines common interface to Extron eBUS panels\n

    **Arguments**:

    * **Host** (*object*) - handle to Extron ProcessorDevice to which the eBUSDevice is connected\n
    * **DeviceAlias** (*string*) - Device Alias of the Extron device\n

    **Parameters**:

    DeviceAlias:- **Returns** (*string*) - the device alias of the object
    Host:- **Returns** (*extronlib.device.ProcessorDevice*) - Handle to the Extron ProcessorDevice to which the eBUSDevice is connected.
    ID:- **Returns** (*int*) - device’s ID (set by DIP switch)
    InactivityTime:- **Returns** (*int*) - Seconds since last activity. :Note:: 0 = Active, Nonzero = Time of inactivity
    LidState:- **Returns** (*string*) - the current lid state ('*Opened*' or '*Closed*')
    ModelName:- **Returns** (*string*) - Model name of this device
    PartNumber:- **Returns** (*string*) - the part number of this device
    SleepState:- **Returns** (*string*) - the current sleep state of the device ('*Asleep*', '*Awake*')
    SleepTimer:- **Returns** (*int*) - sleep timer timeout
    SleepTimerEnabled:- **Returns** (*bool*) - *True* if sleep timer is enabled

    **Events**  
    InactivityChanged: :*Event*:: Triggers at times specified by *SetInactivityTime()* after state transition of inactivity timer. The callback takes two arguments. The first one is the *eBUSDevice* instance triggering the event and time with a float value of inactivity time in seconds.
    LidChanged: :*Event*:: Triggers when the Lid state changes.The callback takes two arguments. The first one is the *eBUSDevice* instance triggering the event and the second is the current lid state ('*Opened*' or '*Closed*').
    Offline: :*Event*:: Triggers when the device goes offline. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when the device comes online. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Online*').
    SleepChanged: :*Event*:: Triggers when sleep state changes. The callback takes two arguments. The first one is the *eBUSDevice* instance triggering the event and the second one is a string ('*Asleep*' or '*Awake*').
    """

    DeviceAlias = ''
    Host = None
    ID = 0
    InactivityChanged = None
    InactivityTime = 0
    LidChanged = None
    LidState = ''
    ModelName = ''
    Offline = None
    Online = None
    PartNumber = ''
    SleepChanged = None
    SleepState = ''
    SleepTimer = 0
    SleepTimerEnabled = False

    def __init__(self, Host, DeviceAlias):
        """ 
        eBUSDevice class constructor.\n

        **Arguments**:

        * **Host** (*object*) - handle to Extron ProcessorDevice to which the eBUSDevice is connected\n
        * **DeviceAlias** (*string*) - Device Alias of the Extron device\n
        """

        self.DeviceAlias = DeviceAlias
        self.Host = Host

    def Click(self, count=1, interval=None):
        """ Play default buzzer sound on applicable device

        **Arguments**:
        * **count** (*int*) - number of buzzer sound to play
        * **interval** (*int*) - time gap in millisecond between consecutive sounds
        """
        pass

    def GetMute(self, name):
        """ Get the mute state for the given channel

        The defined channel names are:
        * 'Click' - button click volume

        **Arguments**:
        * **name** (*string*) - name of channel. 
        
        **Returns** 
        * mute state ('On' or 'Off') (*string*)
        """
        pass

    def SetInactivityTime(self, times):
        """ Set the inactivity times of the *eBUSDevice*. When each time expires, the *InactivityChanged* event will be triggered. All times are absolute.
        
        **Arguments**:
        * **times** (*list of ints*) - list of times. Each time in whole seconds
        """
        pass

    def  SetMute(self, name, mute):
        """ Set the mute state for the given channel
        
        The defined channel names are:
        * 'Click' - button click volume

        **Arguments**:
        * **name** (*string*) - name of channel.
        * **mute** (*string*) - mute state ('On' or 'Off')

        """
        pass

    def  SetSleepTimer(self, state, time=None):
        """ Enable/disable sleep timer. Either 'On' or True enables sleep timer. 'Off' or False disables sleep timer.
        
        **Arguments**:
        * **state** (*bool, string*) - whether to enable the sleep timer
        * (*optional*) **time** (*int*) - time in seconds to sleep ()
        """
        pass

    def Sleep(self):
        """ Force the device to sleep immediately
        """
        pass

    def Wake(self):
        """ Force the device to wake up immediately
        """
        pass

class ProcessorDevice():
    """ Defines common interface to Extron Control Processors
    
    **Note**:
    * DeviceAlias must be a valid device Device Alias of an Extron device in the system.
    * If the part number is provided, the device will trigger a warning message in the program log if it does not match the connected device.
    
    **Arguments**:
    * **DeviceAlias** (*string*) - Device Alias of the Extron device
    * (*optional*) **PartNumber ** (*string*) - device’s part number

    **Parameters**:
    CurrentLoad:- **Returns** (*float*) - the current load of 12V DC power supply. This only applies to ProcessorDevice featuring 12V DC power supply. It returns *None* otherwise.
    DeviceAlias:- **Returns** (*string*) - the device alias of the object
    ExecutiveMode:- **Returns** (*int*) - The current executive mode number.
    FirmwareVersion:- **Returns** (*string*) - the firmware version of this device
    Hostname:- **Returns** (*string*) - the hostname of this device
    IPAddress:- **Returns** (*string*) - IP address of this device
    LinkLicenses:- **Returns** (*list of strings*) - List of LinkLicense® part numbers.
    MACAddress:- **Returns** (*string*) - MAC address of this device. For dual NIC devices, the LAN address is returned.
    ModelName:- **Returns** (*string*) - Model name of this device
    PartNumber:- **Returns** (*string*) - the part number of this device
    SerialNumber:- **Returns** (*string*) - Serial number of this device
    UserUsage:- **Returns** (*tuple of ints*) - user data usage of this device in KB (*used*, *total*).


    **Events**:
    ExecutiveModeChanged: :*Event*:: Triggers when executive mode changes. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is is the executive mode number.
    Offline: :*Event*:: Triggers when the device goes offline. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when the device comes online. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Online*').
    """
    CurrentLoad = 0.0
    DeviceAlias = ''
    ExecutiveMode = 0
    ExecutiveModeChanged = None
    FirmwareVersion = ''
    HostName = ''
    IPAddress = ''
    LinkLicenses = []
    MACAddress = ''
    ModelName = ''
    Offline = None
    Online = None
    PartNumber = None
    SerialNumber = ''
    UserUsage = (0,0)

    def __init__(self, DeviceAlias, PartNumber=None):
        """
        ProcessorDevice class constructor.

        **Arguments**:

        * **DeviceAlias** (*string*) - Device Alias of the Extron device
        * **PartNumber ** (*string*) - device’s part number
        """
        self.DeviceAlias = DeviceAlias
        self.PartNumber = PartNumber

    def SetExecutiveMode(self, ExecutiveMode):
        """ Sets the desired Executive Mode.

        :Note:: See product manual for list of available modes.

        **Arguments**:
        * **ExecutiveMode** (*int*) - The mode to set. 0 to n.
        """
        pass

class UIDevice():
    """Entity to communicate with Extron Device featuring user interactive input.

    **Note**:
    * DeviceAlias must be a valid device Device Alias of an Extron device in the system.
    * If the part number is provided, the device will trigger a warning message in the program log if it does not match the connected device.
    
    **Arguments**:

    * **DeviceAlias** (*string*) - Device Alias of the Extron device
    * (*optional*) **PartNumber ** (*string*) - device’s part number

    **Parameters**:

    AmbientLightValue:- **Returns** (*int*) - current ambient light value
    AutoBrightness:- **Returns** (*bool*) - current auto brightness state
    Brightness:- **Returns** (*int*) - current LCD brightness level
    DeviceAlias:- **Returns** (*string*) - the device alias of the object
    DisplayState:- **Returns** (*string*) - the current display state of the device ('*On*', '*Off*'). **Note**: This property is applicable to TLI only.
    DisplayTimer:- **Returns** (*int*) - Return display timer timeout seconds
    DisplayTimerEnabled:- **Returns** (*bool*) - current state of the display timer
    FirmwareVersion:- **Returns** (*string*) - the firmware version of this device
    Hostname:- **Returns** (*string*) - the hostname of this device
    IPAddress:- **Returns** (*string*) - IP address of this device
    InactivityTime:- **Returns** (*string*) - Seconds since last activity. **Note**: 0 = Active, Nonzero = Time of inactivity.
    LidState:- **Returns** (*string*) - the current lid state ('*Opened*' or '*Closed*')
    LightDetectedState:- **Returns** (*string*) - State of light detection. ('*Detected*', '*Not Detected*')
    MACAddress:- **Returns** (*string*) -MAC address of this device. **Note**: For dual NIC devices, the LAN address is returned.
    ModelName:- **Returns** (*string*) - Model name of this device
    MotionDecayTime:- **Returns** (*int*) - the period of time to trigger *MotionDetected* event after last motion was detected. The default (and minimum) value is 10 seconds.
    MotionState:- **Returns** (*string*) - the state of the Motion sensor (e.g. *Motion*, *No Motion*)
    PartNumber:- **Returns** (*string*) - the part number of this device
    SerialNumber:- **Returns** (*string*) - Serial number of this device
    SleepState:- **Returns** (*string*) - the current sleep state of the device ('*Asleep*', '*Awake*')
    SleepTimer:- **Returns** (*int*) - sleep timer timeout
    SleepTimerEnabled:- **Returns** (*bool*) - *True* if sleep timer is enabled
    UserUsage:- **Returns** (*tuple of ints*) - user data usage of this device in KB (*used*, *total*).
    WakeOnMotion:- **Returns** (*bool*) - current wake on motion state

    **Events**:
    BrightnessChanged: :*Event*:: Triggers when LCD brightness has changed. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and the second one is the current brightness level as an integer.
    HDCPStatusChanged: :*Event*:: Triggers when HDCP Status changes. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and state with a tuple: (Input, Status).
    InactivityChanged: :*Event*:: Triggers at times specified by *SetInactivityTime()* after state transition of inactivity timer. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and time with a float value of inactivity time in seconds.
    InputPresenceChanged: :*Event*:: Triggers when Input Presence changes. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and state with a tuple: (Input, Status).
    LidChanged: :*Event*:: Triggers when the Lid state changes. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and the second is the current lid state ('*Opened*' or '*Closed*').
    LightChanged: :*Event*:: Triggers when ambient light changes. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and the second is the ambient light level in the range of 0 ~ 255.
    MotionDetected: :*Event*:: Triggers when Motion is detected. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and the second one is a string ('*Motio*' or '*No Motion*')
    Offline: :*Event*:: Triggers when the device goes offline. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Offline*').
    Online: :*Event*:: Triggers when the device comes online. The callback takes two arguments. The first one is the *extronlib.device* instance triggering the event and the second one is a string ('*Online*').
    SleepChanged: :*Event*:: Triggers when sleep state changes. The callback takes two arguments. The first one is the *UIDevice* instance triggering the event and the second one is a string ('*Asleep*' or '*Awake*').

    """
    DeviceAlias = ''
    PartNumber = ''
    AmbientLightValue = 0
    AutoBritgtness = True
    Brightness = 0
    BrightnessChanged = None
    DisplayState = ''
    DisplayTimer = 0
    DisplayTimerEnabled = True
    FirmwareVersion = ''
    HDCPStatusChanged = None
    Hostname = ''
    IPAddress = ''
    InactivityChanged = None
    InactivityTime = 0
    InputPresenceChanged = None
    LidChanged = None
    LidState = ''
    LightChanged = None
    LightDetectedState = ''
    MACAddress = ''
    ModelName = ''
    MotionDecayTime = 0
    MotionDetected = None
    MotionState = ''
    Offline = None
    Online = None
    PartNumber = ''
    SerialNumber = ''
    SleepChanged = None
    SleepState = ''
    SleepTimer = 0
    SleepTimerEnabled = False
    UserUsage = (0,0)
    WakeOnMotion = False

    def __init__(self, DeviceAlias, PartNumber=None):
        """
        UIDevice class constructor.

        **Arguments**:

        * **DeviceAlias** (*string*) - Device Alias of the Extron device
        * (*optional*) **PartNumber ** (*string*) - device’s part number
        """
        
        self.DeviceAlias = DeviceAlias
        self.PartNumber = PartNumber

    def Click(self, count=1, interval=None):
        """ Play default buzzer sound on applicable device

        **Arguments**:
        * (*optional*) **count** (*int*) - number of buzzer sound to play
        * (*optional*) **interval** (*float*) - time gap between the starts of consecutive buzzer sounds

        :Note:: If count is greater than 1, interval must be provided.
        """
        pass

    def GetHDCPStatus(self, videoInput):
        """ Return the current HDCP Status for the given input.

        **Arguments**:
        * **videoInput** (*string*) - input ('*HDMI*' or '*XTP*')
        
        **Returns**:
        * *True* or *False* (*bool*)
        """
        return True

    def  GetInputPresence(self, videoInput):
        """ Return the current input presence status for the given input.

        **Arguments**:
        * **videoInput** (*string*) - input ('*HDMI*' or '*XTP*')
        
        **Returns**:
        * *True* or *False* (*bool*)
        """
        return True

    def  GetMute(self, name):
        """ Get the mute state for the given channel

        The defined channel names are:
        * '*Master*' - the master volume
        * '*Speaker*' - the built-in speakers
        * '*Line*' - the line out
        * '*Click*' - button click volume
        * '*Sound*' - sound track playback volume
        * '*HDMI*' - HDMI input volume
        * '*XTP*' - XTP input volume

        **Arguments**:
        * **name** (*string*) - name of channel.
        
        **Returns**:
        * mute state ('*On*' or '*Off*') (*string*)
        """
        return ''

    def  GetVolume(self, name):
        """ Return current volume level for the given channel

        The defined channel names are:  
        * '*Master*' - the master volume
        * '*Click*' - button click volume
        * '*Sound*' - sound track playback volume
        * '*HDMI*' - HDMI input volume
        * '*XTP*' - XTP input volume

        **Arguments**:
        * **name** (*string*) - name of volume channel.
        
        **Returns**:
        * volume level (*int*)
        """
        return 0

    def HideAllPopups(self):
        """ Dismiss all popup pages
        """
        pass

    def HidePopup(self, popup):
        """ Hide popup page

        **Arguments**:
        * **popup** (*int, string*) - popup page number or name
        """
        pass

    def HidePopupGroup(self, group):
        """ Hide all popup pages in a popup group

        **Arguments**:
        * **group** (*int*) - popup group number
        """
        pass

    def PlaySound(self, filename):
        """ Play a sound file identified by the filename

        **Arguments**:
        * **filename** (*string*) - name of sound file

        **Note**:
        * Only WAV files can be played.
        * A subsequent call will preempt the currently playing file.
        * Sound file must be added to the project file.
        """
        pass

    def SetAutoBrightness(self, state):
        """ Set auto brightness state. Either '*On*' or *True* turns on auto brightness. '*Off*' or *False* turns off auto brightness.
        
        **Arguments**:
        * **state** (*bool, string*) - whether to enable auto brightness
        """
        pass

    def SetBrightness(self, level):
        """ Set LCD screen brightness level

        **Arguments**:
        * **level** (*int*) - brightness level from 0 ~ 100
        """
        pass

    def SetDisplayTimer(self, state, timeout):
        """ Enable/disable display timer. Either '*On*' or *True* enables display timer. '*Off*' or *False* disables display timer.
        
        **Arguments**:
        * **state** (*bool, string*) - whether to enable the display timer
        * **timeout** (*int*) - time in seconds before turn off the display
        """
        pass

    def SetInactivityTime(self, times):
        """ Set the inactivity times of the *UIDevice*. When each time expires, the *InactivityChanged* event will be triggered. All times are absolute.
        
        **Arguments**:
        * **times** (*list of ints*) - list of times. Each time in whole seconds
        """
        pass

    def SetInput(self, videoInput):
        """ Sets the input. Inputs must be published for each device.
        
        **Arguments**:
        * **videoInput** (*string*) - input to select ('*HDMI*' or '*XTP*')
        """
        pass

    def SetLEDBlinking(self, ledId, rate, stateList):
        """ Make the LED cycle, at ADA compliant rates, through each of the states provided.

        **Blink rates**:

        +-----------+-------------+
        | Rate      | Frequency   |
        +===========+=============+
        | Slow      | 0.5 Hz      |
        +-----------+-------------+
        | Medium    | 1 Hz        |
        +-----------+-------------+
        | Fast      | 2 Hz        |
        +-----------+-------------+

        :Note:: Using this function will blink in unison with other LEDs.

        **Arguments**:
        * **ledId** (*int*) - LED id
        * **rate** (*string*) - ADA compliant blink rate. ('*Slow*', '*Medium*', '*Fast*')
        * **stateList** (*list of strings*) - List of colors

        :Note:: Available colors are *Red*, *Green*, and *Off*.
        """
        pass

    def SetLEDState(self, ledId, state):
        """ Drive the LED to the given color

        **Arguments**:
        * **ledId** (*int*) - LED id
        * **rate** (*string*) - LED color or ‘*Off*’.
        """
        pass

    def SetMotionDecayTime(self, duration):
        """ Set the period of time to trigger *MotionDetected* after last motion was detected.

        **Arguments**:
        * **duration** (*float*) - time in seconds (minimum/default value is 10)
        """
        pass
    
    def SetMute(self, name, mute):
        """ Set the mute state for the given channel

        The defined channel names are:
        * '*Master*' - the master volume
        * '*Speaker*' - the built-in speakers
        * '*Line*' - the line out
        * '*Click*' - button click volume
        * '*Sound*' - sound track playback volume
        * '*HDMI*' - HDMI input volume
        * '*XTP*' - XTP input volume

        **Arguments**:
        * **name** (*string*) - name of channel.
        * **mute** (*string*) - mute state ('*On*' or '*Off*')
        """
        pass

    def SetSleepTimer(self, state, duration=None):
        """ Enable/disable sleep timer. Either '*On*' or *True* enables sleep timer. '*Off*' or *False* disables sleep timer.
        
        **Arguments**:
        * **state** (*bool, string*) - name of channel.
        * (*optional*) **duration** (*int*) - time in seconds to sleep
        """
        pass

    def SetVolume(self, name, level):
        """ Adjust volume level for the given channel

        The defined channel names are:
        * '*Master*' - the master volume
        * '*Click*' - button click volume
        * '*Sound*' - sound track playback volume
        * '*HDMI*' - HDMI input volume
        * '*XTP*' - XTP input volume

        **Arguments**:
        * **name** (*string*) - name of channel.
        * **level** (*int*) - volume level 0 ~ 100
        """
        pass

    def SetWakeOnMotion(self, state):
        """ Enable/disable wake on motion.

        **Arguments**:
        * **state** (*bool, string*) - *True* ('*On*') or *False* (‘*Off*’) to enable and disable wake on motion, respectively.
        """
        pass

    def ShowPage(self, page):
        """ Show page on the screen

        **Arguments**:
        * **page** (*int, string*) - absolute page number or name
        """
        pass

    def ShowPopup(self, popup, duration=0):
        """ Display pop-up page for a period of time.

        **Arguments**:
        * **page** (*int, string*) - pop-up page number or name
        * (*optional*) **duration** (*float*) - duration the pop-up remains on the screen. 0 means forever.
        
        :Note:: If a pop-up is already showing for a finite period of time, calling this method again with the same pop-up will replace the remaining period with the new period.
        """
        pass

    def Sleep(self):
        """ Force the device to sleep immediately
        """
        pass

    def StopSound(self):
        """ Stop playing sound file
        """
        pass

    def Wake(self):
        """ Force the device to wake up immediately
        """
        pass

    