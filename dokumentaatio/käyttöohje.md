# Käyttöohje

## Konfigurointi
Tallennuksesta vastaavat UserRepository ja ExerciseRepository luokkien alaosassa oleva kutsu. Tämä tapa on erittäin huono, parannettavaa olisi.

## Ohjelman käynnistys
Käynnistys onnistuu ensin asentamalla riippuvuudet "poetry install"  
Sitten alustamalla database komennolla "poetry run invoke build"
Viimeiseksi voidaan käynnistää sovellus komennolla "poetry run invoke start"

## Kirjautuminen
Sovelluksen ensimmäinen sivu on kirjautumissivu.
Kirjoittamalla kenttiin tunnus, salasana ja painamalla login päästään eteenpäin.

## Käyttäjän luominen
Kirjautumis sivulta päästään uuden käyttäjän luomis näkymään painamalla create user painiketta.
Uuden käyttäjän luominen toimii samalla tavalla kuin kirjautuminen, mutta painetaan create painiketta.

## Tehtävälista
Käyttäjän luomisen tai kirjautumisen jälkeen pääsee tehtävälista näkymään, ja tehtäviä ja niiden vastauksia voi lisätä listaan.
Tehtävälista sivulta päästään takaisin kirjautumis sivulle painamalla logout painiketta.
