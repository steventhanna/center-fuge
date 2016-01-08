# center-fuge

## Why
I needed a safe and secure way to protect my deployent keys within my opensource projets on GitHub.  Thus, center-fuge was born.

## How
center-fuge acts as a centralized system that keeps the deployment keys inside the repo, yet they cannot be accessed without proper authorization.  How?  Well first, all of the deployment keys are encrypted using a custom hash generated by center-fuge.  This hash is shared amongst other members of your team.  

Whats awesome about this method is that if the deployment keys are updated with newer versions, the rest of the team does not have to manually change all of the keys, since they are all saved on GitHub.  Instead, the keys are just decrypted upon a users request per usual.

This safeguards keys from unauthorized users and pesky bots in search of a means to siphon resources for free.

