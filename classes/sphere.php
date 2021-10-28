<?php
class sphere{
  var $id;
  var $name;


  function init($id){
      include "config.php";
      include "connect.php";
      if(!isset($id)) $id = 0;

      if ($id == 0){
          $sql = 'SELECT MAX(id) as id FROM indexesSpheres';   
          if ($result = $link->query($sql)) {
              while($row = $result->fetch_array() ){$id = $row['id'];}                
        }
      }

      $sql = 'SELECT * FROM indexesSpheres WHERE id = '.$id;   
        if ($result = $link->query($sql)) {
          while($row = $result->fetch_array() ){
            $this->id=$row["id"];
            $this->name=$row["name2"];
            }}
  }

  function jsonOut(){
      echo json_encode($this);
  }
}

class spheres{
  var $spheres;
  function init($id){
      include "config.php";
      include "connect.php";

      if(!isset($id)) $id = 0;

      $d = array();
      $sql1 = 'SELECT * FROM indexesSpheres';   
        if ($result = $link->query($sql1)) {
          while($row = $result->fetch_array() ){
              $d1 = new sphere;
              $d1->init($row['id']);
              $d[] = $d1;
            }}

      $this->spheres = $d;
  }
  function jsonOut(){
      echo json_encode($this);
  }



}
?>
