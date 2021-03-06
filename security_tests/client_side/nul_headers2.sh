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
Content-type: text/plain
Content-Disposition: attachment; filename="file name.txt"

If the proposed filename for this file is 'file', NUL character results in filename truncation.
If 'file?name.txt' or something along these lines is proposed, no truncation took place.
_EOF_
