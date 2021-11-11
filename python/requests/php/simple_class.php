<?php
include("classes/cafe.php");

header('Access-Control-Allow-Origin: *');
header('Content-type: application/json; charset=utf-8');

// $spf= new sphere(0);
// $spf->init(2);
// $spf->jsonOut();
$spfs = new cafes();
$spfs->init(0);
$spfs->jsonOut();
?>