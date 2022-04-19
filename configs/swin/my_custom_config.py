model = dict(
    type='MaskRCNN' #检测器名称
    backbone = dict(
        type= 'ResNet',
        depth=50, #主干网络深度
        num_stages=4, #主干网络zhu
        out_indices=(0,1,2,3),
        fro
    )
)