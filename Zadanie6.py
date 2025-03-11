import cv2

sciezka_obraz = "profilowe.jpg"
obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    szary = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    twarze = face_cascade.detectMultiScale(szary, 1.3, 5)

    for (x, y, w, h) in twarze:
        srodek_twarzy = (x + w // 2, y + h // 2)
        promien_twarzy = max(w, h) // 2
        cv2.circle(obraz, srodek_twarzy, promien_twarzy, (255, 0, 0), 2)

        roi_gray = szary[y : y + h, x : x + w]
        roi_color = obraz[y : y + h, x : x + w]

        oczy = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)

        for i, (ex, ey, ew, eh) in enumerate(oczy[:2]):
            srodek_oka = (x + ex + ew // 2, y + ey + eh // 2)
            if i == 0:
                cv2.circle(obraz, srodek_oka, eh // 2 + 10, (0, 0, 255), -1)
            else:
                cv2.circle(obraz, srodek_oka, eh // 2 + 10, (0, 0, 255), -1)

        usta_x = x + w // 4
        usta_y = y + int(h * 0.7)
        usta_w = w // 2
        usta_h = h // 6
        cv2.rectangle(obraz, (usta_x, usta_y), (usta_x + usta_w, usta_y + usta_h), (0, 255, 0), -1)

    cv2.imshow("Zamazane zdjęcie", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
