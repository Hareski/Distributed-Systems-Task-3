# Distributed Systems - Task 3: Push vs Pull system architectures
For our implementation of a push architecture we used the Python PyFCM framework available at https://github.com/olucurious/PyFCM and the Firebase messaging repository https://github.com/firebase/quickstart-js/tree/master/messaging.
## Getting Started
### Client
To start the client please follow next commands on the client directory.

```
sudo npm -g install firebase-tools
firebase login
firebase use --add
firebase serve -p 8081
```
### Server
Server need python 2.7. To start the server please follow next commands on the server directory.

```
chmod +x ./script.py
./script.py
```
