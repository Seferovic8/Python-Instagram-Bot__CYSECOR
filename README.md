# Python-Instagram-Script__CYSECOR
Python Instagram bot
# CYSECOR IZAZOV
Unaprijeđena skripta.


<pre>
######  Help Commands:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Username nad kojim zelimo izvrsiti skriptu
  -u USER, --user USER  Instagram Username
  -p PASSWORD, --pass PASSWORD
                        Instagram Password
  --files USERSFILE     Odaberi File za bazu
  -l, --like            Like sve slike
  -f, --follow          Odaberi za follow
  </pre>
 ## Target(-t)
 <pre>
Instagram username korisnika nad kojem zelimo izvrsiti radnju npr:
    python3 Main.py -t Cysecor
 </pre>
 ## FOLLOW(-f), LIKE(-l)
 <pre>
 Odabrati opciju Follow(-f) ako želite da korisnika(target) automatski zaprati,
     Ako je korisnik(target) već followan skripta ga neće un-followati
 Odabrati opciju like(-l) ako želite da korisniku(target) automatski lajkujete slike
     Ako su neke slike već lajkovane program ih neće un-lajkati.
 </pre>
 ## USER(-u) i PASSWORD(-p)
<pre>
Login na instagram pomoću ovih podataka primjer:
    python3 main.py -u your_instagram_username -p your_instagram_password -t Cysecor -f -l   (S ovom komandom ćete se loginovati na instagram pomoću username i passworda i automatski zapratiti korisnika(targeta) u ovom slučaju Cysecora i lajkati mu slike)
    
</pre>
Automatizovan sistem za login. Izimanje username i passworda iz .txt baze usernameova i passworda.
Automatski loginovanje pomoću podataka iz baze.
  
 
