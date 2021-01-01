import cv2

import config


def pretty_print(raw_total, raw_current, custom_processing="Processing ..."):
    # base 20 ####################
    total = raw_total - 1
    current = raw_current + 1
    size = int(20 * (raw_current / total))
    remain = 20 - size
    if remain > 0:
        return print(
            f"\r {current}/{raw_total} [",
            "#" * size,
            " " * remain,
            f"] {custom_processing}",
            end="",
        )
    else:
        return print(f"\n\r {current}/{raw_total} [", "#" * size, "] Done!\n", end="")


font = cv2.FONT_HERSHEY_SIMPLEX


def draw(frame, x, y, w, h, ids, name, dist):
    color = (200, 255, 0)

    if dist > config.THRESHOLD:
        name = "Unknown"
        dist = 0

        color = (200, 0, 255)

    cv2.rectangle(
        frame, (x, y), (x + w, y + h), color, 3
    )  # Gambar box untuk setiap wajah
        
    text = f"{name} {round(dist, 2)}"
    text_size = cv2.getTextSize(text, font, 0.5, 2)[0]
    cv2.rectangle(frame, (x - 3, y), (x + text_size[0], y - text_size[1] - 15), color, -1)

    cv2.putText(
        frame, text, (x, y - 10), font, 0.5, (50, 50, 50), 2,
    )
    return frame
