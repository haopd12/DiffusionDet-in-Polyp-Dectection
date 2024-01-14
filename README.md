## Getting Started with DiffusionDet

### Introduction
This is the official code of DiffusionDet for Polyp Detection. We extend DiffusionDet for testing the result of using this new method instead of using YOLO...

### Installation

The codebases are built on top of [Detectron2](https://github.com/facebookresearch/detectron2), [Sparse R-CNN](https://github.com/PeizeSun/SparseR-CNN), and [denoising-diffusion-pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch).
Thanks very much.

#### Requirements
- Linux or macOS with Python ≥ 3.6
- PyTorch ≥ 1.9.0 and [torchvision](https://github.com/pytorch/vision/) that matches the PyTorch installation.
  You can install them together at [pytorch.org](https://pytorch.org) to make sure of this
- OpenCV is optional and needed by demo and visualization

#### Steps
1. Install Detectron2 following https://github.com/facebookresearch/detectron2/blob/main/INSTALL.md#installation.

2. Prepare datasets
- Install PolypsSet from Harvard Dataverse following https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FFCBUOR&fbclid=IwAR1qCNJWosoTP0Q9luPlY9vK2Ag-9MjmV-_JMpCFD91TRLIaD0UkuH--Aus
- Unzip file and save in the following directory ./PolypsSet/*
- To get dataset's instances, run following command:

```
cd PolypsSet
python devide_train_set.py
python devide_test_set.py
cd ..
```

3. Prepare pretrain models

DiffusionDet uses three backbones including ResNet-50, ResNet-101 and Swin-Base. The pretrained ResNet-50 model can be
downloaded automatically by Detectron2. We also provide pretrained
[ResNet-101](https://github.com/ShoufaChen/DiffusionDet/releases/download/v0.1/torchvision-R-101.pkl) and
[Swin-Base](https://github.com/ShoufaChen/DiffusionDet/releases/download/v0.1/swin_base_patch4_window7_224_22k.pkl) which are compatible with
Detectron2. Please download them to `DiffusionDet_ROOT/models/` before training:

```bash
mkdir models
cd models
# ResNet-101
wget https://github.com/ShoufaChen/DiffusionDet/releases/download/v0.1/torchvision-R-101.pkl

# Swin-Base
wget https://github.com/ShoufaChen/DiffusionDet/releases/download/v0.1/swin_base_patch4_window7_224_22k.pkl

cd ..
```

Thanks for model conversion scripts of [ResNet-101](https://github.com/PeizeSun/SparseR-CNN/blob/main/tools/convert-torchvision-to-d2.py)
and [Swin-Base](https://github.com/facebookresearch/Detic/blob/main/tools/convert-thirdparty-pretrained-model-to-d2.py).

4. Train DiffusionDet
```
python train_net.py --num-gpus 1 \
    --config-file configs/diffdet.polyp.res50.yaml
```

5. Evaluate DiffusionDet
```
python train_net.py --num-gpus 8 \
    --config-file configs/diffdet.polyp.res50.yaml \
    --eval-only MODEL.WEIGHTS path/to/model.pth
```

* Evaluate with 4 refinement steps by setting `MODEL.DiffusionDet.SAMPLE_STEP 4`.


### Inference Demo with Pre-trained Models
We provide a command line tool to run a simple demo of a set of images following [Detectron2](https://github.com/facebookresearch/detectron2/tree/main/demo#detectron2-demo).

```bash
python demo.py --config-file configs/diffdet.coco.res50.yaml \
    --input images_folder --opts MODEL.WEIGHTS diffdet_polyp_res50.pth
```


