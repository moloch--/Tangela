<?php
  header('HTTP/1.0 ' . $_SERVER['QUERY_STRING'] . ' Foo');
  header('Content-Type: image/jpeg');
  readfile('.test_img.jpg');
?>