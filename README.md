![purwadhikaLogo](https://d1ah56qj523gwb.cloudfront.net/uploads/organizations/logos/1538557444-kcgv11HXelvcOnlyrGcEpfwAf6hbPMhC.png)

# Web Scraping List of Digimons from *wikimon.net* using BeautifulSoup
### Web Scraping
Web scraping is a method to copy the data in a certain website without having to copy paste it manually,especially for website that has no available API.

Scraping list of digimons from https://wikimon.net/Visual_List_of_Digimon, to get the name of the digimon and the digimon photo's URL using *BeautifulSoup*. Check out the screenshot of the wikimon web page:
![wikimon](./ss1.png)

Then store the output data into *CSV* file first before saving it into *mySQL* database.
1. Install *Beautiful Soup* package using:
    ```bash
    $ pip install beautifulsoup4
    ```
    Or using another writing method:
    ```bash
    $ py -m pip install beautifulsoup4
    ```

2. Clone this repo and create initial mySQL database. From terminal:
    ```bash
    $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
    $ mySQL -u <yourUsername> -p
    $ Enter password: <yourPassword>
    $ create database digimon;
    $ use digimon;
    $ create table digimon(
        -> id int auto_increment,
        -> name varchar(255),
        -> pict varchar(255),
        -> primary key(id));
    $ describe digimon; # to check the created table        
    ```

3. Cloe this repo and *run* the program. The CSV file that holds the output digimon data will be named *listDigimon.csv*. A screenshot of how the CSV will look like:
    ![CSVdigimon](./ss3.png)

4. The digimon list database has also been created into your mySQL! To check the data in table *digimon* in your mySQL:
    ```bash
    $ select * from digimon;
    ```
    and the screenshot of how the database will look like:
        ![SQLdigimon](./ss2.png)

### **_Enjoy!_**

#

#### Albertus Rianto Wibisono ✉ _albertusrian95@gmail.com_

[Instagram](https://www.instagram.com/rian__wibisono) | 
[LinkedIn](https://www.linkedin.com/in/albertusrian95/) |
[GitHub](https://www.github.com/RiantoWibisono)
