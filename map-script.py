from predict import dataset_predict_json
import json


# Получить информацию о боксах.
def get_boxes(path):
    return json.load(open(path, "r"))


# Расчет Intersection Over Union
def calculate_iou(matches, detections):
    ious = []

    for match, detection in zip(matches['boxes'], detections['predictions']):
        # Ширина/высота обоих боксов
        match_width, pred_width = float(match['width']), float(detection['width'])
        match_height, pred_height = float(match['height']), float(detection['height'])
        # Начальные координаты
        x1, y1 = float(match['x']), float(detection['x'])
        x2, y2 = float(match['x']) + match_width, float(match['y']) + match_height
        x3, y3 = float(detection['x']), float(detection['y'])
        x4, y4 = float(detection['x']) + pred_width, float(detection['y']) + pred_height
        # Оверлап боксов
        area_of_intersect = (x2 - x3) * (y2 - y3)
        # Объединение боксов
        area_of_union = ((x2 - x1) * (y2 - y1)) + ((x4 - x3) * (y4 - y3)) - area_of_intersect
        # Вычисленный IoU
        iou = area_of_intersect / area_of_union
        # Объект IoU
        current_iou = {
            "iou": iou,
            "detection_id": detection['detection_id'],
            'match_id': match['match_id']
        }
        # Добавляем в список
        ious.append(current_iou)

    return ious


# Получить матрицу
def get_confusion_matrix(threshold=0.5):
    matches = get_boxes("test_map/test.json")
    detections = get_boxes("test_map/predictions/test.jpg.json")
    ious = calculate_iou(matches, detections)

    tp, fp = 0, 0
    for iou_object in ious:
        if iou_object['iou'] >= threshold:
            tp += 1
        else:
            fp += 1

    return [tp, fp]


# Получить метрику precision
def get_precision(matrix):
    tp, fp = matrix
    return tp / (tp + fp)


# Получить метрику recall
def get_recall(matrix):
    tp, fp = matrix
    return tp / (tp + fp)


get_confusion_matrix()
