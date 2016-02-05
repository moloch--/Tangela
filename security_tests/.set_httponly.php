<?php
  header('HTTP/1.0 '.$_SERVER['QUERY_STRING'].' Foo');
  header('Set-Cookie: HTTP_ONLY_COOKIE=1; httponly');
  header('Whatever: RESPONSE_VISIBILITY_TEST');
?>
