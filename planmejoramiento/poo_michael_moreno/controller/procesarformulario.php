
<?php
require_once '../Model/conexion.php';
require_once '../Model/modelos.php';

class HabitacionController {
    public function insertarHabitacion($id, $tipo, $estado, $precio) {
        $conexion = Conexion::obtenerConexion();

        $stmt = $conexion->prepare("INSERT INTO habitacion (id, tipo, estado, precio) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("sssd", $id, $tipo, $estado, $precio);
        $resultado = $stmt->execute();
        $stmt->close();
        return $resultado;
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST["id"];
    $tipo = $_POST["tipo"];
    $estado = $_POST["estado"];
    $precio = $_POST["precio"];

    // Verificar si los datos son válidos antes de insertar
    if (!empty($id) && !empty($tipo) && !empty($estado) && is_numeric($precio)) {
        $habitacionController = new HabitacionController();
        $resultado = $habitacionController->insertarHabitacion($id, $tipo, $estado, $precio);

        if ($resultado) {
            echo "Habitacion registrada correctamente.";
        } else {
            echo "Error al registrar la habitacion: " . $stmt->error;
        }
    } else {
        echo "Por favor, complete todos los campos correctamente.";
    }
}
?>


