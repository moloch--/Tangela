#!/bin/bash

# To run this test, download this .sh file, along with miniserver.c provided in
# this directory. Compile miniserver with 'make miniserver', then invoke it as
# follows:
#
# ./miniserver 1234 ./this_script.sh
#
# Then open this_script.html to carry out the test.
#

cat <<_EOF_
HTTP/1.0 200 OK
Content-Type: text/plain
Expires: Tue, 28 Dec 1999 10:00:00 GMT

var script_time = '`date +%s`:$$'
_EOF_

