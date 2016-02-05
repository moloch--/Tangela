<?php
  header('HTTP/1.0 302 Redirect');
  header('Location: ' .urldecode($_SERVER["QUERY_STRING"]));
?>
<!-- REDIRBODY -->
No redirection.