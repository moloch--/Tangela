<?php
  header('Content-Type: ' . urldecode($_SERVER["QUERY_STRING"]));
?>
<html>
<title>foo</title>
<body>
<!-- If this text is shown, document not treated as HTML -->

If only this text is shown, HTML detected