<?php
$link = mysqli_connect( $config["server"], $config["login"], $config["pass"], $config["db"]);  

if (!$link) { printf("Невозможно подключиться к базе данных. Код ошибки: %s\n", mysqli_connect_error());   exit; 
} 
if (!$link->set_charset("utf8")) {printf("Ошибка при загрузке набора символов utf8: %s\n", $link->error); exit();
} else {
// printf("Текущий набор символов: %s\n", $link->character_set_name());
}
?>