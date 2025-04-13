import cv2

class BoxVisualizer:
    def __init__(self, image_path, gt_boxes, pred_boxes):
        self.image_path = image_path
        self.cv2_im = cv2.imread(self.image_path)

        if self.cv2_im is None:
            raise ValueError(f"Ошибка: Не удалось загрузить изображение {self.image_path}")

        self.gt_boxes = gt_boxes
        self.pred_boxes = pred_boxes

    # ---------------------------------------------------
    # Наносение GT и предсказанных боксов на изображение
    # ---------------------------------------------------
    def draw_boxes(self):
        for cls in self.gt_boxes.keys():
            gt_boxes = self.gt_boxes.get(cls, [])
            pred_boxes = self.pred_boxes.get(cls, [])

            # Отрисовка Ground Truth боксов (синие)
            for x0, y0, x1, y1, _ in gt_boxes:
                cv2.rectangle(self.cv2_im, (x0, y0), (x1, y1), (255, 0, 0), 2)

            # Отрисовка предсказанных боксов (голубые)
            for x0, y0, x1, y1, _ in pred_boxes:
                cv2.rectangle(self.cv2_im, (x0, y0), (x1, y1), (100, 149, 237), 2)

    # ---------------------------------------------------
    # Рендер изображения с нанесёнными на него боксами
    # ---------------------------------------------------
    def show_image(self, resize_ratio=1.0):
        self.draw_boxes()

        if resize_ratio != 1.0:
            new_size = (int(self.cv2_im.shape[1] / resize_ratio), int(self.cv2_im.shape[0] / resize_ratio))
            self.cv2_im = cv2.resize(self.cv2_im, new_size, interpolation=cv2.INTER_LINEAR)

        cv2.imshow("Image with Boxes", self.cv2_im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()