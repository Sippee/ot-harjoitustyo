# Arkkitehtuurikuvaus

## Rakenne
Ohjelmalla on kolmitasoinen kerrosarkkitehtuuri.  
![Ohjelman nykyinen arkkitehtuuri](https://github.com/Sippee/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/arkkitehtuurikuva.png?raw=true)  
Repositories sisältää tietojen tallennuksesta vastaavan koodin, ja entities sisältää luokista vastaavan koodin. Ui sisältää käyttöliittymän ja services sovelluslogiikan.
## Käyttöliittymä
Käyttöliittymä koostuu kolmesta eri sivusta, kirjautumis sivusta, uuden käyttäjän luomis sivusta ja tehtävä sivusta.  
Kerralla nähdään vai yksi sivu. Sivuista huolehtii ui luokka.
## Sovelluslogiikka
Sovelluslogiikan pohja muodostuu luokista User- ja Exercise-luokista ja luokka Service huolehtii sovelluslogiikan kokonaisuudesta. Service vastaa kaikista toiminnallisista käskyistä. Service-luokka hallitsee molempien repositorioiden toiminnan.   
## Tiedon tallennus
Tiedon tallennusta varten meillä on repositorio hakemistossa luokat UserRepository ja ExerciseReposity, jotka huolehtivat käyttäjän tietojen tallentamisesta SQLite-tietokannan avulla ja tehtävien tallentamisesta .csv tiedostoon.  
Molemmat tiedostot ovat kansiossa data hakemiston juuressa.
## Päätoiminnallisuudet
### Sovellukseen kirjautuminen
Kirjautuminen toimii helposti kirjoittamalla tunnus ja salasana kenttiin ja painamalla Login.
### Käyttäjän luominen
Käyttäjätunnus luomiseen pääsee kirjautumis valikosta painamalla create user painiketta. Luominen onnistuu kirjoittamalla kenttiin tunnus ja salasana ja painamalla create.
### Tehtävien lisääminen
Kun uusi käyttäjä on luotu tai on kirjauduttu voidaan lisätä tehtäviä ja tehtävät tallentuvat listaan. Jokaisella käyttäjällä on oma lista tehtäviä.
