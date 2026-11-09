
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QTextEdit,QSpinBox
)

import importlib
import Functions
importlib.reload(Functions)

class RandomAnimator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Generator")
        self.setFixedWidth(400)
        self.setFixedHeight(600)
        self.build_ui()
    
    def build_ui(self):
        main_layout = QVBoxLayout(self)

        
        animation_timing_title = QLabel("Animation Timing")
        animation_timing_layout = QHBoxLayout(self)

        animation_timing_duration_label = QLabel("Durations (Frames):")
        animation_timing_duration_value = QSpinBox()
        animation_timing_duration_value.setRange(0,999)
        animation_timing_step_label = QLabel("Step (Frames):")
        animation_timing_step_value = QSpinBox()
        animation_timing_step_value.setRange(0,999)

        animation_timing_layout.addWidget(animation_timing_duration_label)
        animation_timing_layout.addWidget(animation_timing_duration_value)
        animation_timing_layout.addWidget(animation_timing_step_label)
        animation_timing_layout.addWidget(animation_timing_step_value)

        
        translate_parameters_title = QLabel("Translate Parameters")
        translate_min_layout = QHBoxLayout(self) 
        translate_max_layout = QHBoxLayout(self) 

        translate_min_x_label = QLabel("Min x:")
        translate_min_x_value = QSpinBox()
        translate_min_x_value.setRange(0,999)
        translate_min_y_label = QLabel("Min y:")
        translate_min_y_value = QSpinBox()
        translate_min_y_value.setRange(0,999)      
        translate_min_z_label = QLabel("Min z:")
        translate_min_z_value = QSpinBox()
        translate_min_z_value.setRange(0,999)

        translate_max_x_label = QLabel("Max x:")
        translate_max_x_value = QSpinBox()
        translate_max_x_value.setRange(0,999)
        translate_max_y_label = QLabel("Max y:")
        translate_max_y_value = QSpinBox()
        translate_max_y_value.setRange(0,999)
        translate_max_z_label = QLabel("Max z:")
        translate_max_z_value = QSpinBox()
        translate_max_z_value.setRange(0,999)

        translate_min_layout.addWidget(translate_min_x_label)
        translate_min_layout.addWidget(translate_min_x_value)
        translate_min_layout.addWidget(translate_min_y_label)
        translate_min_layout.addWidget(translate_min_y_value)
        translate_min_layout.addWidget(translate_min_z_label)
        translate_min_layout.addWidget(translate_min_z_value)

        translate_max_layout.addWidget(translate_max_x_label)
        translate_max_layout.addWidget(translate_max_x_value)
        translate_max_layout.addWidget(translate_max_y_label)
        translate_max_layout.addWidget(translate_max_y_value)
        translate_max_layout.addWidget(translate_max_z_label)
        translate_max_layout.addWidget(translate_max_z_value)



        rotate_parameters_title = QLabel("Rotate Parameters")
        rotate_min_layout = QHBoxLayout(self)
        rotate_max_layout = QHBoxLayout(self)

        rotate_min_x_label = QLabel("Min x:")
        rotate_min_x_value = QSpinBox()
        rotate_min_x_value.setRange(0,999)
        rotate_min_y_label = QLabel("Min y:")
        rotate_min_y_value = QSpinBox()
        rotate_min_y_value.setRange(0,999)
        rotate_min_z_label = QLabel("Min z:")
        rotate_min_z_value = QSpinBox()
        rotate_min_z_value.setRange(0,999)

        rotate_max_x_label = QLabel("Max x:")
        rotate_max_x_value = QSpinBox()
        rotate_max_x_value.setRange(0,999)
        rotate_max_y_label = QLabel("Max y:")
        rotate_max_y_value = QSpinBox()
        rotate_max_y_value.setRange(0,999)        
        rotate_max_z_label = QLabel("Max z:")
        rotate_max_z_value = QSpinBox()
        rotate_max_z_value.setRange(0,999)

        rotate_min_layout.addWidget(rotate_min_x_label)
        rotate_min_layout.addWidget(rotate_min_x_value)
        rotate_min_layout.addWidget(rotate_min_y_label)                
        rotate_min_layout.addWidget(rotate_min_y_value)
        rotate_min_layout.addWidget(rotate_min_z_label)
        rotate_min_layout.addWidget(rotate_min_z_value)
  
        rotate_max_layout.addWidget(rotate_max_x_label)
        rotate_max_layout.addWidget(rotate_max_x_value)
        rotate_max_layout.addWidget(rotate_max_y_label)
        rotate_max_layout.addWidget(rotate_max_y_value)
        rotate_max_layout.addWidget(rotate_max_z_label)
        rotate_max_layout.addWidget(rotate_max_z_value)


        scale_parameters_title = QLabel("Scale Parameters")
        scale_min_layout = QHBoxLayout(self)
        scale_max_layout = QHBoxLayout(self)

        scale_min_x_label = QLabel("Min x:")
        scale_min_x_value = QSpinBox()
        scale_min_x_value.setRange(0,999)
        scale_min_y_label = QLabel("Min y:")
        scale_min_y_value = QSpinBox()
        scale_min_y_value.setRange(0,999)        
        scale_min_z_label = QLabel("Min z:")
        scale_min_z_value = QSpinBox()
        scale_min_z_value.setRange(0,999)

        scale_max_x_label = QLabel("Max x:")
        scale_max_x_value = QSpinBox()
        scale_max_x_value.setRange(0,999)
        scale_max_y_label = QLabel("Max y:")
        scale_max_y_value = QSpinBox()
        scale_max_y_value.setRange(0,999)        
        scale_max_z_label = QLabel("Max z:")
        scale_max_z_value = QSpinBox()
        scale_max_z_value.setRange(0,999)     

        scale_min_layout.addWidget(scale_min_x_label)
        scale_min_layout.addWidget(scale_min_x_value)
        scale_min_layout.addWidget(scale_min_y_label)
        scale_min_layout.addWidget(scale_min_y_value)
        scale_min_layout.addWidget(scale_min_z_label)
        scale_min_layout.addWidget(scale_min_z_value)

        scale_max_layout.addWidget(scale_max_x_label)
        scale_max_layout.addWidget(scale_max_x_value)
        scale_max_layout.addWidget(scale_max_y_label)
        scale_max_layout.addWidget(scale_max_y_value)
        scale_max_layout.addWidget(scale_max_z_label)
        scale_max_layout.addWidget(scale_max_z_value)



        create_button = QPushButton("Generate")
        create_button.clicked.connect(lambda: Functions.generate_animation())


        main_layout.addWidget(animation_timing_title)
        main_layout.addLayout(animation_timing_layout)

        main_layout.addWidget(translate_parameters_title)
        main_layout.addLayout(translate_min_layout)
        main_layout.addLayout(translate_max_layout)

        main_layout.addWidget(rotate_parameters_title)
        main_layout.addLayout(rotate_min_layout)
        main_layout.addLayout(rotate_max_layout)

        main_layout.addWidget(scale_parameters_title)
        main_layout.addLayout(scale_min_layout)
        main_layout.addLayout(scale_max_layout)
        
        main_layout.addWidget(create_button)
