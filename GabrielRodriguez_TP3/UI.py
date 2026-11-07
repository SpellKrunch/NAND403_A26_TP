
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QTextEdit
)

class RandomAnimator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setFixedWidth(280)
        self.build_ui()
    
    def build_ui(self):
        main_layout = QVBoxLayout(self)

        animation_timing_title = QLabel("Animation Timing")
        animation_timing_layout = QHBoxLayout(self)

        translate_parameters_title = QLabel("Translate Parameters")
        translate_min_layout = QHBoxLayout(self) 
        translate_max_layout = QHBoxLayout(self) 

        rotate_parameters_title = QLabel("Rotate Parameters")
        rotate_min_layout = QHBoxLayout(self)
        rotate_max_layout = QHBoxLayout(self)

        scale_parameters_title = QLabel("Scale Parameters")
        scale_min_layout = QHBoxLayout(self)
        scale_max_layout = QHBoxLayout(self)


        #number_segment_label = QLabel("Number of Segments")
        #number_segment_input = QTextEdit()
        #number_segment_input.setFixedSize(100,30)
        #number_segment_layout.addWidget(number_segment_label)
        #number_segment_layout.addWidget(number_segment_input)

    
        #pole_height_label = QLabel("Pole Height")
        #pole_height_input = QTextEdit()
        #pole_height_input.setFixedSize(100,30)
        #pole_height.addWidget(pole_height_label)
        #pole_height.addWidget(pole_height_input)

        #plank_lenght_label = QLabel("Plank Height")
        #plank_lenght_input = QTextEdit()
        #plank_lenght_input.setFixedSize(100,30)
        #plank_lenght.addWidget(plank_lenght_label)
        #plank_lenght.addWidget(plank_lenght_input)

        create_button = QPushButton("Create Fence")
        create_button.clicked.connect(lambda: self.create_object(int(number_segment_input.toPlainText()),
                                                                 int(pole_height_input.toPlainText()),int(plank_lenght_input.toPlainText())))

        main_layout.addWidget(animation_timing_title)
        main_layout.addLayout(animation_timing_layout)

        main_layout.addWidget(create_button)

    def create_object(self):

        print("Hello")





def other():

    print("")
