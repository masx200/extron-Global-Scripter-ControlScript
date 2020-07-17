# pylint: disable=W0613, C0111, C0103, C0301
"""
Init file with a couple of functions.

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

__all__ = ['Version', 'event']

def Version():
    """ Return the Extron Library version string in the form of <major>.<minor>.<revision>
    """
    return ''

def event(Object, EventName):
    """ Decorate a function to be the handler of Object when EventName happens.

    The decorated function must have the exact signature as specified by the definition of EventName, which must appear in the Object class or one of its parent classes. Lists of objects and/or events can be passed in to apply the same handler to multiple events.
    """
    pass




































