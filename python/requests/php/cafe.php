<?php
class cafe{
  var $ID;
  var $Name;
  var $Price;
  var $Location;
  var $Cuisine;
  var $Hookah;

  function init($id){
      include "config.php";
      include "connect.php";
      if(!isset($id)) $id = 0;

      if ($id == 0){
          $sql = 'SELECT MAX(id) as ID FROM 2go_cafes';   
          if ($result = $link->query($sql)) {
              while($row = $result->fetch_array() ){$id = $row['id'];}                
        }
      }

      $sql = 'SELECT * FROM 2go_cafes WHERE ID = '.$id;   
        if ($result = $link->query($sql)) {
          while($row = $result->fetch_array() ){
            $this->ID=$row["ID"];
            $this->Name=$row["Name"];
            $this->Price=$row["Price"];
            $this->Location=$row["Location"];
            $this->Cuisine=$row["Cuisine"];            
            $this->Hookah=$row["Hookah"];
            }}
  }

  function jsonOut(){
      echo json_encode($this);
  }
}

class cafes{
  var $cafes;
  function init($id){
      include "config.php";
      include "connect.php";

      if(!isset($id)) $id = 0;

      $d = array();
      $sql1 = 'SELECT * FROM 2go_cafes';   
        if ($result = $link->query($sql1)) {
          while($row = $result->fetch_array() ){
              $d1 = new cafe;
              $d1->init($row['ID']);
              $d[] = $d1;
            }}

      $this->cafes = $d;
  }
  function jsonOut(){
      echo json_encode($this);
  }



}
?>