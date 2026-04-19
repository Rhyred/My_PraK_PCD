import cv2
from pathlib import Path

base_dir = Path(__file__).parent
img_path = base_dir / "tes.jpg"

img = cv2.imread(str(img_path))
if img is None:
    raise FileNotFoundError(f"GaGal Load bro: {img_path}")

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
