# 一手证据与成熟实现

优先使用官方文档、原始论文和维护良好的参考实现。公开结果用于形成候选，不替代本项目实验。

## 基础配方

- PyTorch 性能调优指南：<https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html>
- TorchVision 分类参考实现：<https://github.com/pytorch/vision/tree/main/references/classification>
- TorchVision 现代分类配方：<https://pytorch.org/blog/how-to-train-state-of-the-art-models-using-torchvision-latest-primitives/>
- ResNet 训练技巧综述实验：<https://openaccess.thecvf.com/content_CVPR_2019/html/He_Bag_of_Tricks_for_Image_Classification_with_Convolutional_Neural_Networks_CVPR_2019_paper.html>
- ResNet Strikes Back：<https://openreview.net/forum?id=NG6MJnVl6M5>

## 批量与优化

- 大批量线性缩放与预热：<https://arxiv.org/abs/1706.02677>
- 大批量泛化差距：<https://openreview.net/forum?id=H1oyRlYgg>

## 增强与正则化

- AutoAugment：<https://openaccess.thecvf.com/content_CVPR_2019/html/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.html>
- RandAugment：<https://openaccess.thecvf.com/content_CVPRW_2020/html/w40/Cubuk_RandAugment_Practical_Automated_Data_Augmentation_With_a_Reduced_Search_Space_CVPRW_2020_paper.html>
- TrivialAugment Wide：<https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.TrivialAugmentWide.html>
- MixUp：<https://openreview.net/forum?id=r1Ddp1-Rb>
- CutMix：<https://openaccess.thecvf.com/content_ICCV_2019/html/Yun_CutMix_Regularization_Strategy_to_Train_Strong_Classifiers_With_Localizable_Features_ICCV_2019_paper.html>
- 随机擦除：<https://ojs.aaai.org/index.php/AAAI/article/view/7000>

## 权重平均

- PyTorch `AveragedModel` 与批归一化处理：<https://docs.pytorch.org/docs/main/generated/torch.optim.swa_utils.AveragedModel.html>
- TorchVision 分类参考实现：<https://github.com/pytorch/vision/blob/main/references/classification/train.py>
- TorchVision 现代 ResNet 配方与 EMA 消融：<https://pytorch.org/blog/how-to-train-state-of-the-art-models-using-torchvision-latest-primitives/>
- `timm` 的 `ModelEmaV3`：<https://github.com/huggingface/pytorch-image-models/blob/main/timm/utils/model_ema.py>
- TensorFlow Model Garden 动态衰减与延迟启动：<https://www.tensorflow.org/api_docs/python/tfm/optimization/ExponentialMovingAverage>
- EMA 动态、停止时点与批归一化研究：<https://arxiv.org/abs/2411.18704>
- NVIDIA TAO 分类 EMA 配置：<https://docs.nvidia.com/tao/tao-toolkit/latest/text/cv_finetuning/pytorch/image_classification_pyt.html>

## 工程参考

- PyTorch Image Models：<https://github.com/huggingface/pytorch-image-models>
- NVIDIA 卷积网络参考：<https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets>
- FFCV：<https://github.com/libffcv/ffcv>
- NVIDIA DALI：<https://github.com/NVIDIA/DALI>

引用这些来源时说明模型、数据集、训练时长、硬件和评估协议差异。不要把不同输入分辨率、不同轮数或不同网络的数字直接横向比较。
