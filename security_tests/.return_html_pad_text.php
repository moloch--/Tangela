<?php
  header('Content-Type: text/plain');
  echo str_pad('X',$_SERVER["QUERY_STRING"]);
?><html>
<title>foo</title>
<body>
<!-- If this text is shown, document not treated as HTML. Please decrease the number
shown in the URL until HTML starts getting detected. -->





If only this text is shown, HTML detected. Please increase the number shown in the URL
until HTML stops getting detected.