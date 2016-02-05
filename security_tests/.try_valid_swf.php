<?php
  header('Content-Type: '.$_SERVER['QUERY_STRING']);
  readfile('.sample.swf');
?>