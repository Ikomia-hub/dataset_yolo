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
        self.dataset_folder = ""
        self.class_file = ""

    def set_values(self, param_map):
        # Set parameters values from Ikomia application
        # Parameters values are stored as string and accessible like a python dict
        self.dataset_folder = param_map["dataset_folder"]
        self.class_file = param_map["class_file"]

    def get_values(self):
        # Send parameters values to Ikomia application
        # Create the specific dict structure (string container)
        param_map = {"dataset_folder": self.dataset_folder,
                     "class_file": self.class_file}
        return param_map


# --------------------
# - Class which implements the process
# - Inherits core.CProtocolTask or derived from Ikomia API
# --------------------
class DatasetYolo(core.CWorkflowTask):

    def __init__(self, name, param):
        core.CWorkflowTask.__init__(self, name)
        # Add input/output of the process here
        self.add_output(datasetio.IkDatasetIO("yolo"))
        self.add_output(dataprocess.CNumericIO())

        # Create parameters class
        if param is None:
            self.set_param_object(DatasetYoloParam())
        else:
            self.set_param_object(copy.deepcopy(param))

    def get_progress_steps(self):
        # Function returning the number of progress steps for this process
        # This is handled by the main progress bar of Ikomia application
        return 1

    def run(self):
        # Core function of your process
        # Call beginTaskRun for initialization
        self.begin_task_run()

        # Get parameters :
        param = self.get_param_object()

        # Get dataset output :
        output = self.get_output(0)
        output.data = dataset.load_yolo_dataset(param.dataset_folder, param.class_file)
        output.has_bckgnd_class = False

        # Class labels output
        numeric_out = self.get_output(1)
        numeric_out.clear_data()
        numeric_out.set_output_type(dataprocess.NumericOutputType.TABLE)

        class_ids = []
        for i in range(len(output.data["metadata"]["category_names"])):
            class_ids.append(i)

        numeric_out.add_value_list(class_ids, "Id", list(output.data["metadata"]["category_names"].values()))

        # Step progress bar:
        self.emit_step_progress()

        # Call endTaskRun to finalize process
        self.end_task_run()


# --------------------
# - Factory class to build process object
# - Inherits dataprocess.CProcessFactory from Ikomia API
# --------------------
class DatasetYoloFactory(dataprocess.CTaskFactory):

    def __init__(self):
        dataprocess.CTaskFactory.__init__(self)
        # Set process information as string here
        self.info.name = "dataset_yolo"
        self.info.short_description = "Load YOLO dataset"
        self.info.authors = "Ikomia team"
        self.info.license = "MIT License"
        self.info.documentation_link = "https://pjreddie.com/darknet/yolo/"
        self.info.repository = "https://github.com/Ikomia-hub/dataset_yolo"
        # relative path -> as displayed in Ikomia application process tree
        self.info.path = "Plugins/Python/Dataset"
        self.info.icon_path = "icons/yolo.png"
        self.info.version = "1.1.0"
        self.info.keywords = "yolo,dataset,annotation,train,dnn"
        self.info.algo_type = core.AlgoType.DATASET
        self.info.algo_tasks = "OBJECT_DETECTION"

    def create(self, param=None):
        # Create process object
        return DatasetYolo(self.info.name, param)
