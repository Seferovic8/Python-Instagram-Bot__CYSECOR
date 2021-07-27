# Python-Instagram-Script__CYSECOR
Python Instagram bot
# CYSECOR IZAZOV
Unaprijeđena skripta.


<pre>
### Help Commands:
  -h, --help            show this help message and exit<br />
  -t TARGET, --target TARGET<br />
                        Username nad kojim zelimo izvrsiti skriptu
  -u USER, --user USER  Instagram Username
  -p PASSWORD, --pass PASSWORD<br />
                        Instagram Password
  --files USERSFILE     Odaberi File za bazu
  -l, --like            Like sve slike
  -f, --follow          Odaberi za follow<br />
  </pre>
 ## Target(-t)
 <pre>
Instagram username korisnika nad kojem zelimo izvrsiti radnju npr:<br />
    python3 Main.py -t Cysecor
 </pre>
 ## FOLLOW(-f), LIKE(-l)
 <pre>
 Odabrati opciju Follow(-f) ako želite da korisnika(target) automatski zaprati,<br />
     Ako je korisnik(target) već followan skripta ga neće un-followati<br />
 Odabrati opciju like(-l) ako želite da korisniku(target) automatski lajkujete slike
     Ako su neke slike već lajkovane program ih neće un-lajkati.
 </pre>
 ## USER(-u) i PASSWORD(-p)
<pre>
Login na instagram pomoću ovih podataka primjer:
python3 main.py -u your_instagram_username -p your_instagram_password -t Cysecor
</pre>
Automatizovan sistem za login. Izimanje username i passworda iz .txt baze usernameova i passworda.
Automatski loginovanje pomoću podataka iz baze.
  
 
