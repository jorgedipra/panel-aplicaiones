# Tablero de Accesos Directos

Esta aplicación de escritorio, desarrollada en Python, crea un tablero flotante con accesos directos a diversas aplicaciones. Utiliza la biblioteca PyQt5 para la interfaz gráfica y permite ejecutar comandos específicos o abrir URLs al hacer clic en los botones correspondientes.

![image](https://github.com/user-attachments/assets/49095593-719e-42af-a341-6b934502218a)


## Características

- **Interfaz gráfica**: Diseñada con PyQt5, con un diseño atractivo y personalizable.
- **Accesos directos**: Configurable con múltiples accesos directos a aplicaciones y scripts.
- **Iconos personalizados**: Descarga y utiliza iconos personalizados para cada acceso directo.
- **Siempre al frente**: Opción para mantener la ventana siempre visible sobre otras aplicaciones.
- **Gestión de comandos**: Soporte para ejecutar tanto aplicaciones locales como URLs.

## Uso

1. **Agregar accesos directos**: Los accesos directos a las aplicaciones se definen en una lista de tuplas con el nombre, comando y URL del icono.
2. **Ejecutar la aplicación**: Simplemente ejecuta el script principal y la ventana del tablero flotante se abrirá.
3. **Interacción**: Haz clic en los botones para lanzar las aplicaciones o scripts especificados. Usa el checkbox para alternar la ventana entre siempre al frente o no.

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableroFlotante()
    window.show()
    sys.exit(app.exec_())
```
