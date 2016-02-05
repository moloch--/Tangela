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
Content-Length: 110
Content-Type: text/html

[1] If only this part of the document is shown, non-zero Content-Length takes precedence on non-error pages.
              
<p>
If this part is shown as well, actual content length takes precedence over HTTP headers on non-error pages.
_EOF_
