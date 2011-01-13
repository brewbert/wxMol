#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010 Hubert Hanghofer
# hubert.hanghofer.net
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import string

Elements = dict(
H=1.00794,
D=2.014102, 
He=4.002602,
Li=6.941,
Be=9.012182,
B=10.811,
C=12.0107,
N=14.00674,
O=15.9994,
F=18.9984032,
Ne=20.1797,
Na=22.989770,
Mg=24.3050,
Al=26.981538,
Si=28.0855,
P=30.973761,
S=32.066,
Cl=35.4527,
Ar=39.948,
K=39.0983,
Ca=40.078,
Sc=44.955910,
Ti=47.867,
V=50.9415,
Cr=51.9961,
Mn=54.938049,
Fe=55.845,
Co=58.933200,
Ni=58.6934,
Cu=63.546,
Zn=65.39,
Ga=69.723,
Ge=72.61,
As=74.92160,
Se=78.96,
Br=79.904,
Kr=83.80,
Rb=85.4678,
Sr=87.62,
Y=88.90585,
Zr=91.224,
Nb=92.90638,
Mo=95.94,
Tc=98.0,
Ru=101.07,
Rh=102.90550,
Pd=106.42,
Ag=107.8682,
Cd=112.411,
In=114.818,
Sn=118.710,
Sb=121.760,
Te=127.60,
I=126.90447,
Xe=131.29,
Cs=132.90545,
Ba=137.327,
La=138.9055,
Ce=140.116,
Pr=140.90765,
Nd=144.24,
Pm=145.0,
Sm=150.36,
Eu=151.964,
Gd=157.25,
Tb=158.92534,
Dy=162.50,
Ho=164.93032,
Er=167.26,
Tm=168.93421,
Yb=173.04,
Lu=174.967,
Hf=178.49,
Ta=180.9479,
W=183.84,
Re=186.207,
Os=190.23,
Ir=192.217,
Pt=195.078,
Au=196.96655,
Hg=200.59,
Tl=204.3833,
Pb=207.2,
Bi=208.98038,
Po=209.0,
At=210.0,
Rn=222.0,
Fr=223.0,
Ra=226.0,
Ac=227.0,
Th=232.0381,
Pa=231.03588,
U=238.0289,
Np=237.0,
Pu=244.0,
Am=243.0,
Cm=247.0,
Bk=247.0,
Cf=251.0,
Es=252.0,
Fm=257.0,
Md=258.0,
No=259.0,
Lr=262.0,
Rf=261.0,
Db=262.0,
Sg=266.0,
Bh=264.0,
Hs=269.0,
Mt=268.0,
Uun=271.0,
Uuu= 272.0)

k = Elements.keys()


def get_element(symbol):
    """
get_element(str) -> string
Checks if symbol is in IUPAC list and returns
atomic weight in string format, raises NameError otherwise. 
    """
    if symbol in k: return str(Elements[symbol])
    else:
        raise NameError("Element <" + symbol + "> not found "
                        "in IUPAC list!")


def parse_formula(s):
    """
parse_formula(str) -> string
compiles string for eval function, replacing symbols with atomic weight
and inserting operators and paranthesis appropriately.
    """
    d = ''  # temporary buffer for storing digits
    el = '' # temporary buffer for storing element symbols
    f = False # are we scanning a chemical formula?
    r = ''  # buffer for results string

    for i in s:
        # We do a single scan. Compilation is controlled by the
        # state of 3 parameters:
        # d: contents of the digit buffer
        # el: contents of the buffer for element symbols
        # f: if we are currently scanning a chemical formula
        if i in (string.digits + ".,"):
            # if a digit follows an element or ) it's a factor
            if el:      r, el = r + get_element(el) + '*', ''
            elif r and r[-1] == ')':    r += '*'
            elif f and not d:           r, f = r + ')', False
            if i == ',':                d += '.'
            else:                       d += i
        elif i in string.uppercase:
            # This marks the start of a new element symbol
            if el:      r += get_element(el) + '+'
            elif d:
                # if we are scanning a formula, add this to buffers
                if f:   r, d = r + d + '+', ''
                # but gracefully handle prefix factors
                else:   r, d = r + d + '*', ''
            # if this is the start of a new formula, add (
            if not f:   r, f = r + '(', True
            el = i
        elif i in string.lowercase:
            if d or not el:
                raise NameError("Element symbols start capitalized: "
                                + r + i + "<<<")
            el += i
        # PARENTHESIS: besides arithmetic grouping must also work for
        # molecules - consider Al2(SO4)3+18*H2O and 5*(6+7) / (2*(3+4))
        # remember that only postfix factors can be implemented
        # so if a ( follows a digit, the follwoing (term) must be added
        elif i == '(':
            if d:       r, d = r + d + '+', ''
            elif el:    r, el = r + get_element(el) + '+', ''
            r += i
        elif i == ')':
            if d:       r, d = r + d, ''
            elif el:	r, el = r + get_element(el), ''
            r += i
        elif i in string.punctuation:
            if d:       # make sure we use floating point arithmetic
                if f:   r, d = r + d, ''
                else:   r, d = r + str(float(d)), ''
            elif el:    r, el = r + get_element(el), ''
            if f:       r, f = r + ')', False
            r += i

    if d:       r += d
    elif el:    r += get_element(el)
    if f:       r += ')'
    return r

if __name__ == "__main__":
    import sys, locale
    done = False
    while not done:
        if len(sys.argv) > 1:
            s = str(sys.argv[1])
            done = True
        else:
            try:
                s = str(raw_input("Formula: "))
            except (EOFError, KeyboardInterrupt):
                break
            else:
                if not s: continue
        locale.setlocale(locale.LC_ALL, '')
        dp = locale.localeconv()["decimal_point"]
        try:
            p = parse_formula(s)
            r = str(eval(p))
            if dp != '.':
                t = r.partition('.')
                r = t[0] + dp + t[2]
            print p, "\n\t", r
        except (NameError, SyntaxError, UnicodeEncodeError,
                ZeroDivisionError), detail:
            print "Error:", detail
