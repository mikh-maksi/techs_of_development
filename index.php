<?php
$a = $_GET['a'];
$b = $_GET['b'];
$act = $_GET['act'];

if ($act ==1){
    $c = $a + $b;
}
echo "Result is $c";
?>
<br><br><br>
<?php

include "config.php";
include "connect.php";

echo "<table class = 'table  table-striped table-bordered table-hover table-sm'>";


$sql = "SELECT name FROM indexesSpheres";
$nn = 1;
if ($res = mysqli_query($link, $sql)    ) { } else {echo "Error: " . $sql . "<br>" . $link->error;}
while( $row = mysqli_fetch_row($res) ){
    foreach($row as $key =>$value)
    if ($nn<=14)  echo "<tr><td>".$value."</td></td>";
    $nn++;
}


echo "</table>";
