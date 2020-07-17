# pylint: disable=W0613, C0111, C0103, C0301
"""
The ui package.

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

class Button():
    """ Representation of Hard/Soft buttons

    A button may trigger several events depending on the configuration; however, Touch Panels only issue Pressed and Released messages to the controller. Other events (e.g., Held, Repeated) are timer driven within the Button instance.
    
    **Arguments**:
    * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
    * **ID** (*int,string*) - ID or Name of the UIObject
    * (*optional*) **holdTime** (*float*) - Time for *Held* event. Held event is triggered only once if the button is pressed and held beyond this time. If holdTime is given, it must be a floating point number specifying period of time in seconds of button being pressed and held to trigger Held event.
    * (*optional*) **repeatTime** (*float*) - Time for *Repeated* event. After holdTime expires, the Repeated event is triggered for every additional repeatTime of button being held. If repeatTime is given, it must be a floating point number specifying time in seconds of button being held.

    :Note:: If button is released before *holdTime* expires, a *Tapped* event is triggered instead of a *Released* event. If the button is released after *holdTime* expires, there will be no *Tapped* event.

    **Parameters**:
    BlinkState:- **Returns** (*string*) - the current blink state ('*Not blinking*' or '*Blinking*')
    Enabled:- **Returns** (*bool*) - *True* if the control object is enabled else *False*
    Host:- **Returns** (*extronlib.device.UIDevice*) - UIDevice object that hosts this control object
    ID:- **Returns** (*int*) - the object ID
    Name:- **Returns** (*string*) - the object Name
    PressedState:- **Returns** (*bool*) - *True* if the button is pressed, else *False*
    State:- **Returns** (*int*) - the current visual state number
    > :Note:: It does not return the current state if the button is blinking.
    Visible:- **Returns** (*bool*) - *True* if the control object is visible else *False*

    
    **Events**:
    Held: :*Event*:: Get/Set the callback when hold expire event is triggered. The callback function must accept exactly two parameters, which are the *Button* that triggers the event and the state (e.g. ‘Held’).
    Pressed: :*Event*:: Get/Set the callback when the button is pressed. The callback function must accept exactly two parameters, which are the *Button* that triggers the event and the state (e.g. ‘Pressed’).
    Released: :*Event*:: Get/Set the callback when the button is released. The callback function must accept exactly two parameters, which are the *Button* that triggers the event and the state (e.g. ‘Held’).
    Repeated: :*Event*:: Get/Set the callback when repeat event is triggered. The callback function must accept exactly two parameters, which are the *Button* that triggers the event and the state (e.g. ‘Repeated’).
    Tapped: :*Event*:: Get/Set the callback when tap event is triggered. The callback function must accept exactly two parameters, which are the *Button* that triggers the event and the state (e.g. ‘Tapped’).
    """
    UIHost = None
    ID = 0
    holdTime = 0.0
    repeatTime = 0.0
    BlinkState = ''
    Enabled = True
    Held = None
    Name = ''
    Pressed = None
    PressedState = True
    Released = None
    Repeated = None
    State = 0
    Tapped = None
    Visible = True

    def __init__(self, UIHost, ID, holdTime=None, repeatTime=None):
        """ Button class constructor.

        **Arguments**:
        * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
        * **ID** (*int,string*) - ID or Name of the UIObject
        * (*optional*) **holdTime** (*float*) - Time for *Held* event. Held event is triggered only once if the button is pressed and held beyond this time. If holdTime is given, it must be a floating point number specifying period of time in seconds of button being pressed and held to trigger Held event.
        * (*optional*) **repeatTime** (*float*) - Time for *Repeated* event. After holdTime expires, the Repeated event is triggered for every additional repeatTime of button being held. If repeatTime is given, it must be a floating point number specifying time in seconds of button being held.
        """
        self.UIHost = UIHost
        self.ID = ID
        self.holdTime = holdTime
        self.repeatTime = repeatTime

    def CustomBlink(self, rate, stateList):
        """ Make the button cycle through each of the states provided.

        **Arguments**:
        * **rate** (*float*) - duration of time in seconds for one visual state to stay until replaced by the next visual state.
        * **stateList** (*list of ints*) - list of visual states that this button blinks among.
        """
        pass

    def SetBlinking(self, rate, stateList):
        """ Make the button cycle, at ADA compliant rates, through each of the states provided.

        +-----------+-------------+
        | Rate      | Frequency   |
        +===========+=============+
        | Slow      | 0.5 Hz      |
        +-----------+-------------+
        | Medium    | 1 Hz        |
        +-----------+-------------+
        | Fast      | 2 Hz        |
        +-----------+-------------+

        :Note:: Using this function will blink in unison with other buttons.

        **Arguments**:
        * **rate** (*string*) - ADA compliant blink rate. ('*Slow*', '*Medium*', '*Fast*')
        * **stateList** (*list of ints*) - list of visual states that this button blinks among.
        
        """
        pass

    def SetEnable(self, enable):
        """ Enable or disable an UI control object.

        **Arguments**:
        * **enable** (*bool*) - *True* to enable the object or *False* to disable it.
        """
        pass

    def SetState(self, State):
        """ Set the current visual state

        **Arguments**:
        * **State** (*int*) - visual state number

        :Note:: Setting the current state stops button from blinking, if it is running. (*SetBlinking()*)
        """
        pass

    def SetText(self, text):
        """ Specify text to display on the UIObject

        **Arguments**:
        * **text** (*string*) - text to display

        **Raises**:
        * TypeError
        """
        pass

    def SetVisible(self, visible):
        """ Change the visibility of an UI control object.

        **Arguments**:
        * **visible** (*bool*) - *True* to make the object visible or *False* to hide it.
        """
        pass

class Knob():
    """ Knob is a rotary control that has 36 steps for a full revolution

    **Arguments**:
    * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
    * **ID** (*int*) - ID of the UIObject
    
    **Parameters**:
    Host:- **Returns** (*extronlib.device.UIDevice*) - UIDevice object that hosts this control object
    ID:- **Returns** (*int*) - the object ID
    
    **Events**:
    Turned: :*Event*:: Get/Set callback when knob is turned. The callback takes two parameters. The first one is the *Knob* itself and the second one is a signed integer indicating steps that was turned. Positive values indicate clockwise rotation.
    """
    UIHost = None
    ID = 0
    Turned = None

    def __init__(self, UIHost, ID):
        """ Knob class constructor.

        **Arguments**:
        * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
        * **ID** (*int*) - ID of the UIObject
        """
        self.UIHost = UIHost
        self.ID = ID

class Label():
    """ Label object displays text string on the screen

    **Arguments**:
    * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
    * **ID** (*int,string*) - ID or Name of the UIObject
    
    **Parameters**:
    Host:- **Returns** (*extronlib.device.UIDevice*) - UIDevice object that hosts this control object
    ID:- **Returns** (*int*) - the object ID
    Name:- **Returns** (*string*) - the object Name
    Visible:- **Returns** (*bool*) - *True* if the control object is visible else *False*
    """
    UIHost = None
    ID = 0
    Name = ''
    Visible = True

    def __init__(self, UIHost, ID):
        """ Label class constructor.

        **Arguments**:
        * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
        * **ID** (*int,string*) - ID or Name of the UIObject
        """
        self.UIHost = UIHost
        self.ID = ID

    def SetText(self, text):
        """ Specify text to display on the UIObject

        **Arguments**:
        * **text** (*string*) - text to display
        
        **Raises**:
        * TypeError
        """
        pass

    def SetVisible(self, visible):
        """ Change the visibility of an UI control object.

        **Arguments**:
        * **visible** (*bool*) - *True* to make the object visible or *False* to hide it.
        """
        pass

class Level():
    """ This module defines interfaces of Level UI.

    **Arguments**:
    * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
    * **ID** (*int*) - ID of the UIObject

    **Parameters**:
    Host:- **Returns** (*extronlib.device.UIDevice*) - UIDevice object that hosts this control object
    ID:- **Returns** (*int*) - the object ID
    Level:- **Returns** (*int*) - the current level
    Max:- **Returns** (*int*) - the upper bound of the level object
    Min:- **Returns** (*int*) - the lower bound of the level object
    Name:- **Returns** (*string*) - the object Name
    Visible:- **Returns** (*bool*) - *True* if the control object is visible else *False*
    """
    UIHost = None
    ID = 0
    Name = ''
    Visible = True
    Level = 0
    Max = 0
    Min = 0

    def __init__(self, UIHost, ID):
        """ Level class constructor.

        **Arguments**:
        * **UIHost** (*extronlib.device.UIDevice*) - Device object hosting this UIObject
        * **ID** (*int*) - ID of the UIObject
        """
        self.UIHost = UIHost
        self.ID = ID

    def Dec(self):
        """ Nudge the level down a step
        """
        pass

    def Inc(self):
        """ Nudge the level up a step
        """
        pass

    def SetLevel(self, Level):
        """ Set the current level

        **Arguments**:
        * **Level** (*int*) - Discrete value of the level object
        """
        pass

    def SetRange(self, Min, Max, Step=1):
        """ Set level object’s allowed range and the step size

        **Arguments**:
        * **Min** (*int*) - Minimum level
        * **Max** (*int*) - Maximum level
        * (*optional*) **Step** (*int*) - Optional step size for *Inc()* and *Dec()*.
        """
        pass

    def SetVisible(self, visible):
        """ Change the visibility of an UI control object.

        **Arguments**:
        * **visible** (*bool*) - *True* to make the object visible or *False* to hide it.
        """
        pass