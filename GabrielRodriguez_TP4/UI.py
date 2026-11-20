from PySide6.QtWidgets import (QWidget, QPushButton, 
                               QVBoxLayout, QHBoxLayout, 
                               QLabel,QSpinBox,QGroupBox)


#import maya.OpenMayaUI as omui
#from shiboken6 import wrapInstance

#def maya_main_window():
    #pointer = omui.MQtUtil.mainwindow()
    #return wrapInstance(int(pointer),QWidget)


import importlib
import Functions
importlib.reload(Functions)

class RadiusGenerator(QWidget):

    # defining the construction function 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radius Geometry Generator")
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        self.build_ui()


    #function that construction the window for gathering all the values
    def build_ui(self):

        # creating the main layout
        main_layout = QVBoxLayout(self)

        # ------------ RADIUS FROM POINTS -------------

        # creating the group and giving it its layouts 
        radius_value_group = QGroupBox("Radius From Center")
        radius_value_layout = QHBoxLayout(self)
        radius_value_group.setLayout(radius_value_layout)

        # creating all the value gathering widgets 
        radius_value_label = QLabel("Radius (cm) :")
        radius_value = QSpinBox()
        radius_value.setRange(1,999)

        # adding all widgets to the layouts of the group 
        radius_value_layout.addWidget(radius_value_label)
        radius_value_layout.addWidget(radius_value)
 

        # ------------ NUMBER OF OBJECTS  -------------
        
        # creating the group and giving it its layouts 
        nmb_obj_group = QGroupBox("Number Of Objects In Circumference")
        nmb_obj_layout = QHBoxLayout(self)
        nmb_obj_group.setLayout(nmb_obj_layout)

        # creating all the value gathering widgets 
        nmb_obj_label = QLabel("Number :")
        nmb_obj_value = QSpinBox()
        nmb_obj_value.setRange(1,360)

        # adding all widgets to the layouts of the group 
        nmb_obj_layout.addWidget(nmb_obj_label)
        nmb_obj_layout.addWidget(nmb_obj_value)

        # ------------ OBJECT SIZE -------------

        # creating the group and giving it its layouts 
        size_obj_group = QGroupBox("Size Of The Objects")
        size_obj_layout = QHBoxLayout(self)
        size_obj_group.setLayout(size_obj_layout)

        # creating all the value gathering widgets 
        size_obj_label = QLabel("Size (cm³) :")
        size_obj_value = QSpinBox()
        size_obj_value.setRange(1,999)

        # adding all widgets to the layouts of the group 
        size_obj_layout.addWidget(size_obj_label)
        size_obj_layout.addWidget(size_obj_value)


        # ------------ NUMBER OF REPETITION -------------

        # creating the group and giving it its layouts 
        repetition_value_group = QGroupBox("Number Of Repetitions")
        repetition_value_layout = QHBoxLayout(self)
        repetition_value_group.setLayout(repetition_value_layout)

        # creating all the value gathering widgets 
        repetition_value_label = QLabel("Repetitions :")
        repetition_value = QSpinBox()
        repetition_value.setRange(1,999)

        # adding all widgets to the layouts of the group 
        repetition_value_layout.addWidget(repetition_value_label)
        repetition_value_layout.addWidget(repetition_value)


        # ------------ DISTANCE BETWEEN REPETITIONs -------------

        # creating the group and giving it its layouts 
        distance_value_group = QGroupBox("Distance Between Repetitions")
        distance_value_layout = QHBoxLayout(self)
        distance_value_group.setLayout(distance_value_layout)

        # creating all the value gathering widgets 
        distance_value_label = QLabel("Distance (cm) :")
        distance_value = QSpinBox()
        distance_value.setRange(1,999)

        # adding all widgets to the layouts of the group 
        distance_value_layout.addWidget(distance_value_label)
        distance_value_layout.addWidget(distance_value)


        # ------------ BUTTON -------------

        create_button = QPushButton("Generate")

        # connect the button to a function (the lambda prevent the script from calling the function immediately)
        create_button.clicked.connect(lambda: Functions.radius_generation(radius_value.value(),nmb_obj_value.value(),
                                                                          size_obj_value.value(),repetition_value.value(),
                                                                          distance_value.value()))

        
        # add all groups to the main layout 
        main_layout.addWidget(radius_value_group)
        main_layout.addWidget(nmb_obj_group)
        main_layout.addWidget(size_obj_group)
        main_layout.addWidget(repetition_value_group)
        main_layout.addWidget(distance_value_group)
        main_layout.addWidget(create_button)
