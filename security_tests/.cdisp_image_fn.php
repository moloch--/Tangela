<?php
  header('Content-Type: image/jpeg');
  header('Content-Disposition: attachment; filename="' . urldecode($_SERVER["QUERY_STRING"]) . '"');
?>
Test.
