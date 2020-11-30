KastFucker


Kast.gg Account Creator

Create Accounts in bulk. 

Enjoy :) 


Not the prettiest solution but I did this with months of time between creating the accounts and writing the code to verify them. 

There is no need for any proxies (although if you modify the code to include it you can definitely speed the whole process along as they do have rate limiting)







Note:

Okay so I forgot how lazy I was when making this, email portion I wrote in C# so I'm including that solution as well.


The order of running the program:

KastFucker.py (checks usernames.txt for usernames you want to register)
KastVerifier.exe (build and run the c# email program)
KastVerifier.py

Make sure to edit the variables in the source to match your email username/password and update usernames.txt for your own sake



To make sure you have all the required python modules just do the usual: "pip install -r requirements.txt" in the directory