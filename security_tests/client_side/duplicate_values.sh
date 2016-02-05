#!/bin/bash

# To run this test, download this .sh file, along with miniserver.c provided in
# this directory. Compile miniserver with 'make miniserver', then invoke it as
# follows:
#
# ./miniserver 1234 ./this_script.sh
#
# Navigate to http://<your_current_ip>:1234/ to carry out the test.
#

cat <<_EOF_
HTTP/1.0 200 OK
Content-Type: text/plain
Content-Disposition: attachment; filename="first_precedence.txt"; filename="last_precedence.txt"

Depending on the filename, first or last occurence of a parameter value matters the most.

_EOF_
