import os
import sys

# Add the current directory to PYTHONPATH
current_directory = os.getcwd()

sys.path.append(current_directory)
#sys.path.append("/work/vision_lab/DenseSSL/SlotCon-main/transfer/segmentation/mmsegmentation/projects/Fundus/gamma3")

_base_ = [
    './orvs_512x512.py', 'mmseg::_base_/models/fcn_unet_s5-d16.py',
    'mmseg::_base_/default_runtime.py',
    'mmseg::_base_/schedules/schedule_20k.py'
]
custom_imports = dict(imports='datasets.orvs_dataset')
img_scale = (512, 512)
data_preprocessor = dict(size=img_scale)
optimizer = dict(lr=0.01)
optim_wrapper = dict(optimizer=optimizer)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=2),
    auxiliary_head=None,
    test_cfg=dict(mode='whole', _delete_=True))
vis_backends = None
visualizer = dict(vis_backends=vis_backends)
