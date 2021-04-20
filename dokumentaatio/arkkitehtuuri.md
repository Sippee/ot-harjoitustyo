# Arkkitehtuurikuvaus

## Rakenne
Ohjelmalla on vasta kaksitasoinen kerrosarkkitehtuuri, sillä tulee olemaan kolmi.  
![Ohjelman nykyinen arkkitehtuuri](https://github.com/Sippee/ot-harjoitustyo/dokumentaatio/kuvat/arkkitehtuurikuva.png?raw=true)  
Repositories sisältää tietojen tallennuksesta vastaavan koodin, ja entities sisältää luokista vastaavan koodin.  
## Sovelluslogiikka
Sovelluksen nykyisen logiikan muodostaa vain luokka User, mutta tulee sisältämään luokan tehtävät.  
## Tiedon tallennus
Tiedon tallennusta varten meillä on repositorio hakemistossa UserData luokka, joka huolehtii käyttäjän tietojen tallentamisesta SQLite-tietokannan avulla.  
## Päätoiminnallisuudet
Tällä hetkellä vain käyttäjän luominen.  
