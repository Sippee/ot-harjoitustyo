# TeacherHelper  
Sovelluksessa voi luoda tunnuksen, kirjautua ja lisätä tehtäviä ja niiden vastauksia listaan. Eri ihmiset voivat käyttää myös sovellusta, koska tehtävät tallentuvat henkilökohtaisesti käyttäjätunnukseen sidottuna.

## Dokumentaatio  
[Käyttöohje](dokumentaatio/käyttöohje.md)  
[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)  
[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)  
[Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)  
[Testausdokumentti](dokumentaatio/testausdokumentti.md)  

## Asennus  
1. Asennetaan riippuvuudet "poetry install"  
2. Alustetaan tietokanta   "poetry run invoke build"  
3. Käynnistetään sovelllus "poetry run invoke start"

## Komennot  
### Ohjelman suoritus  
poetry run invoke start  

### Testaus  
poetry run invoke test  

### Testikattavuus  
poetry run invoke coverage-report  
