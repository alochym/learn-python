# BeautifulSoup

## Installation Python Virtual Enviroment

1. sudo apt install python3.8-venv

### Setup Python Virtual Enviroment

Using Requests and Beautiful Soup version 4

| No  | Modules        | Description                                                |
| --- | -------------- | ---------------------------------------------------------- |
| 01  | requests       | using to make HTTP Requests to web site                    |
| 02  | beautifulsoup4 | Using to parse text to the HTML Documents                  |
| 03  | selenium       | Using to automate Microsoft Edge browser enable javascript |

1. Using browser
   1.Google Chrome driver - Version 117.0.5938.92
   2.Google Chrome - Version 117.0.5938.92
   3. https://www.pythonrequests.com/python-requests-you-need-to-enable-javascript/
2. python3 -m venv .env
3. source .env/bin/activate
4. pip install requests beautifulsoup4 lxml selenium

## HTML Content

1. [Amozon Fire TV Stick 4k](./Amazon-Fire-TV-Stick-4K-Max-streaming-device.html)
2. https://www.amazon.com/dp/B0BP9SNVH9

## Beautiful Soup Objects

### BeautifulSoup Object

1. The BeautifulSoup object represents the parsed document as a whole.
2. For most purposes, you can treat it as a ***Tag object***.

#### Searching the tree

1. (CSS selectors)[https://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors]
2. [find_all() function](https://beautiful-soup-4.readthedocs.io/en/latest/#find-all)

#### Navigation Tree

##### Going Down

1. Using ***Tag names*** - ***soup.head***
2. Using ***.contents*** - A tag’s children are available in a list called ***.contents***
3. Using ***.children***
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   for c in soup.html.head.children:
     print(c)
 
   """
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="light dark" name="color-scheme"/>
   """
   ```

4. Using ***.descendants*** lets you iterate over all of a tag’s children, recursively: 
   1. Its direct children
   2. The children of its direct children, and so on.

      ```python
      from bs4 import BeautifulSoup
      with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
          soup = BeautifulSoup(f, "lxml")

      for c in soup.html.body.table.tbody.tr.children:
         print(c)

      """ 
      <td class="line-number" value="1"></td>
      <td class="line-content"><span class="html-doctype">&lt;!doctype html&gt;</span><span class="html-tag">&lt;html <span class="html-attribute-name">lang</span>="<span class="html-attribute-value">en-us</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">a-no-js</span>"
                              <span class="html-attribute-name">data-19ax5a9jf</span>="<span class="html-attribute-value">dingo</span>"&gt;</span><span class="html-comment">&lt;!--
                              sp:feature:head-start --&gt;</span></t      
      """
      ```

##### Going Up

1. Every tag and every string has a ***parent*** - using ***.parent***.
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   print(soup.html.head.parent)
 
   """
   <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="light dark" name="color-scheme"/>
   </head>
   """
   ```

##### Going sideways

1. Using ***.next_sibling*** and ***.previous_sibling*** to navigate between page elements `that are on the same level` of the HTML document.
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   print(soup.html.head.parent)
 
   """
   <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="light dark" name="color-scheme"/>
   </head>
   """
   ```

2. Using ***.next_siblings*** and **.previous_siblings** to iterate over a tag’s siblings
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   for n in soup.html.head.meta.next_siblings:
     print(n)

   """
    <meta content="light dark" name="color-scheme"/>
   """
   ```

##### Going back and forth

1. Using ***.next_element*** and ***.previous_element***
2. Using ***.next_elements*** and ***.previous_elements*** to iterators to move forward or backward in the document.

### Comment Object
### NavigableString Object

1. A string corresponds to a bit of text within a tag.
2. If a tag has only one child, and that child is a NavigableString - ***soup.html.title***.
3. If a tag contains more than one thing, then it’s not clear what .string should refer to, so .string is defined to be ***None***.
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   print(soup.html.string)

   """
   html
   """
   ```

### Tags Object

1. A Tag object corresponds to an XML or HTML tag in the original document.
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   type(soup.html.body)
   # <class 'bs4.element.Tag'>

   print(soup.html.head)

   """
   <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="light dark" name="color-scheme"/>
   </head>
   """
   ```

#### Tags Name

1. Every tag has a name.
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   print(soup.html.name)

   """
   html
   """
   ```

#### Tags Attributes

1. A tag may have any number of attributes.
2. You can access to its attributes.
3. [Multi-valued attributes](https://beautiful-soup-4.readthedocs.io/en/latest/#multi-valued-attributes)
   
   ```python
   from bs4 import BeautifulSoup

   with open("Amazon-Fire-TV-Stick-4K-Max-streaming-device.html") as f:
     soup = BeautifulSoup(f, "lxml")

   # access to class attributes.
   print(soup.html.body.div["class"])

   """
   ['line-gutter-backdrop']
   """

   # check numbers of attributes.
   print(soup.html.body.table.tbody.tr.td.attrs)
   # {'class': ['line-number'], 'value': '1'}
   ```

