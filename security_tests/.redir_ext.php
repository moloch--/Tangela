<?php
  header('HTTP/1.0 302 Foo');
  header('Location: http://www.example.com/');
  header('Whatever: RESPONSE_VISIBILITY_TEST');
?>
