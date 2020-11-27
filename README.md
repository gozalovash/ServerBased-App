#  Served Based App

Server-Client based Console Application for webscraping.

## Prerequisites

- Python3
- OOP understanding


## Libraries used

```python
import socket
import argparse
import requests
from bs4 import BeautifulSoup
```
## Content
- Server.py - Server part of program, which performs operations, requested by client
- web_scraper.py - Client part, send request with the name of webpage to the Server and prints result

  #### Scenario
 > You as a software developer must create the client-server-based console app “web_scraper”. With the next abilities:
Get statistical data: 
-Calculate the number of pictures in the webpage
-Calculate the number of the leaf paragraphs in the webpage


   #### Task
>Create console-based app with two roles server and the client. The server must be started and wait the request from the client. 
Server must produce the web scraping of the webpage to get two parameters: the number of pictures and the number of the leaf paragraphs. 
The leaf paragraphs in HTML document represents only the last paragraphs in the nested paragraph structures (picture below marks with blue the paragraphs). 
Use and modify the algorithm to calculate the leaf nodes!
        <p>
                             /          \
                     <p>          <p>
                                   /         \
                             <p>     <p>
 The client must send the request to the server to get the proper answer. The client  has options  page (-p) to get the statistical data. 
 All the cacluation must be done on the server side
   

## Usage

First run the program as server:

```
python web_scraper.py server
```
Then as a client, providing necessary arguments:

```
python web_scraper.py client [-p Page] {webpage}
```
Example:
```
python web_scraper.py -p www.cisco.com
```


