# importation 
import maya.cmds as cmds 
import json  
import os 
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QTextEdit,QPushButton, QMessageBox, QCheckBox


# --------------------------------------------------------------------
#                         CLASS
# --------------------------------------------------------------------

# creation de la class ParameterBoard  
class ParameterBoard(QWidget):

    # contructeur du Widget
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outliner Organizer")
        self.create_ui()

    # fonction de creation du UI du Widget principale 
    def create_ui(self):

        # creation du layout principale 
        layout = QVBoxLayout(self)

        # creation du message d'entrer 
        label = QLabel("Enter JSON file path")

        # utiliser QTextEdit pour avoir le nom du fichier JSON 
        text_input = QTextEdit("file path...")
        text_input.setFixedSize(400,30)

        # creation des 3 checkbox 
        check_selection = QCheckBox("Apply on selection only")
        check_colors = QCheckBox("Apply colors")
        check_reorder = QCheckBox("Apply reorder")

        # creation du bouton 
        button_apply = QPushButton("Organize Outliner")

        # connecter le button a la fonction on_click 
        button_apply.clicked.connect(lambda: self.on_click(text_input.toPlainText(), check_selection.isChecked(),check_colors.isChecked(),
                                                           check_reorder.isChecked()))
        
        # ajouter tout les element au layout principal 
        layout.addWidget(label)
        layout.addWidget(text_input)
        layout.addWidget(check_selection)
        layout.addWidget(check_colors)
        layout.addWidget(check_reorder)
        layout.addWidget(button_apply)


    # fonction qui effectue l'organisation de l'outliner quand le bouton est appuye 
    def on_click(self,file_path,selection_bool, color_bool, reorder_bool): 

        # lecture du fichier JSON
        with open(file_path, "r", encoding="utf-8") as file:
            color_identity = json.load(file)

        # creation d'un chunk pour implementer une fonction de ctrl z 
        cmds.undoInfo(openChunk=True, chunkName="Organization")

        # chunk d'organisation 
        try:


          # ACTION SUR SELECTION 
           
          if selection_bool == True: 

            # aller chercher tout les element selectionne sur Maya 
            all_items_selected = cmds.ls(selection=True, long=True)

            if color_bool == True:

              # ACTION DE COLORATION SUR SELECTION 
              
              # iteration sur les elements selectionne pour avoir leur noms 
              for item in all_items_selected: 
                item_name = item.split("|")[-1]

                # iteration sur le fichier json pour changer la couleur des elements
                for name, color in color_identity.items():

                   # changer la couleur selon les noms qui corresponde
                   if name.lower() in item_name.lower():
                     cmds.setAttr(item + ".useOutlinerColor",1)
                     cmds.setAttr(item + ".outlinerColor", color[0], color[1], color[2], type="double3")

            if reorder_bool == True: 

              # ACTION D'ORGANISATION SUR SELECTION 

              # organiser les element en ordre alphabetique (le resultat est de Z a A)
              items_sorted = sorted(all_items_selected, key=lambda x: x.split("|")[-1].lower())

              # iteration sur l'inverse des elemtents organise (donc de A a Z)
              for i in reversed(items_sorted):

                 # iteration sur le fichier json afin de verifier sur l'element fait partit de la regle 
                 for name, color in color_identity.items():
                   if name.lower() in i.lower():

                      # organiser l'element dans l'outliner
                      cmds.reorder(i,front=True)
                    
          else:

           # ACTION SUR TOUT 
         
           # aller chercher tout les element sur Maya 
           all_items = cmds.ls(dag=True, long=True)

           if color_bool == True:

            # ACTION DE COLORATION SUR TOUT
            
            # iteration sur les elements selectionne pour avoir leur noms 
            for item in all_items: 
              item_name = item.split("|")[-1]

              # iteration sur le fichier json pour changer la couleur des elements
              for name, color in color_identity.items():

                 # changer la couleur selon les noms qui corresponde
                 if name.lower() in item_name.lower():
                     cmds.setAttr(item + ".useOutlinerColor",1)
                     cmds.setAttr(item + ".outlinerColor", color[0], color[1], color[2], type="double3")

           if reorder_bool == True:

            # ACTION D'ORGANISATION SUR TOUT
          
            # organiser les element en ordre alphabetique (le resultat est de Z a A)
            items_sorted = sorted(all_items, key=lambda x: x.split("|")[-1].lower())

            # iteration sur l'inverse des elemtents organise (donc de A a Z)
            for i in reversed(items_sorted):

                 # iteration sur le fichier json afin de verifier sur l'element fait partit de la regle 
                 for name, color in color_identity.items():
                   if name.lower() in i.lower():

                      # organiser l'element dans l'outliner
                      cmds.reorder(i,front=True)
            
        # option de retour sur le chunk 
        finally: 
           cmds.undoInfo(closeChunk=True)



# --------------------------------------------------------------------
#                         MAIN
# --------------------------------------------------------------------
    
def main():

    # creation du widget global 
    global widget

    # fermer l'ancien widget 
    try:
        widget.close()
    except Exception:
        pass 

    # faire apparaitre le widget ParameterBoard
    widget = ParameterBoard()
    widget.show()


main()


