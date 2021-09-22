from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from dataset_yolo.dataset_yolo_process import DatasetYoloFactory
        # Instantiate process object
        return DatasetYoloFactory()

    def getWidgetFactory(self):
        from dataset_yolo.dataset_yolo_widget import DatasetYoloWidgetFactory
        # Instantiate associated widget object
        return DatasetYoloWidgetFactory()
