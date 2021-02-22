# FullyHomomorphicEncryption

The bottom line is that to be usable, information encrypted with traditional methods has to be visible in plain text at some point, if only for a brief moment. Another way to look at it is that a man-in-the-middle attack is always possible and as long as the attacker is creative when it comes to defining where the “middle” is!
Does it have to be that way? What if we could reliably manipulate encrypted information without ever decrypting it? Turns out that we can. Enter Fully Homomorphic Encryption (FHE). FHE is a class of ciphers that have the interesting quality that an arbitrary computation on ciphertexts generates an encrypted result which, when decrypted, matches what you would see had the same computations been performed on the plaintext. Sounds like black magic, doesn’t it? Theoretical FHE systems were postulated in the late 1970s. In the following decades, researchers implemented systems that permitted a limited number and limited types of computa- tions. Then in 2009, Craig Gentry described a system that could perform any computation, albeit very slowly. Basic computations would take hours! But it didn’t take long for Gentry and other researchers to come up with implementations many orders of magnitude faster. Those systems are finding practical uses today.

A Practical SaaS Example

One application for FHE is SaaS. Alice might have valuable data and Bob might have a valu- able algorithm. Neither wants to reveal their “secret sauce” to the other. With traditional encryp- tion methods, this would not be possible: The algorithm would have to operate on plaintext data, and Alice and Bob would have to duke it out regarding who should lift the skirt. Typical solutions
to the dilemma involve lawyers and NDAs.
Moments before he took his last breath, Alice’s grandfather gave her three top secret numbers
that will lead to the map coordinates of the spot where his treasure is hidden. To get the real coordinates, Alice must add two of the numbers and multiply the third by a constant. Alas, while cryptographically savvy, Alice is arithmetically challenged and has to enlist outside help.
Fortunately, Bob runs a service that can add and multiply encrypted numbers. Alice agrees to send Bob her FHE encrypted numbers. Bob will then perform the calculations on the two numbers without ever seeing them in plaintext. Calculations completed, Bob returns the encrypted results to Alice without ever seeing the plaintext results. When Alice gets the results, she can simply decrypt them to get the coordinates.
We are implementing this interaction in Python - see the listing for fullyhomo.py that follows this article. The code was written for Python 3, but should work fine with Python 2 as well. It will run on Ubuntu Linux using any one of the following three commands:
./fhc.py
python3 fhc.py
python fhc.py

SaaS Example:

Alice wants to use Bob’s calculation service to calculate 5 + 10 
She encrypts 5
...and the encrypted value is 408231311223330758911876050904... 
She then encrypts 10
...and the encypted value is 6811593647043826157618544194678...
Alice also wants to to multiply 6 with the constant 3
She encrypts 6
...and the encrypted value is 275872367736262799842862895600...
Then Alice sends the encrypted values to Bob along with her public key
Bob adds the two encrypted values without knowing what they are 
the encrypted result is 3509690235178988491246734744677382694... 
Bob multiplies the third encrypted value with the constant
the encrypted result is 8919545079897387397953169089569936011...
Bob sends the encrypted results back to Alice
Alice uses her private key to view the plain text results: 
Addition: 15
Multiplication: 18
Armed with the coordinates, Alice packs her shovel and books a trip to Niger. Or did he mean Mauritania? Or maybe Namibia? Surely the treasure isn’t in the middle of the Atlantic?!?! East versus West, North versus South, these things do matter!
The Code
The Python code implements an FHE algorithm called the Paillier cryptosystem. To keep things brief and simple, the code only implements the operations required to for the addition and multiplication operations. Also, the key pair is hard coded for the sake of simplicity. A full fledged implementation would provide code to generate random keys.
The class FullyHomoCipher on line 14 is the Paillier encryption code. The class BobsCalcula- tionService on line 54 defines the operations for addition and multiplication of Paillier-encrypted values.
Our treasure hunt adventure starts on line 75 and uses the two classes described above. It’s extensively commented in order to make it easy for the interested reader to modify and experiment.
 
A note of caution for readers that aren’t familiar with the Python language: 
Unlike most languages, Python is white-space sensitive, and indentation matters. It’s important to preserve the indentation or the program will not execute properly.

FHE Now and Tomorrow

Our SaaS example is obviously a toy, but that’s to be expected from about 140 lines of commented Python code. More robust, fully featured FHEs built around stronger algorithms are finding new applications every day.
Software as a Service is only one application that’s a good match for FHE. Other types of applications include smart contracts, block chain systems, data mining, “vanity” hashes, end- to-end encrypted database queries, anonymous identity systems, data integrity verification, and so on. With the rapid development in the field, we can expect many other uses in the very near future.
FHE is currently deployed across several industries and problem domains, including elec- tronic voting systems, genomics, and payment systems, and we predict widespread adoption in areas such as health care, smart power grids, and finance to take place very soon.
