import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread("C:/Users/Axong/Practice_/test1.jpg") # Первый тест
image = cv2.imread("C:/Users/Axong/Practice_/test2.jpg") # Второй тест 

# Размытие для подавления шума
blurred = cv2.GaussianBlur(image, (11, 11), 0)

# Перевод в HSV 
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# Диапазон зелёного цвета в HSV
green_min = np.array((40, 80, 80), np.uint8)   # Нижняя граница зелёного
green_max = np.array((80, 255, 255), np.uint8) # Верхняя граница зелёного

# Создание маски для зелёного цвета
green_mask = cv2.inRange(hsv, green_min, green_max)

# Нахождение контуров
contours, hierarchy = cv2.findContours(green_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Обрабатываем только внешние контуры
for i, contour in enumerate(contours):
    # Проверяем иерархию
    if hierarchy[0][i][3] == -1:  # Parent == -1 значит внешний контур
        area = cv2.contourArea(contour)
        if area > 500:  # отсекаем маленькие шумовые контуры (артефакты сглаживания)
            x, y, w, h = cv2.boundingRect(contour)
            center = (int(x + w / 2), int(y + h / 2))
            cv2.circle(image, center, 7, (0, 0, 255), 2)
# Показ результата
cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
