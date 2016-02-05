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
HTTP/1.1 200 OK
Content-Type: text/plain
Cache-Control: private, max-age=wharrgarbl

var script_time = '`date +%s`:$$'
_EOF_

