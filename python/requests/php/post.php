<?php

# Получить JSON как строку
    $json_str = file_get_contents('php://input');

# Получить объект
    $json_obj = json_decode($json_str);

    $fp = fopen('results.csv', 'w');
    $other = $_POST['some_data'];
    $name = $json_obj->some_data;

    $mytext .= "$name;$other;\r\n"; // Исходная строка
    $test = fwrite($fp, $mytext); // Запись в файл
    if ($test) echo 'Данные в файл успешно занесены.';
    else echo 'Ошибка при записи в файл.';
    fclose($fp); //Закрытие файла

    //Заголовки

    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Credentials: true');
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
    header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");
    header('Content-type: application/json; charset=utf-8');
    

//    echo(json_encode($json_obj));

 ?>