import os
import numpy as np
from PIL import Image
from skimage import color
OUT = os.path.dirname(os.path.abspath(__file__))
N = 480
def julia(c, zoom=1.5, rot=0.0, power=2, iters=300):
    y, x = np.mgrid[-zoom:zoom:N*1j, -zoom:zoom:N*1j]
    z = (x + 1j*y) * np.exp(1j*rot)
    out = np.zeros(z.shape); alive = np.ones(z.shape, bool)
    for i in range(iters):
        z[alive] = z[alive]**power + c
        esc = alive & (np.abs(z) > 4)
        out[esc] = i + 1 - np.log(np.log(np.abs(z[esc]))) / np.log(power)
        alive &= ~esc
    out[alive] = iters
    v = out / iters
    return v ** 0.45
def palette(v, stops):
    stops = np.array(stops, float) / 255.0
    pos = np.linspace(0, 1, len(stops))
    vv = (v * 3.0) % 1.0  # cycle the palette 3x for structure
    rgb = np.stack([np.interp(vv, pos, stops[:, k]) for k in range(3)], -1)
    return rgb
specs = {
  'v1_left':  dict(c=-0.8+0.156j, zoom=1.45, rot=0.3, stops=[(20,40,120),(60,140,230),(240,250,255),(30,80,180),(20,40,120)]),
  'v1_right': dict(c=0.285+0.01j, zoom=1.3, rot=0.0, stops=[(120,40,10),(240,150,40),(255,245,220),(200,90,20),(120,40,10)]),
  'v2_left':  dict(c=-0.4+0.6j, zoom=1.4, rot=1.1, stops=[(10,80,70),(40,190,170),(230,255,245),(20,130,110),(10,80,70)]),
  'v2_right': dict(c=-0.70176-0.3842j, zoom=1.45, rot=0.7, stops=[(110,20,80),(230,90,180),(255,235,245),(170,40,120),(110,20,80)]),
  'p_left':   dict(c=0.355+0.355j, zoom=1.3, rot=0.4, stops=[(40,90,20),(140,210,80),(245,255,230),(80,150,40),(40,90,20)]),
  'p_right':  dict(c=-0.123+0.745j, zoom=1.35, rot=0.0, stops=[(70,30,120),(170,120,230),(245,235,255),(110,60,180),(70,30,120)]),
}
T_MEAN, T_STD = 58.0, 20.0
report = []
for name, s in specs.items():
    v = julia(s['c'], s['zoom'], s['rot'])
    rgb = palette(v, s['stops'])
    lab = color.rgb2lab(rgb)
    L = lab[..., 0]
    lab[..., 0] = np.clip((L - L.mean()) / L.std() * T_STD + T_MEAN, 0, 100)
    ch = np.hypot(lab[...,1], lab[...,2]).mean(); lab[...,1:] *= 34.0 / ch
    for _ in range(6):  # iterate so the in-gamut result matches the targets
        out = np.clip(color.lab2rgb(lab), 0, 1)
        m = color.rgb2lab(out)
        lab[...,0] = np.clip(lab[...,0] + (T_MEAN - m[...,0].mean()), 0, 100)
        lab[...,1:] *= 34.0 / max(np.hypot(m[...,1], m[...,2]).mean(), 1e-6)
    out = np.clip(color.lab2rgb(lab), 0, 1)
    lab2 = color.rgb2lab(out)
    report.append((name, round(lab2[...,0].mean(),2), round(lab2[...,0].std(),2), round(np.hypot(lab2[...,1],lab2[...,2]).mean(),1)))
    Image.fromarray((out*255).astype(np.uint8)).save(os.path.join(OUT, f'{name}.jpg'), quality=88)
for r in report: print(r)
