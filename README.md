# PRLT — Probabilistic Reversal Learning Task (Thai, web version)

Browser-based Probabilistic Reversal Learning Task with Thai instructions, ported from the author's PsychoPy v8 task for a test–retest reliability study in Thai healthy adults. The task structure replicates Waltmann, Schlagenhauf & Deserno (2022).

แบบทดสอบ PRLT ภาษาไทยบนเว็บเบราว์เซอร์ พัฒนาจากโปรแกรม PsychoPy เวอร์ชัน 8 สำหรับการศึกษา reliability ในผู้ใหญ่ไทยสุขภาพดี

## Versions

| Folder | Version | Stimuli |
| --- | --- | --- |
| `index.html` | PRLT-v9.2-web | Coloured shapes (V1 squares, V2 diamonds) |
| `fractal/index.html` | PRLT-v9.3-fractal | Julia-set fractals matched on CIELAB L* mean 58, L* SD 20, chroma 34 |

Both versions use the same task: 10 practice trials, then 160 trials; 80/20 reward probabilities, outcomes drawn fresh each trial; reversals after trials 55, 70, 90, 105 and 125; break after trial 80; fixation 500 ms, response window 2,500 ms, feedback 1,200 ms, ITI 500 ms. Responses by touch or the F / J keys. RT is measured from the first frame on which the stimuli are drawn, and RT < 150 ms is flagged (`rt_anticipatory`). Every session stores its random seed.

## Running

Open `index.html` (or `fractal/index.html`) in a browser. Run as a standalone file, the app stores sessions in the browser's local storage and exports CSV from the "ข้อมูลที่เก็บ" tab. Hosted as a claude.ai artifact, it also writes sessions to the artifact's database.

Use test mode ("โหมดทดลองระบบ", 20 trials, reversals after 8 and 14) to check a device before collecting data. Test sessions are labelled `test`.

## Output

One trial-level CSV per session and one behavioural summary CSV. Column names include those of the PsychoPy v8.1 files (`choice_num`, `outcome`, `missed`, `rt` in seconds, `reversal_this_trial`) so existing analysis scripts read them. Behavioural indices: `stay`, `win_stay`, `lose_stay`, `persev_opportunity`, `perseverate` (perseveration as defined by Waltmann et al., 2022).

## Fractal stimuli

`fractal/stimuli/generate_fractals.py` regenerates the six images (numpy, Pillow, scikit-image). The images are embedded in `fractal/index.html` as data URIs.

## Reference

Waltmann, M., Schlagenhauf, F., & Deserno, L. (2022). Sufficient reliability of the behavioral and computational readouts of a probabilistic reversal learning task. *Behavior Research Methods, 54*(6), 2993–3014. https://doi.org/10.3758/s13428-021-01739-7
