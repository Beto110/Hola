class Aparato:
    def __init__(self, nombre, potencia_watts, horas_uso, costo_kwh):
        """
        nombre: Nombre del aparato
        potencia_watts: Potencia del aparato en Watts
        horas_uso: Horas de uso al mes
        costo_kwh: Precio del kWh en dólares
        """
        self.nombre = nombre
        self.potencia_watts = potencia_watts
        self.horas_uso = horas_uso
        self.costo_kwh = costo_kwh

    def consumo_kwh(self):
        """Calcula el consumo mensual en kWh"""
        return (self.potencia_watts * self.horas_uso) / 1000

    def costo_mensual(self):
        """Calcula el costo mensual del aparato"""
        return self.consumo_kwh() * self.costo_kwh

    def __str__(self):
        return (f"Aparato: {self.nombre} | Potencia: {self.potencia_watts} W | "
                f"Horas: {self.horas_uso} h | Consumo: {self.consumo_kwh():.2f} kWh | "
                f"Costo: ${self.costo_mensual():.2f}")
