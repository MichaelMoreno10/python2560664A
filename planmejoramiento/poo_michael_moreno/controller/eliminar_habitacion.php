<?php
require_once '../Model/conexion.php';

if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["id"])) {
    $id = $_GET["id"];

    $conexion = Conexion::obtenerConexion();
    $stmt = $conexion->prepare("DELETE FROM habitacion WHERE id = ?");
    $stmt->bind_param("s", $id);
    $resultado = $stmt->execute();
    $stmt->close();

    if ($resultado) {
        header("Location: mostrar_habitaciones.php"); // Redirigir después de eliminar
    } else {
        echo "Error al eliminar la habitacion: " . $conexion->error;
    }
}
?>



