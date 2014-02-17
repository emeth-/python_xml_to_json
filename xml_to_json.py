##  Copyright (c) 2014 Sean Kooyman
## Based off pesterfish, which is Copyright (c) 2010 Jacob Smullyan (https://bitbucket.org/smulloni/pesterfish)

##  Permission is hereby granted, free of charge, to any person
##  obtaining a copy of this software and associated documentation
##  files (the "Software"), to deal in the Software without
##  restriction, including without limitation the rights to use,
##  copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the
##  Software is furnished to do so, subject to the following
##  conditions:

##  The above copyright notice and this permission notice shall be
##  included in all copies or substantial portions of the Software.

##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
##  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
##  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
##  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
##  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
##  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
##  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
##  OTHER DEALINGS IN THE SOFTWARE.

"""
Usage:
from xml_to_json import xml_str_to_json_str
json_str = xml_str_to_json_str(xml_str)
"""

try:
    import xml.etree.cElementTree as ET
except ImportError:
    try:
        import xml.etree.ElementTree as ET
    except ImportError:
        try:
            import cElementTree as ET
        except ImportError:
            try:
                import lxml.etree as ET
            except ImportError:
                import elementtree.ElementTree as ET

import json

def elem_to_dict_helper_func(elem):
    d=dict(tag=elem.tag)
    if elem.text:
        d['text']=elem.text
    if elem.attrib:
        d['attributes']=elem.attrib
    children=elem.getchildren()
    if children:
        d['children']=map(elem_to_dict_helper_func, children)
    if elem.tail:
        d['tail']=elem.tail
    return d
                   
def xml_str_to_json_str(xml):
    elem = ET.fromstring(xml)
    if hasattr(elem, 'getroot'):
        elem=elem.getroot()
    return json.dumps(elem_to_dict_helper_func(elem))
    