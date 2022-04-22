from ikomia import core, dataprocess
from ikomia.dnn import dataset, datasetio
import copy


# --------------------
# - Class to handle the process parameters
# - Inherits core.CProtocolTaskParam from Ikomia API
# --------------------
class DatasetYoloParam(core.CWorkflowTaskParam):

    def __init__(self):
        core.CWorkflowTaskParam.__init__(self)
        # Place default value initialization here
        self.data_folder_path = ""
        self.class_file_path = ""

    def setParamMap(self, param_map):
        # Set parameters values from Ikomia application
        # Parameters values are stored as string and accessible like a python dict
        self.data_folder_path = param_map["data_folder_path"]
        self.class_file_path = param_map["class_file_path"]

    def getParamMap(self):
        # Send parameters values to Ikomia application
        # Create the specific dict structure (string container)
        param_map = core.ParamMap()
        param_map["data_folder_path"] = self.data_folder_path
        param_map["class_file_path"] = self.class_file_path
        return param_map


# --------------------
# - Class which implements the process
# - Inherits core.CProtocolTask or derived from Ikomia API
# --------------------
class DatasetYolo(core.CWorkflowTask):

    def __init__(self, name, param):
        core.CWorkflowTask.__init__(self, name)
        # Add input/output of the process here
        self.addOutput(datasetio.IkDatasetIO("yolo"))
        self.addOutput(dataprocess.CNumericIO())

        # Create parameters class
        if param is None:
            self.setParam(DatasetYoloParam())
        else:
            self.setParam(copy.deepcopy(param))

    def getProgressSteps(self):
        # Function returning the number of progress steps for this process
        # This is handled by the main progress bar of Ikomia application
        return 1

    def run(self):
        # Core function of your process
        # Call beginTaskRun for initialization
        self.beginTaskRun()

        # Get parameters :
        param = self.getParam()

        # Get dataset output :
        output = self.getOutput(0)
        output.data = dataset.load_yolo_dataset(param.data_folder_path, param.class_file_path)
        output.has_bckgnd_class = False

        # Class labels output
        numeric_out = self.getOutput(1)
        numeric_out.clearData()
        numeric_out.setOutputType(dataprocess.NumericOutputType.TABLE)

        class_ids = []
        for i in range(len(output.data["metadata"]["category_names"])):
            class_ids.append(i)

        numeric_out.addValueList(class_ids, "Id", list(output.data["metadata"]["category_names"].values()))

        # Step progress bar:
        self.emitStepProgress()

        # Call endTaskRun to finalize process
        self.endTaskRun()


# --------------------
# - Factory class to build process object
# - Inherits dataprocess.CProcessFactory from Ikomia API
# --------------------
class DatasetYoloFactory(dataprocess.CTaskFactory):

    def __init__(self):
        dataprocess.CTaskFactory.__init__(self)
        # Set process information as string here
        self.info.name = "dataset_yolo"
        self.info.shortDescription = "Load YOLO dataset"
        self.info.description = "Load YOLO dataset. " \
                                "This plugin converts a given dataset in YOLO format to Ikomia format. " \
                                "Once loaded, all images can be visualized with their respective annotations. " \
                                "Then, any training algorithms from the Ikomia marketplace can be connected " \
                                "to this converter."
        self.info.authors = "Ikomia team"
        self.info.license = "MIT License"
        self.info.documentationLink = "https://pjreddie.com/darknet/yolo/"
        self.info.repo = "https://github.com/Ikomia-dev"
        # relative path -> as displayed in Ikomia application process tree
        self.info.path = "Plugins/Python/Dataset"
        self.info.iconPath = "icons/yolo.png"
        self.info.version = "1.1.0"
        self.info.keywords = "yolo,dataset,annotation,train,dnn"

    def create(self, param=None):
        # Create process object
        return DatasetYolo(self.info.name, param)
