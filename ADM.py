#!/usr/bin/env python
from urllib2 import Request, urlopen, URLError, HTTPError
def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
def banner():
        print """                                                                                                                                                      
                                                               ``.::/:.:++: -+/::--.`                                                                 
                                                        ``  `/+o..:yy-``s+` `.os+//+o/`                                                               
                                                     .:+o+o. `./`  sy+  s.    +o    .s/  -+/-.`                                                                     
                                  `-/ss+-` /s.   /` s-s.`s     s:`   -s/  `-:oo+:.`                                                    
                                                :sys.` .-  -.   -+`+`++:o    .so+++oo:     -o+:++:                                                    
                                            `.- --:o:  .s:       //+-.so/    /+``./s-     -o:   ```:.                                                 
                                          `/sy+    `/+.+ys:  -.   os/ oy+    o.   `s-    :o.      `oo+-                                               
                                          :s//s+.    -ss-./- :s`  .y+ :y:   -o````//    /+`      ./:.-++-                                             
                                       .::..` `:+/`   .o:    `s/   //``/.``:+o++//- ` `/+`     ./:`   `:+/`                                           
                                      -yhhhyo+:.`-+:`  `/+.:osy++ssyyo/:/:/syoso/-.:++o+`    ./+/+--/.  .+/                                           
                                      `::-/so/:://::/-`  oyyyhdmmdhNmho:hdmNhodmmmhhos+o/ ``:/. .o/-` `:/:`                                           
                                            ./+/``.:/so-.smNNmhyyydhmNds+omNhommhyyhhyo+.-+o-   :.    `.`                                             
                                               .:/:`..:ymNmds+:--:/+shyyyoymyysssyddyo+so/-/o:``.::                                                   
                                                  .syshmds/:/++++/////+osydysshddyyhNNms/ss:+++/:.                                                    
                                                   :ymdo-:+o/+syhhhysshdmhs++//sdmmysmMNdsoys:                                                        
                                                  `hNh+//+s//so/:::::/osmNNmmmdy+yNNdyNMMNdoyo                                                        
                                                  yNhshddy+:y/-+ssyyddddNNNNNNNmmsdNNhhNNNNmsm/                                                       
                                                 /NdhmNNmh:h+:sdddmmmmdhNNNNNNNNNhhNNmyddhdNdyd`                                                      
                                                 dmdNNNNms+o-sdhhmmmdy++NNNNmNNNNhyNNNdssyhyNhy+                                                      
                                                .myhmNNNdso:+hy+yoodyhh+dmhshhNNNysdNNdsssdmhNhs                                                      
                                                :ddddmNNhos:yhdd+ymNmhyddysdNmdNNyhymNmssydmmhy+                                                      
                                                -NdydmdmmdmohmmmshmmmNhhhhNmmmdhmyhhdNmdmmmmmddd                                                      
                                                `NmyddhhNmmdhddhs/ymmmd/+sdmNy:omhyyhNmNNNmddddy                                                      
                                               `:yydhyhydNyyss+/+somdysoooshdy:yddhhhdmmmmmmhhd/...`    `                                             
                                   :/-.-:://--..:syhdmyyyhdhyshdmmsymyddhdydy/oyyhsyyhdhddmmmho-+-.```/:--::.                                         
                                   -s/.` `+s:--  /shmdyhhddhdmmNNNysyy+syooh+hshms:-..:++yyyhy..+-` .+:    .+-..                                      
                                    +o` `--`` .::-.oyhhmmmmmmmmdmdohydhyyhdsy+odmmdhdddhdyhhy-  `.-:-.     `+:-+.                                     
                                   :/o/.-:-      `:+:+sodNmNm+--+yo+dhddddhhs/ymdmmNNNNNdhso//:---`   `---/+:`-`                                      
                                   /+:--.`      -/..:osdmmmh:-+ydmhs+hhyhyys/yhs:omNNNNmNm+:+:`  .+-`   `...`                                         
                                    ``.+:..---:++/-...-/ydsohmmmmmmmyysyhsyssmms.`/mNNmms- ..--. :+:-:::-++`                                          
                                       :s+-.-o/``     -++/ohmmmmmmNNd+osodmmmmds.--+yy+-//--.  .:+/`  ``.-.                                           
                                        `.-:o:      -:.``o.`/yhdNNd/o.---hmdh+:++...`./+:```-`   `-:-`.-`                                             
                                         .os/     -++`  .+``/o+:.:-/``.`:yyo-`./::/-:..:. `:.   `   ./+/`                                             
                                          `//`  -/:-/+/::. -+.`    .://.`.++++`+../`./. .:./+:` -/-  ::`                                              
                                            `+++:`   ```..-o:.    -+-.-+``.-+` -. -:```  `//``-  `+:`-                                                
                                             `-+-       /o+::.   .+.   :-   +`  .  ::      ::` `-/+:/-                                                
                                               `        :+.      /:    -/   /.      /:      -/:/:.`-.`                                                
                                                     ://o-    /.`o`    -/   ::      `/-``   ./:`                                                      
                                                     .:/++/-.:+`.o.    ::   .+`     `:+/:.                                                            
                                                        `.:://. `++-``-/`   .o-.-`  -/--.                                                             
                                                                 `/+///`  ://o+//`     /+.                                                            
                                                                   ```    ```://:      `/.                                                            
                                                                             `.`        `                                  """
def miminEA():
        r = open("pan.txt","r");
        print("WEBSITE TARGET  \n(contoh : xnxx.com or www.xnxx.com ) ")
        link = raw_input("Rieef@GNS : ")
        print "\033[92m \n\nlink admin : \n"
        while True:
                sub_link = r.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "Nich =  ",req_link

banner()
miminEA()
