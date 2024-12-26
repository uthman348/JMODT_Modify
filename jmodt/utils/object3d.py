# import numpy as np


# class Object3d:
#     def __init__(self, line):
#         label = line.strip().split(' ')
#         self.cls_type = label[0]
#         self.truncation = float(label[1])
#         self.occlusion = float(label[2])  # 0:fully visible 1:partly occluded 2:largely occluded 3:unknown
#         self.alpha = float(label[3])
#         self.box2d = np.array((float(label[4]), float(label[5]), float(label[6]), float(label[7])), dtype=np.float32)
#         self.h = float(label[8])
#         self.w = float(label[9])
#         self.l = float(label[10])
#         self.pos = np.array((float(label[11]), float(label[12]), float(label[13])), dtype=np.float32)
#         self.dis_to_cam = np.linalg.norm(self.pos)
#         self.ry = float(label[14])
#         self.score = float(label[15]) if label.__len__() == 16 else -1.0

#     def to_kitti_format(self):
#         kitti_str = '%s %d %d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f' \
#                     % (self.cls_type, int(self.truncation), int(self.occlusion), self.alpha,
#                        self.box2d[0], self.box2d[1], self.box2d[2], self.box2d[3],
#                        self.h, self.w, self.l, self.pos[0], self.pos[1], self.pos[2], self.ry)
#         return kitti_str




import numpy as np


class Object3d:
    def __init__(self, line):
        label = line.strip().split(' ')

        # Handle DontCare entries
        if label[2] == "DontCare":
            self.cls_type = "DontCare"
            self.truncation = None
            self.occlusion = None
            self.alpha = None
            self.box2d = np.array([float(label[6]), float(label[7]), float(label[8]), float(label[9])], dtype=np.float32)
            self.h = None
            self.w = None
            self.l = None
            self.pos = None
            self.dis_to_cam = None
            self.ry = None
            self.score = None
            return

        # Parse valid objects
        self.cls_type = label[2]
        self.truncation = float(label[3])
        self.occlusion = float(label[4])
        self.alpha = float(label[5])
        self.box2d = np.array([float(label[6]), float(label[7]), float(label[8]), float(label[9])], dtype=np.float32)
        self.h = float(label[10])
        self.w = float(label[11])
        self.l = float(label[12])
        self.pos = np.array([float(label[13]), float(label[14]), float(label[15])], dtype=np.float32)
        self.dis_to_cam = np.linalg.norm(self.pos)
        self.ry = float(label[16])
        self.score = float(label[17]) if len(label) == 18 else -1.0

    def to_kitti_format(self):
        if self.cls_type == "DontCare":
            return "DontCare 0 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"
        
        kitti_str = '%s %d %d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f' \
                    % (self.cls_type, int(self.truncation), int(self.occlusion), self.alpha,
                       self.box2d[0], self.box2d[1], self.box2d[2], self.box2d[3],
                       self.h, self.w, self.l, self.pos[0], self.pos[1], self.pos[2], self.ry)
        return kitti_str
