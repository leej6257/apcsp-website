<!DOCTYPE html>
<html>
  <head>
    <title>Magic 8 Ball</title>
  </head>


  <body>

    <h1>Magic 8 Ball</h1>
    <p>Ask a yes or no question.</p>

    <?php
       // define variables and set to empty values
       $arg1 = $output = $retc = "";
       if ($_SERVER["REQUEST_METHOD"] == "POST") {
         $arg1 = test_input($_POST["arg1"]);
         exec("/usr/lib/cgi-bin/sp1b/Magic8Ball \"" . $arg1 . "\"", $output, $retc); 
       }
       function test_input($data) {
         $data = trim($data);
         $data = stripslashes($data);
         $data = htmlspecialchars($data);
         return $data;
       }
    ?>

    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>$
      Arg1: <input type="text" name="arg1"><br>
      <br>
      <input type="submit" value="ASK!">
    </form>
    <?php
       // only display if return code is numeric - i.e. exec has been called
       if (is_numeric($retc)) {
         echo "<h2>Your Input:</h2>";
         echo $arg1;
         echo "<br>";
       
         echo "<h2>Program Output (an array):</h2>";
         foreach ($output as $line) {
           echo $line;
           echo "<br>";
         }
       
         echo "<h2>Program Return Code:</h2>";
         echo $retc;
       }
    ?>
  
  </body>
</html>
