import cv2

image = cv2.imread("scena.png")
template = cv2.imread("template.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
th, tw = template_gray.shape[::-1]

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

index = 1
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    if w < 20 or h < 20:
        continue

    roi = image[y:y+h, x:x+w]

    if roi.shape[0] >= template.shape[0] and roi.shape[1] >= template.shape[1]:
        roi_resized = cv2.resize(roi, (tw, th))

        roi_gray = cv2.cvtColor(roi_resized, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(roi_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.8:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f'ID: {index}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            print(f"Obiekt {index}: Dopasowanie = {max_val:.2f}")
            index += 1

cv2.imshow("Wykryte podobne obiekty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
