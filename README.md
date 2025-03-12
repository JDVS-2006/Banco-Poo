# Proyecto Banco POO

## Descripción

Este proyecto es una aplicación bancaria que permite a los usuarios realizar operaciones como depósitos, retiros y consultas de saldo. La aplicación está diseñada utilizando el patrón Modelo-Vista-Controlador (MVC) para facilitar el mantenimiento y si tener un codigo mas organizado.

## Estructura del Proyecto

- **Modelo (Model)**: 
  - Contiene la lógica de negocio y la estructura de datos. En este proyecto, el modelo es `BancoModel.py`, que define las clases y métodos para manejar las cuentas y transacciones.

- **Vista (View)**: 
  - Se encarga de la presentación de la información al usuario. En este caso, `BancoView.py` maneja la interfaz de usuario y muestra los resultados de las operaciones.

- **Controlador (Controller)**: 
  - Actúa como intermediario entre el modelo y la vista. `BancoController.py` recibe las entradas del usuario, interactúa con el modelo para procesar los datos y actualiza la vista con los resultados.

## Cómo Usar

1. Clona el repositorio:
   ```bash
   git clone <URL_del_repositorio> 
