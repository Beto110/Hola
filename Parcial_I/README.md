# Proyecto: Control de Consumo Eléctrico

## Integrantes
- Nombre 1: Luis Angel Zuniga Menjivar
- Nombre 2: Alberto Jose Velasquez Paz

## Descripción
Este programa permite registrar aparatos eléctricos de un hogar, calcular automáticamente su consumo mensual y el costo en dólares, y generar un resumen final.

### Archivos
- `aparato.py`: Clase Aparato (almacena datos y cálculos).
- `gestion.py`: Clase GestionConsumo (gestiona la lista de aparatos y genera reportes).
- `main.py`: Clase principal que conecta todo y recibe datos del usuario.

---

## Preguntas

### 1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
Separar en módulos permite ordenar el código, facilita su mantenimiento, promueve la reutilización de clases y funciones, y hace el programa más escalable.

### 2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución?
Creamos dos clases:
- **Aparato**: Representa un aparato eléctrico con sus atributos (nombre, potencia, horas de uso) y métodos para calcular consumo y costo.
- **GestionConsumo**: Administra los aparatos, permite agregarlos y genera reportes ordenados y resumen.

Esto permite trabajar con objetos independientes, más fáciles de manipular y extender.

### 3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto.
GitHub permitió que cada integrante trabajara en archivos diferentes sin sobrescribir el trabajo del otro.  
Por ejemplo: un integrante programó la clase `Aparato` mientras el otro trabajaba en `GestionConsumo`, y luego unificamos los cambios usando pull requests y commits documentados.
