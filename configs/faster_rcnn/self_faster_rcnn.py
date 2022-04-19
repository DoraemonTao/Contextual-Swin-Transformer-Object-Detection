base=[
    './configs/fast_rcnn/fast_rcnn_r50_fpn_1x_coco.py'
]

model= dict(
    roi_head= dict(
        bbox_head=dict(
            num_classes=3,
        )
    )
)

data = dict(
    train=dict(
        # ann_file='F:/Connect/orange_detection_COCO/annotations/voc_train.json',
        # img_prefix='F:/Connect/orange_detection_COCO/images/',
        ann_file='F:/Connect/datasets/datasets/train/instance_train.json',
        img_prefix='F:/Connect/datasets/datasets/train/images/',
        ),
    val=dict(
        # ann_file='F:/Connect/orange_detection_COCO/annotations/voc_test.json',
        # img_prefix='F:/Connect/orange_detection_COCO/images/',
        ann_file='F:/Connect/datasets/datasets/test/instance_test.json',
        img_prefix='F:/Connect/datasets/datasets/test/images/',

    ),
    test=dict(
        # ann_file='F:/Connect/orange_detection_COCO/annotations/voc_test.json',
        # img_prefix='F:/Connect/orange_detection_COCO/images/',
        ann_file='F:/Connect/datasets/datasets/test/instance_test.json',
        img_prefix='F:/Connect/datasets/datasets/test/images/',
    ))