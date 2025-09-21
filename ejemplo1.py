import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QListWidget, QComboBox
)
from PyQt5.QtGui import QPalette, QColor

class GymMembershipApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Membresías - 180 Fitness")
        self.members = []
        self.total_income = 0.0
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        # Campos de entrada
        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()

        self.surname_label = QLabel("Apellido:")
        self.surname_input = QLineEdit()

        self.phone_label = QLabel("Teléfono:")
        self.phone_input = QLineEdit()

        self.plan_label = QLabel("Tipo de Membresía:")
        self.plan_combo = QComboBox()
        self.plan_combo.addItem("1 Semana - $15", 15)
        self.plan_combo.addItem("15 Días - $25", 25)
        self.plan_combo.addItem("1 Mes - $30", 30)

        # Botones
        self.add_button = QPushButton("Registrar Miembro")
        self.clear_button = QPushButton("Limpiar Registros")

        # Lista y total
        self.member_list = QListWidget()
        self.total_label = QLabel("Ingresos totales: $0.00")

        # Conexiones
        self.add_button.clicked.connect(self.add_member)
        self.clear_button.clicked.connect(self.clear_members)

        # Layouts
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.surname_label)
        input_layout.addWidget(self.surname_input)
        input_layout.addWidget(self.phone_label)
        input_layout.addWidget(self.phone_input)
        input_layout.addWidget(self.plan_label)
        input_layout.addWidget(self.plan_combo)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(QLabel("Miembros registrados:"))
        main_layout.addWidget(self.member_list)
        main_layout.addWidget(self.total_label)

        self.setLayout(main_layout)

    def apply_styles(self):
        # Fondo naranja
        self.setStyleSheet("""
            QWidget {
                background-color: #FFA500; /* naranja */
                font-family: Arial;
                font-size: 14px;
            }
            QPushButton {
                background-color: white;
                color: black;
                border: 1px solid #ccc;
                padding: 6px;
            }
            QLineEdit, QComboBox {
                background-color: #FFF8DC;
                border: 1px solid #ccc;
                padding: 4px;
            }
            QListWidget {
                background-color: #FFE4B5;
                border: 1px solid #ccc;
            }
        """)

    def add_member(self):
        name = self.name_input.text().strip()
        surname = self.surname_input.text().strip()
        phone = self.phone_input.text().strip()
        plan_text = self.plan_combo.currentText()
        plan_price = self.plan_combo.currentData()

        if not name or not surname or not phone:
            self.name_input.setPlaceholderText("Requerido")
            self.surname_input.setPlaceholderText("Requerido")
            self.phone_input.setPlaceholderText("Requerido")
            return

        self.members.append((name, surname, phone, plan_text, plan_price))
        self.total_income += plan_price

        self.member_list.addItem(f"{name} {surname} | {phone} | {plan_text}")
        self.total_label.setText(f"Ingresos totales: ${self.total_income:.2f}")

        # Limpiar campos
        self.name_input.clear()
        self.surname_input.clear()
        self.phone_input.clear()

    def clear_members(self):
        self.members.clear()
        self.total_income = 0.0
        self.member_list.clear()
        self.total_label.setText("Ingresos totales: $0.00")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GymMembershipApp()
    window.show()
    sys.exit(app.exec_())
