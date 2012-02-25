Copyright (c) 2010 Ing. Hubert Hanghofer
Licensed under the GPL (see sources).
Binaries are available from <http://hanghofer.net/~hubert/python>
Sources are available from the repositories at

*   <https://github.com/brewbert/wxMol> and
*   <https://bitbucket.org/brewbert/wxmol>

What is wxMol?
==============

wxMol.py is a stoichiometric calculator. Under the hood it's a
simple wrapper for python's eval() function. It recognizes
element symbols and formula notation. Element symbols are replaced by
the corresponding atomic mass and the shortcuts of formula notation
(postfix and prefix factors, eg. CaSO4+2H2O) are expanded to give
mathematically correct syntax.

The converted input is presented along with the result, so that
you can check if the calculation was done according to your
expectations.

molcalc.py contains the parser function and acts as a shell version
of the program. wxMol.py is the graphical user interface, built
with the popular [wxPython Library](http://wxpython.org/).

Prerequisites
=============

*   [Python](http://python.org/) interpreter.
*   [wxPython](http://wxpython.org/) GUI library.

On Windows you may use the Windows Installers provided
at <http://hanghofer.net/~hubert/python> or in the Output directory
of the repositories. They install all dependencies.