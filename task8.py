""" 
Paul's Plane Problem

A passenger has requested that they can book 3 seats together on a plane, and will only book if they can sit together.

You are to process seat reservations. The plane has N rows of seats, numbered from 1 to N. There are ten seats in each row (Labelled from A to K, with the letter I omitted), as shown in the below figure

 ABC DEFG HJK
Row 1 : XXX XXXX XXX
Row 2 : XXX XXXO XXX
... .. ... .... ...
Row 25: XOX XXXX XXX
Row 30: XXX XXXX XOX

Row N: XXX XXXX XXX

Some seats are already reserved. The list of reserved seats is given as a string S ( of length M) containing seat numbers, seperated by single spaces: for example, "1A 3C 2B 40G". The reserved seats can be listed in S in any order

Your task is to allocate for as many 3 person families as possible, but they must be together, and cannot be cross aisle. So for example G1 and H1 are not considered to be next to each other

Your task is to write a function that given the number of rows (N) and a list of reserved seats (string S), what is the maximum number of 3 person families that can be seated in the remaining unreserved seats

Example N = 2, and S = "1A 2F 1C"

Assumptions:
N is an integer (range of 1 to 50)
M is an integer (range of 0 to 1500)
S is a string, space seperated
No seat will appear in S more than once.

"""

