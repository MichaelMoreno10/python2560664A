<?php
class Habitacion {
    private $id;
    private $tipo;
    private $estado;
    private $precio;

    public function __construct($id, $tipo, $estado, $precio) {
        $this->id = $id;
        $this->tipo = $tipo;
        $this->estado = $estado;
        $this->precio = $precio;
    }

    public function getid() {
        return $this->id;
    }

    public function gettipo() {
        return $this->tipo;
    }

    public function getestado() {
        return $this->estado;
    }

    public function getprecio() {
        return $this->precio;
    }
}
?>
