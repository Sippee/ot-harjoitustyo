# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Kaavio](./kuvat/arkkitehtuuri-luokkakaavio.png)

Kaikista näistä vastaavat koodit ovat omissa pakkauksissa.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Tulostaulu / Pelin aloitus
- Peli

Kolme ensimmäistä ovat toteutettu omana luokaanaan. Pelin pitäisi olla toteutettu luokkana, mutta se on tällä hetkellä voin methodi, jolla on muutama luokaa auttamassa. UI vastaa käyttöliitymästä, eli näkymistä.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostaa luokka User, joka kuvaa käyttäjiä.

Service luokka vastaa toiminnallisuuksista.

Service käsittelee UserRepository luokkaa, joka vastaa tietojen tallennuksesta, ja main_game methodia, joka on pelin päärunko tällä hetkellä.

## Tietojen pysyväistallennus

Pakkauksen repositories luokka UserRepository huolehtii tietojen tallentamisesta. Tiedot tallennetaan SQLite-tietokantaan.

### Tiedosto

Sovellus tallentaa käyttäjien tiedostoon data.db, joka on hakemistossa data projektin juuressa.

SQLite-tietokanta alustetaan initialize_database.py-tiedostolla. Tieto tallentuu user tauluun.

## Päätoiminnallisuudet

### Käyttäjän kirjaantuminen

Kun kirjautumisnäkymän syötekenttiin kirjoitetaan käyttäjätunnus ja salasana, jonka jälkee klikataan painiketta "Login", etenee sovelluksen kontrolli seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-login.PNG)

Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan Service metodia login. UserRepository avulla tarkastetaan ovatko kirjautumistiedot oikeat. Päästään MainViewiin sovelluksen päänäkymään ja nähdään myös tulostaulun, joka esittää 10 parhaan pisteet.

### Uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus, joka ei ole jo käytössä sekä salana, jonka jälkee klikataan painiketta "Create" etenee sovelluksen kontrolli seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-register.PNG)'

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia create_user. UserRepositoryn avulla tarkastetaan ja luodaan uusi käyttäjä. Päästään MainViewiin sovelluksen päänäkymään. Käyttäjä kirjautuu automaattisesti sisään, kun se on luotu.

### Pelin aloitus

Uuden pelin aloitus painamalla painiketta "Play" klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

![image](kuvat/arkkitehtuuri-seq-diagram-game.PNG)

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia game. Sovelluslogiikka kutsuu tämän jälkeen coincollector pelin metodia main_game. Pelin päättyessä se tallentaa pisteet tietokantaan, jos pisteet ylittävät edelliset pisteet. main_game metodi palauttaa sovelluslogiikalle pistemäärän, ja sovelluslogiikka palauttaa tämän pistemäärän käyttöliittymälle, joka luo pop-up ikkunan, jossa kerrotaan saatujen pisteiden määrä. Peli sammuu ja ollaa päänäkymässä.
