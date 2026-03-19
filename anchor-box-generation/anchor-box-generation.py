def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # total_anchors = feature_size * feature_size * len(scales) * len(aspect_ratios)
    stride = image_size / feature_size

    # (cx, cy) of every grid
    centers = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride
            centers.append((cx, cy))

    # (w, h) of every boxes
    dims = []
    for s in scales:
        for r in aspect_ratios:
            w = s * (r ** 0.5)
            h = s / (r ** 0.5)
            dims.append((w, h))

    # [x1, y1, x2, y2] of every anchor boxes
    anchor_boxes = []
    for cx, cy in centers:
        for w, h in dims:
            box = [cx - w/2, cy - h/2, cx + w/2, cy + h/2]
            anchor_boxes.append(box)
    
    return anchor_boxes