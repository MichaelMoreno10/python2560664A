<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/estilo.css">
    
    <title>Mostrar Habitaciones</title>
</head>
<body>
    <h1>Listado de Habitaciones</h1>
    
    <?php
    require_once '../Model/conexion.php';
    
    // Obtener habitaciones desde la base de datos
    $conexion = Conexion::obtenerConexion();
    $sql = "SELECT * FROM habitacion";
    $resultado = $conexion->query($sql);
    
    if ($resultado->num_rows > 0) {
        echo "<table>";
        echo "<tr><th>ID</th><th>Tipo</th><th>Estado</th><th>Precio</th><th>Acciones</th></tr>";
        while ($fila = $resultado->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $fila["id"] . "</td>";
            echo "<td>" . $fila["tipo"] . "</td>";
            echo "<td>" . $fila["estado"] . "</td>";
            echo "<td>" . $fila["precio"] . "</td>";
            echo '<td><a href="eliminar_habitacion.php?id=' . $fila["id"] . '">Eliminar</a></td>';
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No hay habitaciones registradas.";
    }
    ?>
    
</body>
</html>


