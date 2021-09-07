from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class YOLO_Dataset(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from YOLO_Dataset.YOLO_Dataset_process import YOLO_DatasetProcessFactory
        # Instantiate process object
        return YOLO_DatasetProcessFactory()

    def getWidgetFactory(self):
        from YOLO_Dataset.YOLO_Dataset_widget import YOLO_DatasetWidgetFactory
        # Instantiate associated widget object
        return YOLO_DatasetWidgetFactory()
