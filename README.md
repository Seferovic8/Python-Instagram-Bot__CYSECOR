# Python-Instagram-Script__CYSECOR
Python Instagram bot
# CYSECOR IZAZOV
Unaprijeđena skripta.

###### Help Commands:
<pre>

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
    python3 main.py -u your_instagram_username -p your_instagram_password -t Cysecor -f -l   
    (S ovom komandom ćete se loginovati na instagram pomoću username i passworda i automatski zapratiti korisnika(targeta) u ovom slučaju Cysecora i lajkati mu slike)
    
</pre>
## --files:
<pre>
  Automatizovan sistem za login. Uzimanje username i passworda iz .txt baze usernameova i passworda.
  Automatski loginovanje pomoću podataka iz baze.
  Primjer file je users.txt
  
  python3 main.py --files users.txt -t Cysecor -f -l
</pre>
## Kako postaviti users.txt file:
    <pre>
    Prvo trebate napisati instagram username pa onda zarezom(,) odvojiti i napisati password, nakon toga odvojiti točkom-zarezom(;) i 
    upisati novi account po istom principu:
    
      
          your1_instagram_username, your1_instagram_password;
          your2_instagram_username, your2_instagram_password;
          your3_instagram_username, your3_instagram_password;
     
   
    
    </pre>
# SET SCRIPT
<pre>
  U 32. liniji koda morate unesti odgovarajući put(path) do firefoxa.
  U 33. liniji koda morate unesti odgovarajući put(path) do geckoriver-a
  </pre>
