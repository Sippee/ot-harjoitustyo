# Vaatimusmäärittely

## Sovelluksen tarkoitus
Käyttäjä voi tallentaa tehtäviä ja niiden tehtävien vastauksia tulevaisuutta varten muistiin.

## Käyttäjät

Sovelluksella on vain yksi normaali käyttäjä rooli.

## Käyttöliittymä

Kirjautumisnäkymä aukeaa ensimmäisenä. 
Kirjautumisnäkymästä voi mennä rekisteröitymisnäkymään luomaan tunnuksen.
Kirjautumisen tai uuden käyttäjän luomisen jälkeen pääsee tehtävä näkymään, ja käyttäjä voi aloittaa lisäämään tehtäviä

## Perusversion tarjoama toiminnallisuus

### Tunnuksen luominen ja kirjautuminen

+ Käyttäjä voi luoda tunnuksen sovellukselle
  + Tunnus luodaan menemällä create-sivulle ja kirjoittamalla uusi tunnus ja salasana sinne.
  + Tunnuksia voi luoda useita kappaleita, kunhan ne ovat eri nimisiä, muuten yrityksestä tulee virhe
+ Käyttäjä voi kirjautua sovellukseen
  + Kirjautuminen onnistuu ensimmäisellä sivulla kirjoittamalla käyttäjätunnus, salasana ja painamalla Login-painikeeta
  + Jos tunnusta ei ole olemassa tai salasana on väärin tulee virheilmoitus.

### Kirjautumisen jälkeen

+ Käyttäjä pystyy aloittaa luomaan tehtäviä
+ Luodut tehtävät ilmestyvät sovelluksen alaosaan, ja jos tehtäviä on jo luotu niin ne ilmestyvät päästäessään sille sivulle
+ Jokainen tehtävä on uniikki sille käyttäjätunnukselle, jolla se on tehty
+ Käyttäjä voi kirjautua ulos 

## Jatkokehitysideoita

+ Tehdä tehtäviä
+ Saada pisteitä tehtävistä
+ Merkitä tehtäviä tekemättömiksi
