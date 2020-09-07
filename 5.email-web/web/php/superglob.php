<html>

<head>      
<title>PHP: Variabili superglobali </title>
session_start();
</head>

 <body>

  <a href="http://netlab.fis.unipr.it/php/superglob.php"> home </a>
          
  <h1>$_SERVER</h1>
  <dl>
  <?php
  foreach($_SERVER as $key => $value)
  {
      echo "<dt>".$key."</dt>";
      echo "<dd>".$value."</dd>";
  }
  ?>
  </dl>

  <h1>$_GET</h1>
  <dl>
      <?php
      foreach($_GET as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>

  <h1>$_POST</h1>
  <dl>
      <?php
      foreach($_POST as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>


  <h1>$_COOKIE</h1>
  <dl>
      <?php
      foreach($_COOKIE as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>


  <h1>$_REQUEST</h1>
  <dl>
      <?php
      foreach($_REQUEST as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>
  <h1>$_ENV</h1>
  <dl>
      <?php
      foreach($_ENV as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>
  <h1>$_SESSION</h1>
  <dl>
      <?php
      foreach($_SESSION as $key => $value)
      {
          echo "<dt>".$key."</dt>";
          echo "<dd>".$value."</dd>";
      }
      ?>
  </dl>

 </body>

</html>

