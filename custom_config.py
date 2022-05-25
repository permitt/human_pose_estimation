from config import Config


class CocoConfig(Config):
    def __init__(self):
        super()
        self.NAME = "coco_pose_estimation_azure"
        self.GPU_COUNT = 2
        self.NUM_CLASSES = 80 + 1

