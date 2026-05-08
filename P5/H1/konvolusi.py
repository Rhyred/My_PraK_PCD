import numpy as np

def konvolusi_2d(image, kernel):
    # Baca ukuran citra dan kernel
    h, w = image.shape[:2]
    kh, kw = kernel.shape[:2]
    
    # H dan W untuk margin batas kernel
    pad_h, pad_w = kh // 2, kw // 2
    
    # Padding pinggiran citra biar piksel di ujung tetep bisa dikonvolusi
    padded_img = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    out_img = np.zeros_like(image, dtype=np.float32)
    
    # Looping konvolusi (pseudo-code baris 5 & 6)
    for i in range(h):
        for j in range(w):
            # Inner loop (k & l) diganti pakai numpy slicing biar GUI nggak nge-hang
            region = padded_img[i:i+kh, j:j+kw]
            
            # sum = sum + (w*a) -> Dihitung langsung satu blok
            out_img[i, j] = np.sum(region * kernel)
            
    # Memastikan nilai piksel mentok di 0-255
    out_img = np.clip(out_img, 0, 255).astype(np.uint8)
    return out_img