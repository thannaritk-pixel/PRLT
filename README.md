# PRLT — Probabilistic Reversal Learning Task (Thai, web version)

Browser-based Probabilistic Reversal Learning Task with Thai instructions, ported from the author's PsychoPy v8 task for a test–retest reliability study in Thai healthy adults. The task structure replicates Waltmann, Schlagenhauf & Deserno (2022).

แบบทดสอบ PRLT ภาษาไทยบนเว็บเบราว์เซอร์ พัฒนาจากโปรแกรม PsychoPy เวอร์ชัน 8 สำหรับการศึกษา reliability ในผู้ใหญ่ไทยสุขภาพดี

## เปิดใช้งาน (Web app)

| Version | URL |
| --- | --- |
| รูปทรง (PRLT-v9.2-web) | https://thannaritk-pixel.github.io/PRLT/ |
| Fractal (PRLT-v9.3-fractal) | https://thannaritk-pixel.github.io/PRLT/fractal/ |

**ติดตั้งบน iPad:** เปิด URL ใน Safari → ปุ่มแชร์ → "เพิ่มไปยังหน้าจอโฮม" (Add to Home Screen) แล้วเปิดจากไอคอนทุกครั้ง แอปจะเปิดเต็มจอโดยไม่มีแถบเบราว์เซอร์ และเปิดได้แม้ไม่มีอินเทอร์เน็ตหลังจากเปิดครั้งแรกแล้ว

### การเก็บข้อมูลเมื่อเปิดจาก GitHub Pages

- ข้อมูลเก็บในเบราว์เซอร์ของเครื่องนั้นเท่านั้น (IndexedDB) ไม่ส่งไปที่ใด
- **ส่งออก CSV หลังจบทุก session:** หน้าจบมีปุ่ม "ส่งออก CSV ตอนนี้" บน iPad จะเปิดหน้าแชร์ให้เลือก "บันทึกไปยังไฟล์" (Save to Files)
- แท็บ "ข้อมูลที่เก็บ" แสดงว่าแต่ละ session "ส่งออกแล้ว" หรือ "ยังไม่ส่งออก"
- ใช้แอปที่ติดตั้งบนหน้าจอโฮม Safari อาจลบข้อมูลของเว็บไซต์ที่ไม่ได้เปิดนาน ส่วนแอปบนหน้าจอโฮมไม่ถูกลบด้วยเงื่อนไขนี้ แต่ข้อมูลจะหายถ้าลบแอปหรือล้างข้อมูลเว็บไซต์
- ข้อมูลแต่ละ session บันทึก `platform` ว่าทำบน `github-pages`, `claude-artifact` หรือ `local-file`

### เปิด GitHub Pages (ทำครั้งเดียว)

Settings → Pages → Build and deployment → Source: **Deploy from a branch** → Branch: **main** / **(root)** → Save. URL ใช้งานได้ภายในไม่กี่นาที

## Versions

| Folder | Version | Stimuli |
| --- | --- | --- |
| `index.html` | PRLT-v9.2-web | Coloured shapes (V1 squares, V2 diamonds) |
| `fractal/index.html` | PRLT-v9.3-fractal | Julia-set fractals matched on CIELAB L* mean 58, L* SD 20, chroma 34 |

Both versions use the same task: 10 practice trials, then 160 trials; 80/20 reward probabilities, outcomes drawn fresh each trial; reversals after trials 55, 70, 90, 105 and 125; break after trial 80; fixation 500 ms, response window 2,500 ms, feedback 1,200 ms, ITI 500 ms. Responses by touch or the F / J keys. RT is measured from the first frame on which the stimuli are drawn, and RT < 150 ms is flagged (`rt_anticipatory`). Every session stores its random seed.

Use test mode ("โหมดทดลองระบบ", 20 trials, reversals after 8 and 14) to check a device before collecting data. Test sessions are labelled `test`.

## Files

| Path | Purpose |
| --- | --- |
| `index.html`, `fractal/index.html` | The two apps (single self-contained pages) |
| `manifest.webmanifest`, `fractal/manifest.webmanifest` | Web app manifests (name, icons, standalone display) |
| `icons/`, `fractal/icons/` | App icons |
| `sw.js` | Service worker for offline use: pages network-first, fonts cache-first |
| `fractal/stimuli/` | Fractal images and `generate_fractals.py` (numpy, Pillow, scikit-image) |

## Output

One trial-level CSV per session and one behavioural summary CSV. Column names include those of the PsychoPy v8.1 files (`choice_num`, `outcome`, `missed`, `rt` in seconds, `reversal_this_trial`) so existing analysis scripts read them. Behavioural indices: `stay`, `win_stay`, `lose_stay`, `persev_opportunity`, `perseverate` (perseveration as defined by Waltmann et al., 2022).

## Reference

Waltmann, M., Schlagenhauf, F., & Deserno, L. (2022). Sufficient reliability of the behavioral and computational readouts of a probabilistic reversal learning task. *Behavior Research Methods, 54*(6), 2993–3014. https://doi.org/10.3758/s13428-021-01739-7
