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
Content-Type: text/html

                                                                                                                                                                                                                                                                                                                                                
<html><font color=red>
If this page is displayed in black, first header takes precedence.
Otherwise, it's the last header.

_EOF_
