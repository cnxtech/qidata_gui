from .editable_tree import EditableTree

from PySide.QtGui import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox

from qidata import annotationitems

class AnnotationMaker(QWidget):

    def __init__(self):
        super(AnnotationMaker, self).__init__()

        ## VIEW DEFINITION

        # Top layer widget: annotation definition
        self.definition_widget = QWidget(self)

        self.annotation_type_selection_widget = QComboBox(self.definition_widget)

        self.topic_vlayout = QVBoxLayout(self)
        self.topic_vlayout.addWidget(self.annotation_type_selection_widget)

        self.definition_widget.setLayout(self.topic_vlayout)

        # Middle widget: annotation composition
        self.editable_tree = EditableTree(self)

        # Bottom layer widget: Import data from another frame and save the current annotation
        self.utils_widget = QWidget(self)

        self.import_button = QPushButton("Import from...", self.utils_widget)
        self.save_button = QPushButton("Save", self.utils_widget)

        self.utils_hlayout = QHBoxLayout(self)
        self.utils_hlayout.addWidget(self.import_button)
        self.utils_hlayout.addWidget(self.save_button)
        self.utils_widget.setLayout(self.utils_hlayout)


        # Integrate all the widgets and the top layer widget into the main layout
        self.main_vlayout = QVBoxLayout(self)
        self.main_vlayout.addWidget(self.definition_widget)
        self.main_vlayout.addWidget(self.editable_tree)
        self.main_vlayout.addWidget(self.utils_widget)
        self.setLayout(self.main_vlayout)

        ## GUI ELEMENT SETUP

        # Save button
        self.save_button.setEnabled(True)

        # Import button
        self.import_button.setEnabled(True)

        # Topic selection
        self.annotation_type_selection_widget.addItems(annotationitems.__all__) # we add some message type

        self.show()