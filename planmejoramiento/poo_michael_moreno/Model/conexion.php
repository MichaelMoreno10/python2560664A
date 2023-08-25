<?php
class Conexion {
    private static $servername = "localhost";
    private static $username = "root"; 
    private static $password = ""; 
    private static $dbname = "skiline";
    private static $conexion = null;

    public static function obtenerConexion() {
        if (self::$conexion === null) {
            self::$conexion = new mysqli(self::$servername, self::$username, self::$password, self::$dbname);
            if (self::$conexion->connect_error) {
                die("Conexión fallida: " . self::$conexion->connect_error);
            }
            
            echo "Conexión exitosa a la base de datos"; 
            
        }
        return self::$conexion;
    }
}

try {
    $conexion = Conexion::obtenerConexion();
    // Puedes continuar con tus operaciones en la base de datos aquí
} catch (Exception $e) {
    echo "Error en la conexión: " . $e->getMessage();
}
?>


