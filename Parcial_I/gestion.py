from aparato import Aparato

class GestionConsumo:
    def __init__(self, costo_kwh):
        self.aparatos = []
        self.costo_kwh = costo_kwh

    def agregar_aparato(self, nombre, potencia_watts, horas_uso):
        aparato = Aparato(nombre, potencia_watts, horas_uso, self.costo_kwh)
        self.aparatos.append(aparato)

    def mostrar_aparatos(self):
        for aparato in self.aparatos:
            print(aparato)
            
    def resumen(self):
        total_consumo = sum(a.consumo_kwh() for a in self.aparatos)
        total_costo = sum(a.costo_mensual() for a in self.aparatos)
        print("\n--- Resumen ---")
        print(f"Consumo Total: {total_consumo:.2f} kWh")
        print(f"Gasto Mensual: ${total_costo:.2f}")