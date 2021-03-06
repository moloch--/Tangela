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
Content-Disposition Bad: attachment; filename="field_name_truncated.txt"
Garbage-HTTP-Header: yes

[1] If this text is displayed in-line, NUL in field names does not result in truncation.
If HTTP garbage or error message appears, NUL stops header parsing (bad).
If file is saved as field_name_truncated.txt, NUL results in field name truncation.
_EOF_
