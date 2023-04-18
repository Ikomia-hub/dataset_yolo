from ikomia import utils, core, dataprocess
from ikomia.utils import pyqtutils, qtconversion
from dataset_yolo.dataset_yolo_process import DatasetYoloParam
# PyQt GUI framework
from PyQt5.QtWidgets import *


# --------------------
# - Class which implements widget associated with the process
# - Inherits core.CProtocolTaskWidget from Ikomia API
# --------------------
class DatasetYoloWidget(core.CWorkflowTaskWidget):

    def __init__(self, param, parent):
        core.CWorkflowTaskWidget.__init__(self, parent)

        if param is None:
            self.parameters = DatasetYoloParam()
        else:
            self.parameters = param

        # Create layout : QGridLayout by default
        self.grid_layout = QGridLayout()

        self.browse_folder = pyqtutils.append_browse_file(grid_layout=self.grid_layout, label="YOLO dataset folder",
                                                          path=self.parameters.dataset_folder,
                                                          mode=QFileDialog.Directory)

        self.browse_class_file = pyqtutils.append_browse_file(grid_layout=self.grid_layout, label="YOLO classes file",
                                                              path=self.parameters.class_file_path,
                                                              mode=QFileDialog.ExistingFile)

        # PyQt -> Qt wrapping
        layout_ptr = qtconversion.PyQtToQt(self.grid_layout)

        # Set widget layout
        self.set_layout(layout_ptr)

    def on_apply(self):
        # Apply button clicked slot
        # Get parameters from widget
        self.parameters.dataset_folder = self.browse_folder.path
        self.parameters.class_file_path = self.browse_class_file.path

        # Send signal to launch the process
        self.emit_apply(self.parameters)


# --------------------
# - Factory class to build process widget object
# - Inherits dataprocess.CWidgetFactory from Ikomia API
# --------------------
class DatasetYoloWidgetFactory(dataprocess.CWidgetFactory):

    def __init__(self):
        dataprocess.CWidgetFactory.__init__(self)
        # Set the name of the process -> it must be the same as the one declared in the process factory class
        self.name = "dataset_yolo"

    def create(self, param):
        # Create widget object
        return DatasetYoloWidget(param, None)
