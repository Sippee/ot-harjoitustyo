# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Kaavio](./kuvat/arkkitehtuuri-luokkakaavio.png)

Pakkaus ui sisältää käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus entities sisältää luokan user, joka kuvaa sovelluksen käyttämää käyttäjä tietokohdetta.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Tulostaulu / Pelin aloitus
- Peli

Kolme ensimmäistä ovat toteutettu omana luokaanaan. Pelin pitäisi olla toteutettu luokkana, mutta se on tällä hetkellä voin methodi, jolla on muutama luokaa auttamassa. Kaikki näkymät, paitsi peli, ovat aina yksin näkyvillä. Peli ja tulostaulu ovat samaan aikaa auki. Näkymistä vastaa UI-luokka. Käyttöliittymä on eristetty sovelluslogiikasta. Kutsutaan servicestä methodeja.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostaa luokka User, joka kuvaa käyttäjiä.

Toiminnallisista kokonaisuuksista vastaa luokan Service olio. Luokkalla on käyttöliittymälle käytettäviä methodeja.  
Esimerkiksi:
- login(username, password)
- logout()
- top10_hiscore()

Service käsittelee UserRepository luokkaa, joka vastaa tietojen tallennuksesta, ja main_game methodia, joka on pelin päärunko tällä hetkellä. Luokkien toteutuksen injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

## Tietojen pysyväistallennus

Pakkauksen repositories luokka UserRepository huolehtii tietojen tallentamisesta. UserRepository-luokka käyttää SQLite-tietokantaa.

### Tiedosto

Sovellus tallentaa käyttäjien tiedostoon, joka on juuressa olevassa hakemistossa data, nimeltä data.db.

Käyttäjä tiedot tallentuu siis SQLite-tietokantaa tauluun user, joka alustetaan initialize_database.py-tiedostossa

## Päätoiminnallisuudet

### Käyttäjän kirjaantuminen

Kun kirjautumisnäkymän syötekenttiin kirjoitetaan käyttäjätunnus ja salasana, jonka jälkee klikataan painiketta "Login", etenee sovelluksen kontrolli seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-login.PNG)

Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan Service metodia login antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää UserRepositoryn avulla onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasanat. Jos salasanat täsmäävät, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi MainView, eli sovelluksen päänäkymän ja näyttää myös tulostaulun, joka esittää 10 parhaan pisteet.

### Uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus, joka ei ole jo käytössä sekä salana, jonka jälkee klikataan painiketta "Create" etenee sovelluksen kontrolli seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-register.PNG)'

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia create_user antaen parametriksi luotavan käyttäjän tiedot. Sovelluslogiikka selvittää UserRepositoryn avulla onko käyttäjätunnus olemassa. Jos ei, eli uuden käyttäjän luominen on mahdollista, luo sovelluslogiikka User-olion ja tallettaa sen kutsumalla UserRepositoryn metodia create. Tästä seurauksena on se, että käyttöliittymä vaihtaa näkymäksi MainView:n. Luotu käyttäjä kirjataan automaattisesti sisään.

### Pelin aloitus

Uuden pelin aloitus painamalla painiketta "Play" klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-game.PNG)

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia game. Sovelluslogiikka kutsuu tämän jälkeen coincollector pelin metodia main_game. Pelin päättyessä se tallentaa pisteet tietokantaan, jos pisteet ylittävät edelliset pisteet. main_game metodi palauttaa sovelluslogiikalle pistemäärän, ja sovelluslogiikka palauttaa tämän pistemäärän käyttöliittymälle, joka luo pop-up ikkunan, jossa kerrotaan saatujen pisteiden määrä. Peli sammuu ja ollaa päänäkymässä.

### Muut toiminnaliisuudet

Samalla periaatteella toimii myös muutkin asiat.

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Pylint ilmoittaa toistuvuuksissa kahdessa käyttöliittymään kuuluvista luokista.
