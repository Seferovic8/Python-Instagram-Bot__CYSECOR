# Python-Instagram-Script__CYSECOR
Python Instagram bot
#CYSECOR IZAZOV
Unaprijeđena skripta.



Commands Help file:
  -h, --help            show this help message and exit<br />
  -t TARGET, --target TARGET<br />
                        Username nad kojim zelimo izvrsiti skriptu<br />
  -u USER, --user USER  Instagram Username<br />
  -p PASSWORD, --pass PASSWORD<br />
                        Instagram Password<br />
  --files USERSFILE     Odaberi File za bazu<br />
  -l, --like            Like sve slike<br />
  -f, --follow          Odaberi za follow<br />
  
 # Target(-t)
   Instagram username korisnika nad kojem zelimo izvrsiti radnju npr:<br />
         python3 Main.py -t Cysecor
 # FOLLOW(-f), LIKE(-l)
 <pre>
 Odabrati opciju Follow(-f) ako želite da korisnika(target) automatski zaprati,<br />
     Ako je korisnik(target) već followan skripta ga neće un-followati<br />
 Odabrati opciju like(-l) ako želite da korisniku(target) automatski lajkujete slike
     Ako su neke slike već lajkovane program ih neće un-lajkati.
 </pre>
 # USER(-u) i PASSWORD(-p)
   Login na instagram pomoću ovih podataka primjer:
   python3 main.py -u your_instagram_username -p your_instagram_password -t Cysecor
 
  Automatizovan sistem za login. Izimanje username i passworda iz .txt baze usernameova i passworda.
  Automatski loginovanje pomoću podataka iz baze.
  
 
